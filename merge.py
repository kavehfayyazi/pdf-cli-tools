import argparse
import sys
from pikepdf import Pdf as PDF
from utils import validate_file_exists, get_valid_filename, expand_pages

# pdf-tools merge <path1> <path2> [-p1 <pages1> | -pages1 <pages1>] [-p2 <pages2> | --pages2 <pages2>] [-o <out>]
def merge():
    parser = argparse.ArgumentParser(
        prog='pdf_tools.py merge',
        description='Merge two PDFs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('path1',            help='file path of the first PDF',      type=str)
    parser.add_argument('path2',            help='file path of the second PDF',     type=str)
    parser.add_argument('-p1', '--pages1',  help='selected pages of first PDF',     type=str, default='all')
    parser.add_argument('-p2', '--pages2',  help='selected pages of second PDF',    type=str, default='all')
    parser.add_argument('-o', '--out',      help='file name of the output PDF',     type=str, default='merged.pdf')
    args = parser.parse_args(sys.argv[2:])

    merged = PDF.new()

    # Error checking nonexistent PDFs
    validate_file_exists(args.path1)
    validate_file_exists(args.path2)
        
    for path, pages in [(args.path1, args.pages1), (args.path2, args.pages2)]:
        with PDF.open(path) as pdf:
            for page_num in expand_pages(pdf, pages):
                merged.pages.append(pdf.pages[page_num])

    filename = get_valid_filename(args.out)
    merged.save(filename)
