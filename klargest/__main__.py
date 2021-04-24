"""
Main file for providing module interface via input/output for getting keys
and values.
"""

import fileinput
import argparse

from .models import process_stream_to_get_keys
from .utils import get_num_key_from_line

parser = argparse.ArgumentParser(
    description='Process stream to get K Largest uids.')
parser.add_argument('k', metavar='K', type=int,
                    help='int for returning number of uids')
parser.add_argument('--input-file', dest='input_file', type=str, default="-",
                    help='optional file name to read stream (default: stdin)')
parser.add_argument('--output-file', dest='output_file', type=str, default="",
                    help='optional file output to write (default: stdout)')


if __name__ == "__main__":
    args = parser.parse_args()

    # Read stream to prepare k_largest
    with fileinput.input(args.input_file) as f:
        k_largest_keys = process_stream_to_get_keys(
            args.k, f, extractor=get_num_key_from_line)

    # Write to file or stdout
    if args.output_file:
        with open(args.output_file, 'w') as wd:
            print("\n".join(k_largest_keys), end="", file=wd)
    else:
        print("\n".join(k_largest_keys))
