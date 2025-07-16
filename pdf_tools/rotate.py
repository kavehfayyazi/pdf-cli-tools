import argparse
from pikepdf import Pdf as PDF
from pdf_tools.utils import validate_file_exists, get_valid_filename, expand_pages

def add_arguments(parser):
    parser.add_argument('path',             help='file path of the PDF',                            type=str)
    parser.add_argument('-p', '--pages',  help='selected pages of the PDF',                       type=str, default='all')
    parser.add_argument('-a', '--angle',    help='clockwise degrees of rotation (e.g. 90,180,270)', type=int, default=90)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', '--in-place', help='edit the PDF in place, overwriting the original file', action='store_true')
    group.add_argument('-o', '--out',      help='file name of the output PDF',                     type=str, default='rotated.pdf')

# pdf-tools rotate <path> [-p <pages | --pages <pages>] [-a deg | --angle deg] [-o <out>]
def run(args):
    path = args.path
    pages = args.pages
    angle = args.angle

    # Error checking nonexistent PDF
    validate_file_exists(path)
    with PDF.open(path) as pdf:
        select_pages = expand_pages(pdf, pages)
        for page_num in select_pages:
            pdf.pages[page_num].rotate(angle, relative=True)
        filename = path if args.in_place else get_valid_filename(args.out)
        pdf.save(filename)