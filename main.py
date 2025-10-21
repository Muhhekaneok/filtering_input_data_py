import argparse


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

    print("--- Result of parsing ---")
    print(f"Path for output (-o): {args.output_path}")
    print(f"Prefix (-p): {args.prefix}")
    print(f"Append (-a): {args.append}")
    print(f"Short stats (-s): {args.short_stats}")
    print(f"Full stats (-f): {args.full_stats}")
    print(f"Input files (+): {args.input_files}")
