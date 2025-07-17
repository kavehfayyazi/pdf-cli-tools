"""
pdf_tools.delete

Implements the 'delete' command for the pdf-tools CLI.
Provides functions to delete select pages or ranges of a PDF.
"""

from argparse import ArgumentParser, Namespace
from pikepdf import Pdf as PDF
from pdfwiz.utils import validate_file_exists, get_valid_filename, expand_page_ranges

def add_arguments(parser: ArgumentParser):
    """Appends the 'delete' parser arguments to the parser passed.

    Args:
        parser (ArgumentParser): The original subparser.
    """
    parser.add_argument('path',             help='file path of the PDF',                    type=str)
    parser.add_argument('pages',            help='selected pages or ranges of the PDF',     type=str)
    group = parser.add_mutually_exclusive_group() # -i and -o flags are mutually exclusive: in-place vs. output file
    group.add_argument('-i', '--in-place',  help='edit the PDF in place, overwriting the original file', action='store_true')
    group.add_argument('-o', '--out',       help='file name of the output PDF',             type=str,   default='deleted.pdf')

def run(args: Namespace):
    """Runs the 'delete' command.
    
    Usage:
        pdf-tools delete <path> <pages> [-i | --in-place] [-o <out>]

    Args:
        args (Namespace): Parsed command-line arguments with the following attributes:
            path (str): Path to the PDF file.
            pages (str): Pages or ranges to include from the PDF.
            in_place (bool): If True, overwrites the original file (default: False).
            out (str): Output file name (default: 'deleted.pdf').
    """
    validate_file_exists(args.path)

    with PDF.open(args.path, allow_overwriting_input=args.in_place) as pdf:
        all_pages = expand_page_ranges(pdf, 'all')
        select_pages = expand_page_ranges(pdf, args.pages)
        pages_kept = [x for x in all_pages if x not in select_pages]

        deleted = PDF.new()

        for page_num in pages_kept:
            deleted.pages.append(pdf.pages[page_num])

        filename = args.path if args.in_place else get_valid_filename(args.out)
        deleted.save(filename)