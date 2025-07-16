import argparse
import sys
import os
from pikepdf import Pdf as PDF

# pdf-tools merge <path1> <path2> [-p1 <pages1> | -pages1 <pages1>] [-p2 <pages2> | --pages2 <pages2>] [-o <out>]
def merge():
    parser = argparse.ArgumentParser(
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
    for path in [args.path1, args.path2]:
        if not os.path.isfile(os.path.join(os.getcwd(), path)):
            print(f"Error: File not found: {path}", file=sys.stderr)
            return 
        
    for path, pages in [(args.path1, args.pages1), (args.path2, args.pages2)]:
        with PDF.open(path) as pdf:
            if pages == 'all':
                for i in range(len(pdf.pages)):
                    merged.pages.append(pdf.pages[i])
            else:
                page_list = []
                page_nums = pages.split(',')
                for page_range in page_nums:
                    # change any if they have a colon
                    if ':' in page_range:
                        left, right = page_range.split(':')
                        for num in range(int(left), int(right) + 1):
                            page_list.append(num)
                    else:
                        page_list.append(page_range)
                for page_num in page_list:
                    # Error checking for invalid page numbers
                    if int(page_num) < 1 or int(page_num) > len(pdf.pages):
                        print(f"Error: Invalid page number ({path}): {page_num}", file=sys.stderr)
                        return
                    merged.pages.append(pdf.pages[int(page_num) - 1])

    # File Name
    current_dir = os.getcwd()
    filename = ''
    i = 0
    while True:
        filename = args.out if i == 0 else f'{args.out}{i}.pdf'
        filepath = os.path.join(current_dir, filename)
        if os.path.isfile(filepath):
            i += 1
            continue
        break

    merged.save(filename)

# pdf-tools rotate <path> [-p <pages | --pages <pages>] [-a deg | --angle deg] [-o <out>]
def rotate():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',             help='file path of the PDF',                            type=str)
    parser.add_argument('-p', '--pages',  help='selected pages of the PDF',                       type=str)
    parser.add_argument('-a', '--angle',    help='clockwise degrees of rotation (e.g. 90,180,270)', type=int, default=90)
    parser.add_argument('-o', '--out',      help='file name of the output PDF',                     type=str, default='rotated.pdf')
    args = parser.parse_args(sys.argv[2:])

    print(args)

# pdf-tools reverse <path> [-p <pages | --pages <pages>] [-o <out>]
def reverse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',             help='file path of the PDF',                            type=str)
    parser.add_argument('-p', '--pages',  help='selected pages of the PDF',                       type=str)
    parser.add_argument('-o', '--out',      help='file name of the output PDF',                     type=str, default='reversed.pdf')
    args = parser.parse_args(sys.argv[2:])

    print(args)