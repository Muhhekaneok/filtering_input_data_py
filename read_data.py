def read_and_filter_files(file_paths: list[str]) -> tuple[list[int], list[float], list[str]]:
    integers = []
    floats = []
    strings = []

    for file_path in file_paths:
        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                print(f"File being processed: {file_path}")
                for line in file:
                    processed_line = line.strip()
                    if not processed_line:
                        continue

                    try:
                        integers.append(int(processed_line))
                    except ValueError:
                        try:
                            floats.append(float(processed_line))
                        except ValueError:
                            strings.append(line.rstrip("\n"))

        except FileNotFoundError:
            print(f"Error. File {file_path} not found. Skipping.")

    return integers, floats, strings


# print(read_and_filter_files(["input1.txt", "input2.txt"]))