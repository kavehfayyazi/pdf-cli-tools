import argparse
import sys
from pikepdf import Pdf as PDF
from utils import validate_file_exists, get_valid_filename, expand_pages

# pdf-tools rotate <path> [-p <pages | --pages <pages>] [-a deg | --angle deg] [-o <out>]
def rotate():
    parser = argparse.ArgumentParser(
        prog='pdf_tools.py rotate',
        description='Rotate a PDF',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('path',             help='file path of the PDF',                            type=str)
    parser.add_argument('-p', '--pages',  help='selected pages of the PDF',                       type=str, default='all')
    parser.add_argument('-a', '--angle',    help='clockwise degrees of rotation (e.g. 90,180,270)', type=int, default=90)
    parser.add_argument('-o', '--out',      help='file name of the output PDF',                     type=str, default='rotated.pdf')
    args = parser.parse_args(sys.argv[2:])

    path = args.path
    pages = args.pages
    angle = args.angle

    # Error checking nonexistent PDF
    validate_file_exists(path)
    with PDF.open(path) as pdf:
        select_pages = expand_pages(pdf, pages)
        for page_num in select_pages:
            pdf.pages[page_num].rotate(angle, relative=True)
        filename = get_valid_filename(path)
        pdf.save(filename)