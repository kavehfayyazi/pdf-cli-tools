import sys
import os
from pikepdf import Pdf as PDF

def validate_file_exists(path: str):
    if not os.path.isfile(os.path.join(os.getcwd(), path)):
        print(f"Error: File not found: {path}", file=sys.stderr)
        sys.exit(1)

def get_valid_filename(filename: str) -> str:
    current_dir = os.getcwd()
    valid_name = ''
    i = 0
    while True:
        valid_name = filename if i == 0 else f'{filename.split('.')[0]}{i}.pdf'
        filepath = os.path.join(current_dir, valid_name)
        if os.path.isfile(filepath):
            i += 1
            continue
        break
    return valid_name

""" all -> 0 , len(pdf.pages) - 1

for customs,
it subtracts one to account for pages.pdf starting at 0

"""
def expand_pages(pdf: PDF, pages: str) -> list:
    if pages == 'all':
        return [x for x in range(len(pdf.pages))]
    else:
        page_list = []
        page_nums = pages.split(',')
        for page_range in page_nums:
            if ':' in page_range:
                parts = page_range.split(':')
                if len(parts) != 2 or not all(part.isdigit() for part in parts):
                    print(f"Error: Invalid page number: {page_range}", file=sys.stderr)
                    sys.exit(1)
                left, right = map(int, parts)
                for num in range(left - 1, right):
                    page_list.append(num)
            else:
                if not page_range.isdigit():
                    print(f"Error: Invalid page number: {page_range}", file=sys.stderr)
                    sys.exit(1)
                page_list.append(int(page_range) - 1)
        if page_list == []:
            print(f"Error: Invalid page number: {page_range}", file=sys.stderr)
            sys.exit(1)
        for page_num in page_list:
            if page_num < 0 or page_num >= len(pdf.pages):
                print(f"Error: Invalid page number: {page_num + 1}", file=sys.stderr)
                sys.exit(1)
        # remove duplicates and preserve order
        seen = set()
        page_list = [x for x in page_list if not (x in seen or seen.add(x))]
        return page_list