#!/usr/bin/env python3

import argparse
from pdf_tools import merge
from pdf_tools import rotate
from pdf_tools import delete
from pdf_tools import reverse

def main():
    parser = argparse.ArgumentParser(prog="pdf-tools", description='Merge two PDFs')
    subparsers = parser.add_subparsers(dest="command", required=True)

    merge_parser = subparsers.add_parser("merge", help="Merge two PDFs")
    rotate_parser = subparsers.add_parser("rotate", help="Rotate pages in a PDF")
    delete_parser = subparsers.add_parser("delete", help="Delete pages in a PDF")
    reverse_parser = subparsers.add_parser("reverse", help="Reverse pages in a PDF")

    merge.add_arguments(merge_parser)
    rotate.add_arguments(rotate_parser)
    delete.add_arguments(delete_parser)
    reverse.add_arguments(reverse_parser)

    args, unknown = parser.parse_known_args()
    match args.command:
        case 'merge': merge.run(args)
        case 'rotate': rotate.run(args)
        case 'delete': delete.run(args)
        case 'reverse': reverse.run(args)