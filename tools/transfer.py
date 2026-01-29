#!/usr/bin/env python3
from pathlib import Path
import zipfile
import argparse


def export_folder(src, out):
    src = Path(src)
    out = Path(out)
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in src.rglob('*'):
            if p.is_file():
                z.write(p, arcname=str(p.relative_to(src)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Bundle a folder of canon files for transfer.')
    parser.add_argument('src', nargs='?', default='canon', help='source folder to bundle')
    parser.add_argument('out', nargs='?', default='canon.zip', help='output zip filename')
    args = parser.parse_args()
    export_folder(args.src, args.out)
    print(f'Exported {args.src} -> {args.out}')
