from collections import defaultdict
import logging

from helpers.utils import merge_folder
import argparse


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('folder', type=str)
    argparser.add_argument('-c', '--clear', action='store_true')
    argparser.add_argument('--no-copy', action='store_true')
    argparser.add_argument('--verbose', '-v', action='count', default=0)
    args = argparser.parse_args()

    if args.verbose == 0:
        logging.root.setLevel(logging.WARN)
    elif args.verbose == 1:
        logging.root.setLevel(logging.INFO)
    elif args.verbose > 1:
        logging.root.setLevel(logging.DEBUG)

    print(args)

    merge_folder(args.folder, '', clear=args.clear, no_copy=args.no_copy)


if __name__ == '__main__':
    main()
