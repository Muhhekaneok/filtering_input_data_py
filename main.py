import sys
import argparse
import logging
from read_data import read_and_filter_files
from write_filtered_data import write_results
from stats import print_statistics


def parse_arguments():
    parser = argparse.ArgumentParser(description='Utility for filter input data by data type')
    parser.add_argument("-o", "--output",
                        dest="output_path",
                        default="",
                        help="path to save output file")

    parser.add_argument("-p", "--prefix",
                        default="",
                        help="prefix of output file")

    parser.add_argument("-a", "--append",
                        action="store_true",
                        help="append data")

    parser.add_argument("-s", "--short-stats",
                        action="store_true",
                        help="show short statistics")

    parser.add_argument("-f", "--full-stats",
                        action="store_true",
                        help="show full statistics")

    parser.add_argument("input_files",
                        nargs="+",
                        help="One or more input files for processing")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    try:
        integers_data, floats_data, strings_data = read_and_filter_files(
            file_paths=args.input_files)

        if not any([integers_data, floats_data, strings_data]):
            logging.warning("No input files found or files contain invalid data")
            sys.exit(1)

        write_results(args, integers_data, floats_data, strings_data)
        logging.info("All input files have been processed")
        sys.exit(0)

    except Exception as e:
        logging.error(f"Unexpected error {e}")
        sys.exit(1)