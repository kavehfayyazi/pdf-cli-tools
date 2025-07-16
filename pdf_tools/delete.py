import argparse
from pikepdf import Pdf as PDF
from pdf_tools.utils import validate_file_exists, get_valid_filename, expand_pages

def add_arguments(parser):
    parser.add_argument('path',             help='file path of the PDF',            type=str)
    parser.add_argument('pages',            help='selected pages of the PDF',         type=str)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', '--in-place', help='edit the PDF in place, overwriting the original file', action='store_true')
    group.add_argument('-o', '--out',      help='file name of the output PDF',     type=str, default='deleted.pdf')

# pdf-tools reverse <path> [-p <pages | --pages <pages>] [-o <out>]
def run(args):
    path = args.path
    pages = args.pages

    validate_file_exists(path)

    with PDF.open(path, allow_overwriting_input=args.in_place) as pdf:
        all_pages = expand_pages(pdf, 'all')
        select_pages = expand_pages(pdf, pages)

        deleted = PDF.new()
        for page_num in (x for x in all_pages if x not in select_pages):
            deleted.pages.append(pdf.pages[page_num])

        filename = path if args.in_place else get_valid_filename(args.out)
        deleted.save(filename)