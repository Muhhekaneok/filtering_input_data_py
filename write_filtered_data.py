import argparse
import os


def write_results(args: argparse.Namespace,
                  integers: list[int],
                  floats: list[float],
                  strings: list[str]) -> None:
    mode = "a" if args.append else "w"

    if args.output_path:
        os.makedirs(args.output_path, exist_ok=True)

    if integers:
        file_path = os.path.join(args.output_path, f"{args.prefix}integers.txt")
        try:
            with open(file_path, mode, encoding="utf-8") as f:
                for item in integers:
                    f.write(str(item) + "\n")
                print(f"Integers successfully written to {file_path}")
        except IOError as e:
            print(f"Error. Could not write to {file_path}: {e}")

    if floats:
        file_path = os.path.join(args.output_path, f"{args.prefix}floats.txt")
        try:
            with open(file_path, mode, encoding="utf-8") as f:
                for item in floats:
                    f.write(str(item) + "\n")
                print(f"Floats successfully written to {file_path}")
        except IOError as e:
            print(f"Error. Could not write to {file_path}: {e}")

    if strings:
        file_path = os.path.join(args.output_path, f"{args.prefix}strings.txt")
        try:
            with open(file_path, mode, encoding="utf-8") as f:
                for item in strings:
                    f.write(item + "\n")
                print(f"Strings successfully written to {file_path}")
        except IOError as e:
            print(f"Error. Could not write to {file_path}: {e}")


args = argparse.Namespace(
    output_path="C:/Users/darkwizard/Desktop/",
    prefix="sample-",
    append=False,
    short_stats=False,
    full_stats=True,
    input_files=["input1.txt", "input2.txt"]
)

print(write_results(args,
                    [11, 2, 567],
                    [3.14, 2.5, 9.99, 1.0],
                    ["hello", "world"]))