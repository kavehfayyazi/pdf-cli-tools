#!/usr/bin/env python3

import argparse
from merge import merge
from reverse import reverse
from rotate import rotate

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="pdf-tools", description='Merge two PDFs')
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("merge", help="Merge two PDFs")
    subparsers.add_parser("rotate", help="Rotate pages in a PDF")
    subparsers.add_parser("reverse", help="Reverse pages in a PDF")

    args, unknown = parser.parse_known_args()

    match args.command:
        case 'merge':
            merge()
        case 'rotate':
            rotate()
        case 'reverse':
            reverse()