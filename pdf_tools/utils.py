"""
pdf_tools.utils

Provides utility functions to aid with the pdf-tools CLI.

API:
- validate_file_exists(path: str) -> None
- get_valid_filename(filename: str) -> str
- expand_page_ranges(pdf: PDF, pages: str) -> list
"""

import sys
import os
from pikepdf import Pdf as PDF

def validate_file_exists(path: str):
    """Ensures a PDF file exists at the passed path.

    Args:
        path (str): Path of the file
    """
    if not os.path.isfile(os.path.join(os.getcwd(), path)):
        print(f"Error: File not found: {path}", file=sys.stderr)
        sys.exit(1)

def get_valid_filename(filename: str) -> str:
    """Renames filename until unique depending on current working directory.

    Args:
        filename (str): Name of the file
    Returns:
        str: Unique file name
    """
    current_dir = os.getcwd()
    valid_name = ''
    i = 0
    while True:
        root, ext = os.path.splitext(filename)
        valid_name = f"{root}{i if i > 0 else ''}{ext or '.pdf'}"
        filepath = os.path.join(current_dir, valid_name)
        if os.path.isfile(filepath):
            i += 1
            continue
        break
    return valid_name

def expand_page_ranges(pdf: PDF, pages: str) -> list:
    """Parses specified pages and ranges into a list of unique, 0-indexed page numbers.

    Args:
        pdf (PDF): The PDF to validate against.
        pages (str): A string of pages and ranges (e.g. '1,3:5').
    Returns:
        list: A list of unique 0-indexed page numbers.
    """
    if pages == 'all':
        return [x for x in range(len(pdf.pages))]
    else:
        page_list = []
        page_nums = pages.split(',')
        for page_range in page_nums:
            if ':' in page_range: # Page Range
                parts = page_range.split(':')
                if len(parts) != 2 or not all(part.isdigit() for part in parts):
                    print(f"Error: Invalid page number: {page_range}", file=sys.stderr)
                    sys.exit(1)
                left, right = map(int, parts)
                for num in range(left - 1, right):
                    page_list.append(num)
            else: # Single Page
                if not page_range.isdigit():
                    print(f"Error: Invalid page number: {page_range}", file=sys.stderr)
                    sys.exit(1)
                page_list.append(int(page_range) - 1)
        for page_num in page_list: # Ensure valid pages
            if page_num < 0 or page_num >= len(pdf.pages):
                print(f"Error: Invalid page number: {page_num + 1}", file=sys.stderr)
                sys.exit(1)
        # Remove duplicates with preserved order
        seen = set()
        page_list = [x for x in page_list if not (x in seen or seen.add(x))]
        return page_list