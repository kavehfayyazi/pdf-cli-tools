"""
pdf_tools.reverse

Implements the 'reverse' command for the pdf-tools CLI.
Provides functions to reverse particular pages or ranges of a PDF.
"""

from argparse import ArgumentParser, Namespace
from pikepdf import Pdf as PDF
from pdf_tools.utils import validate_file_exists, get_valid_filename, expand_page_ranges

def add_arguments(parser: ArgumentParser):
    """Appends the 'reverse' parser arguments to the parser passed.

    Args:
        parser (ArgumentParser): The original subparser.
    """
    parser.add_argument('path',             help='file path of the PDF',                    type=str)
    parser.add_argument('-p', '--pages',    help='selected pages or ranges of the PDF',     type=str,   default='all')
    group = parser.add_mutually_exclusive_group() # -i and -o flags are mutually exclusive: in-place vs. output file
    group.add_argument('-i', '--in-place',  help='edit the PDF in place, overwriting the original file',    action='store_true')
    group.add_argument('-o', '--out',       help='file name of the output PDF',             type=str,   default='reversed.pdf')

def run(args: Namespace):
    """Runs the 'reverse' command.
    
    Usage:
        pdf-tools reverse <path> [-p <pages> | --pages <pages>] [-i | --in-place] [-o <out>]

    Args:
        args (Namespace): Parsed command-line arguments with the following attributes:
            path (str): Path to the PDF file.
            pages (str): Pages or ranges to reverse from the PDF (default: 'all').
            in_place (bool): If True, overwrites the original file (default: False).
            out (str): Output file name (default: 'reversed.pdf').
    """
    validate_file_exists(args.path)

    with PDF.open(args.path, allow_overwriting_input=args.in_place) as pdf:
        if args.pages == 'all': 
            pdf.pages.reverse() # Built in pikepdf reverse function for entire PDF
        else:
            select_pages = expand_page_ranges(pdf, args.pages)
            # Temporary list to store selected pages
            reversed_pages = [pdf.pages[page_num] for page_num in reversed(select_pages)]
            for i, page_num in enumerate(select_pages):
                pdf.pages[page_num] = reversed_pages[i]
        filename = args.path if args.in_place else get_valid_filename(args.out)
        pdf.save(filename)