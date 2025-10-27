import argparse
import os
import logging


def write_results(args: argparse.Namespace,
                  integers: list[int],
                  floats: list[float],
                  strings: list[str]) -> None:
    mode = "a" if args.append else "w"

    dir_path = args.output_path or "."
    os.makedirs(dir_path, exist_ok=True)

    def safe_write(filename: str, data: list, datatype: str) -> None:
        file_path = os.path.join(dir_path, f"{args.prefix}{filename}")
        if not data:
            return
        try:
            with open(file_path, mode, encoding="utf-8") as f:
                for item in data:
                    f.write(str(item) + "\n")
            logging.info(f"{datatype.capitalize()} successfully written to {file_path}")
        except PermissionError as e:
            logging.error(f"No permission to write file {file_path}: {e}")
        except IOError as e:
            logging.error(f"I/O error while writing file {file_path}: {e}")
        except Exception as e:
            logging.error(f"Unexpected error while writing file {file_path}: {e}")

    safe_write("integers.txt", integers, "integers")
    safe_write("floats.txt", floats, "floats")
    safe_write("strings.txt", strings, "strings")

# args = argparse.Namespace(
#     output_path="C:/Users/darkwizard/Desktop/",
#     prefix="sample-",
#     append=False,
#     short_stats=False,
#     full_stats=True,
#     input_files=["input1.txt", "input2.txt"]
# )
#
# print(write_results(args,
#                     [11, 2, 567],
#                     [3.14, 2.5, 9.99, 1.0],
#                     ["hello", "world"]))