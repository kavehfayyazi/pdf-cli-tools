#!/usr/bin/env python3

import argparse
import merge
import rotate
import reverse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="pdf-tools", description='Merge two PDFs')
    subparsers = parser.add_subparsers(dest="command", required=True)

    merge_parser = subparsers.add_parser("merge", help="Merge two PDFs")
    merge.add_arguments(merge_parser)

    rotate_parser = subparsers.add_parser("rotate", help="Rotate pages in a PDF")
    rotate.add_arguments(rotate_parser)

    reverse_parser = subparsers.add_parser("reverse", help="Reverse pages in a PDF")
    reverse.add_arguments(reverse_parser)

    args, unknown = parser.parse_known_args()

    match args.command:
        case 'merge':
            merge.run(args)
        case 'rotate':
            rotate.run(args)
        case 'reverse':
            reverse.run(args)