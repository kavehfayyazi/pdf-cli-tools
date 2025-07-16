import argparse
import sys

# pdf-tools merge <path1> <path2> [-p1 <pages1> | -pages1 <pages1>] [-p2 <pages2> | --pages2 <pages2>] [-o <out>]
# pdf-tools rotate <path> [-p <pages | --pages <pages>] [-a deg | --angle deg] [-o <out>]
# pdf-tools reverse <path> [-p <pages | --pages <pages>] [-o <out>]

def merge():
    parser = argparse.ArgumentParser()
    parser.add_argument("path1",            help="file path of the first PDF",      type=str)
    parser.add_argument("path2",            help="file path of the second PDF",     type=str)
    parser.add_argument("-p1", "--pages1",  help="selected pages of first PDF",     type=str, default="all")
    parser.add_argument("-p2", "--pages2",  help="selected pages of second PDF",    type=str, default="all")
    parser.add_argument("-o", "--out",      help="file name of the output PDF",     type=str, default="merged.pdf")
    args = parser.parse_args(sys.argv[2:])

    print(args)
def rotate():
    parser = argparse.ArgumentParser()
    parser.add_argument("path",             help="file path of the PDF",                            type=str)
    parser.add_argument("-p", "--pages",  help="selected pages of the PDF",                       type=str)
    parser.add_argument("-a", "--angle",    help="clockwise degrees of rotation (e.g. 90,180,270)", type=int, default=90)
    parser.add_argument("-o", "--out",      help="file name of the output PDF",                     type=str, default="rotated.pdf")
    args = parser.parse_args(sys.argv[2:])

    print(args)

def reverse():
    parser = argparse.ArgumentParser()
    parser.add_argument("path",             help="file path of the PDF",                            type=str)
    parser.add_argument("-p", "--pages",  help="selected pages of the PDF",                       type=str)
    parser.add_argument("-o", "--out",      help="file name of the output PDF",                     type=str, default="reversed.pdf")
    args = parser.parse_args(sys.argv[2:])

    print(args)