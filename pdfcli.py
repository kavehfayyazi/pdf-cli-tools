#!/usr/bin/env python3

import sys
from pdf_tools import merge, rotate, reverse

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage pdf-tools <merge|rotate|reverse> [options]")
        sys.exit(1)

    command = sys.argv[1]
    match command:
        case 'merge':
            merge()
        case 'rotate':
            rotate()
        case 'reverse':
            reverse()
        case _:
            print(f"Unknown command: {command}")
            sys.exit(1)