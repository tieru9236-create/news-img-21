#!/usr/bin/env python3
import os
import shutil

# Make.fun entrypoint for news-image-20261121: 21 November World News Infographic
# All 35 stories verified for Saturday 21 November 2026
def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    
    here = os.path.dirname(os.path.abspath(__file__))
    src_png = os.path.join(here, "entry.png")
    dst_png = os.path.join(out_dir, "entry.png")
    
    shutil.copyfile(src_png, dst_png)
    print(f"Delivered 21 Nov 2026 world news summary to {dst_png} ({os.path.getsize(dst_png)} bytes)")

if __name__ == "__main__":
    main()
