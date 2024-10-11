from collections import defaultdict

from helpers.utils import merge_folder
import argparse


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('folder', type=str)
    argparser.add_argument('-c', '--clear', action='store_true')
    argparser.add_argument('--no-copy', action='store_true')
    args = argparser.parse_args()
    print(args)

    merge_folder(args.folder, '', **args)


if __name__ == '__main__':
    main()
