import os
import glob
import argparse
from typing import List, Tuple
from configurations import *


def main(args):
    val_size = args.val_size
    output_dir = args.output_dir

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output-dir', type=str, default='output',
                        help='Path to directory where files/directories will be generated')
    parser.add_argument('-v', '--val-size', type=float, default=0.1, help='Proportion of data that goes into the '
                                                                          'validation set')
    args = parser.parse_args()
    main(args)