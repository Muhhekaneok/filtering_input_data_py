import argparse


def print_statistics(args: argparse.Namespace,
                     integers: list[int],
                     floats: list[float],
                     strings: list[str]) -> None:
    if args.short_stats:
        print("\nShort statistics:")
        if integers:
            print(f"\tIntegers written: {len(integers)}")
        if floats:
            print(f"\tFloats written: {len(floats)}")
        if strings:
            print(f"\tStrings written: {len(strings)}")

    if args.full_stats:
        print("\nFull statistics:")
        if integers:
            print(f"---Integers written: {len(integers)} qty---")
            print(f"   min: {min(integers)}")
            print(f"   max: {max(integers)}")
            print(f"   sum: {sum(integers)}")
            print(f"   avg: {sum(integers) / len(integers):.2f}")

        if floats:
            print(f"---Floats written: {len(floats)} qty---")
            print(f"   min: {min(floats)}")
            print(f"   max: {max(floats)}")
            print(f"   sum: {sum(floats)}")
            print(f"   avg: {sum(floats) / len(floats):.2f}")

        if strings:
            print(f"---Strings written: {len(strings)} qty---")
            min_length = len(min(strings, key=len))
            max_length = len(max(strings, key=len))
            print(f"   shortest line: {min_length}")
            print(f"   longest line: {max_length}")


args = argparse.Namespace(
    output_path=f"C/users/darkwizard/desktop/",
    prefix="results-",
    append=False,
    short_stats=False,
    full_stats=True,
    input_files=["input1.txt", "input2.txt"]
)

print_statistics(args=args,
                 integers=[23, -1, 101, 0],
                 floats=[5.0, 77.77],
                 strings=["hello", "digital", "world", "!"])