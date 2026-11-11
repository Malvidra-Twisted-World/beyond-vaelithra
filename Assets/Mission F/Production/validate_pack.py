"""Read-only PNG integrity, dimensions and token alpha checks; then package assets."""
import hashlib
import json
import re
import shutil
import struct
import zipfile
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def inspect_png(path):
    data = path.read_bytes()
    assert data[:8] == b'\x89PNG\r\n\x1a\n', path
    pos, compressed = 8, bytearray()
    while pos < len(data):
        size = struct.unpack('>I', data[pos:pos + 4])[0]
        kind = data[pos + 4:pos + 8]
        payload = data[pos + 8:pos + 8 + size]
        crc = struct.unpack('>I', data[pos + 8 + size:pos + 12 + size])[0]
        assert zlib.crc32(kind + payload) & 0xffffffff == crc, path
        if kind == b'IHDR':
            w, h, bits, color, comp, filt, interlace = struct.unpack('>IIBBBBB', payload)
        if kind == b'IDAT':
            compressed.extend(payload)
        pos += 12 + size
        if kind == b'IEND':
            break
    assert bits == 8 and color in (2, 6) and interlace == 0, path
    bpp = 4 if color == 6 else 3
    raw = zlib.decompress(compressed)
    stride = w * bpp
    assert len(raw) == h * (stride + 1), path
    alpha_min, alpha_max, corner_alpha = 255, 0, []
    if color == 6:
        previous = bytearray(stride)
        offset = 0
        for y in range(h):
            mode = raw[offset]
            row = bytearray(raw[offset + 1:offset + 1 + stride])
            for x in range(stride):
                a = row[x - bpp] if x >= bpp else 0
                b = previous[x]
                c = previous[x - bpp] if x >= bpp else 0
                if mode == 1:
                    predictor = a
                elif mode == 2:
                    predictor = b
                elif mode == 3:
                    predictor = (a + b) // 2
                elif mode == 4:
                    p = a + b - c
                    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                    predictor = a if pa <= pb and pa <= pc else b if pb <= pc else c
                else:
                    assert mode == 0, path
                    predictor = 0
                row[x] = (row[x] + predictor) & 255
            alphas = row[3::4]
            alpha_min = min(alpha_min, min(alphas))
            alpha_max = max(alpha_max, max(alphas))
            if y in (0, h - 1):
                corner_alpha.extend((alphas[0], alphas[-1]))
            previous = row
            offset += stride + 1
    record = dict(file=path.relative_to(ROOT).as_posix(), width=w, height=h,
                  mode='RGBA' if color == 6 else 'RGB', bytes=len(data),
                  sha256=hashlib.sha256(data).hexdigest())
    if path.parent.name == 'Tokens':
        assert color == 6 and w == h and alpha_min == 0 and alpha_max == 255, path
        assert max(corner_alpha) <= 5, (path, corner_alpha)
        record.update(alpha_min=alpha_min, alpha_max=alpha_max, corner_alpha=corner_alpha,
                      display_cells=[1, 1])
    else:
        assert (w, h) == (1536, 1024), path
        record.update(grid_px=64, grid_offset_px=[0, 0], grid_cells=[24, 16], feet_per_cell=5)
    return record


def main():
    maps = sorted((ROOT / 'Maps').glob('*.png'))
    tokens = sorted((ROOT / 'Tokens').glob('*.png'))
    assert len(maps) == 4 and len(tokens) == 9, (len(maps), len(tokens))
    records = [inspect_png(p) for p in maps + tokens]
    manifest = dict(mission='F - No Way Out', generator='Built-in image_gen',
                    local_png_checks='passed', vtt_import_tested=False, playtested=False,
                    wulan='Existing DM asset; not recreated or bundled', assets=records)
    (ROOT / 'Production' / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    guide = ROOT.parents[1] / 'Mission F - VTT Preparation.md'
    guide_text = re.sub(r'!\[\[Assets/Mission F/Maps/([^\]]+)\]\]', r'![](Maps/\1)', guide.read_text())
    (ROOT / 'DM Guide.md').write_text(guide_text)
    shutil.copy2(ROOT.parents[1] / 'Mission F - Combat Preparation.md', ROOT / 'Combat Preparation.md')
    shutil.copy2(ROOT.parents[1] / 'Lore' / 'Resonance - Thresholds & Effects Draft.md', ROOT / 'Resonance Rules.md')
    output = ROOT / 'mission-f-vtt-pack-v1.zip'
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
        for p in sorted(ROOT.rglob('*')):
            if p.is_file() and p != output:
                archive.write(p, p.relative_to(ROOT))
    with zipfile.ZipFile(output) as archive:
        assert archive.testzip() is None
        count = len(archive.namelist())
    print(json.dumps(dict(maps=len(maps), tokens=len(tokens), png_checks='passed',
                          zip_integrity='passed', zip_entries=count, zip_bytes=output.stat().st_size)))


if __name__ == '__main__':
    main()
