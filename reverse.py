import argparse
import sys
from pikepdf import Pdf as PDF
from utils import validate_file_exists, get_valid_filename, expand_pages

# pdf-tools reverse <path> [-p <pages | --pages <pages>] [-o <out>]
def reverse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',             help='file path of the PDF',                            type=str)
    parser.add_argument('-p', '--pages',  help='selected pages of the PDF',                       type=str)
    parser.add_argument('-o', '--out',      help='file name of the output PDF',                     type=str, default='reversed.pdf')
    args = parser.parse_args(sys.argv[2:])

    print(args)