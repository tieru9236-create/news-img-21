import zlib, struct
from pathlib import Path

def write_png(filename, width, height, pixels):
    raw_data = bytearray()
    for y in range(height):
        raw_data.append(0)
        for x in range(width):
            r, g, b = pixels(x, y, width, height)
            raw_data.extend((r, g, b))
    
    def chunk(chunk_type, data):
        return struct.pack('>I', len(data)) + chunk_type + data + struct.pack('>I', zlib.crc32(chunk_type + data) & 0xffffffff)

    png_bytes = b'\x89PNG\r\n\x1a\n'
    png_bytes += chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0))
    png_bytes += chunk(b'IDAT', zlib.compress(bytes(raw_data), level=9))
    png_bytes += chunk(b'IEND', b'')
    
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    with open(filename, 'wb') as f:
        f.write(png_bytes)

def news_art(x, y, w, h):
    ny = y / h
    nx = x / w
    # Infographic header band: deep slate blue
    if ny < 0.15:
        return (24, 32, 48)
    # 3-column split for world news digest
    col = int(nx * 3)
    # Divider lines
    if abs(nx - 0.333) < 0.003 or abs(nx - 0.666) < 0.003:
        return (200, 205, 215)
    # Background tone
    if col == 0: # Global Climate Summit & Tech
        r = int(240 - 20 * ny)
        g = int(245 - 15 * ny)
        b = int(250 - 10 * ny)
    elif col == 1: # World Financial Markets & AI
        r = int(248 - 15 * ny)
        g = int(248 - 15 * ny)
        b = int(242 - 10 * ny)
    else: # Space Exploration & Diplomacy
        r = int(242 - 15 * ny)
        g = int(245 - 20 * ny)
        b = int(252 - 10 * ny)
    return (r, g, b)

write_png('/output/entry.png', 1024, 1024, news_art)
print('News infographic generated.')
