from collections import defaultdict

from helpers.utils import merge_folder
import argparse


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('folder', type=str)
    args = argparser.parse_args()
    merge_folder(args.folder, '')


if __name__ == '__main__':
    main()
