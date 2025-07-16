import argparse
import sys
from pikepdf import Pdf as PDF
from utils import validate_file_exists, get_valid_filename, expand_pages

def add_arguments(parser):
    parser.add_argument('path',             help='file path of the PDF',            type=str)
    parser.add_argument('-p', '--pages',  help='selected pages of the PDF',         type=str, default='all')
    parser.add_argument('-i', '--in-place', help='edit the PDF in place, overwriting the original file', action='store_true')
    parser.add_argument('-o', '--out',      help='file name of the output PDF',     type=str, default='reversed.pdf')

# pdf-tools reverse <path> [-p <pages | --pages <pages>] [-o <out>]
def run(args):
    path = args.path
    pages = args.pages

    validate_file_exists(path)

    with PDF.open(path, allow_overwriting_input=args.in_place) as pdf:
        if pages == 'all':
            pdf.pages.reverse()
        else:
            select_pages = expand_pages(pdf, pages)
            reversed_pages = [pdf.pages[page_num] for page_num in reversed(select_pages)]
            for i, page_num in enumerate(select_pages):
                pdf.pages[page_num] = reversed_pages[i]
        filename = path if args.in_place else get_valid_filename(args.out)
        pdf.save(filename)