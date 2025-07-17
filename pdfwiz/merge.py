"""
pdf_tools.merge

Implements the 'merge' command for the pdf-tools CLI.
Provides functions to merge two PDF files into a single PDF, 
optionally specifying particular pages or ranges from each input file.
"""

from argparse import ArgumentParser, Namespace
from pikepdf import Pdf as PDF
from pdfwiz.utils import validate_file_exists, get_valid_filename, expand_page_ranges

def add_arguments(parser: ArgumentParser):
    """Appends the 'merge' parser arguments to the parser passed.

    Args:
        parser (ArgumentParser): The original subparser.
    """
    parser.add_argument('path1',            help='file path of the first PDF',              type=str)
    parser.add_argument('path2',            help='file path of the second PDF',             type=str)
    parser.add_argument('-p1', '--pages1',  help='selected pages or ranges of first PDF',   type=str,   default='all')
    parser.add_argument('-p2', '--pages2',  help='selected pages or ranges of second PDF',  type=str,   default='all')
    parser.add_argument('-o', '--out',      help='file name of the output PDF',             type=str,   default='merged.pdf')

def run(args: Namespace):
    """Runs the 'merge' command.
    
    Usage:
        pdf-tools merge <path1> <path2> [-p1 <pages1> | --pages1 <pages1>] [-p2 <pages2> | --pages2 <pages2>] [-o <out>]

    Args:
        args (Namespace): Parsed command-line arguments with the following attributes:
            path1 (str): Path to the first PDF file.
            path2 (str): Path to the second PDF file.
            pages1 (str): Pages or ranges to include from the first PDF (default: 'all').
            pages2 (str): Pages or ranges to include from the second PDF (default: 'all').
            out (str): Output file name (default: 'merged.pdf').
    """
    merged = PDF.new()

    validate_file_exists(args.path1)
    validate_file_exists(args.path2)

    for path, page_ranges in [(args.path1, args.pages1), (args.path2, args.pages2)]:
        with PDF.open(path) as pdf:
            for page_num in expand_page_ranges(pdf, page_ranges):
                merged.pages.append(pdf.pages[page_num])

    filename = get_valid_filename(args.out)
    merged.save(filename)