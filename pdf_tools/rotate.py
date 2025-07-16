"""
pdf_tools.rotate

Implements the 'rotate' command for the pdf-tools CLI.
Provides functions to rotate particular pages or ranges of a PDF.
"""

from argparse import ArgumentParser, Namespace
from pikepdf import Pdf as PDF
from pdf_tools.utils import validate_file_exists, get_valid_filename, expand_page_ranges

def add_arguments(parser: ArgumentParser):
    """Appends the 'rotate' parser arguments to the parser passed.

    Args:
        parser (ArgumentParser): The original subparser.
    """
    parser.add_argument('path',             help='file path of the PDF',                                type=str)
    parser.add_argument('-p', '--pages',    help='selected pages or ranges of the PDF',                 type=str,   default='all')
    parser.add_argument('-a', '--angle',    help='clockwise degrees of rotation (e.g. 90,180,270)',     type=int,   default=90)
    group = parser.add_mutually_exclusive_group() # -i and -o flags are mutually exclusive: in-place vs. output file
    group.add_argument('-i', '--in-place',  help='edit the PDF in place, overwriting the original file',    action='store_true')
    group.add_argument('-o', '--out',       help='file name of the output PDF',                         type=str,   default='rotated.pdf')

def run(args: Namespace):
    """Runs the 'rotate' command.
    
    Usage:
        pdf-tools rotate <path> [-p <pages> | --pages <pages>] [-a <deg> | --angle <deg>] [-i | --in-place] [-o <out>]

    Args:
        args (Namespace): Parsed command-line arguments with the following attributes:
            path (str): Path to the PDF file.
            pages (str): Pages or ranges to include from the PDF (default: 'all').
            angle (int): Angle in degrees (90, 180, 270) to rotate pages clockwise (default: 90).
            in_place (bool): If True, overwrites the original file (default: False).
            out (str): Output file name (default: 'rotated.pdf').
    """
    validate_file_exists(args.path)

    with PDF.open(args.path, allow_overwriting_input=args.in_place) as pdf:
        select_pages = expand_page_ranges(pdf, args.pages)
        for page_num in select_pages:
            # Rotate each page by the angle relative to its current rotation
            pdf.pages[page_num].rotate(args.angle, relative=True)
        # Set output file path to input file path if -i flag is marked
        filename = args.path if args.in_place else get_valid_filename(args.out)
        pdf.save(filename)