import sys


def get_sys_args():
    arguments = sys.argv

    argument_count = len(arguments) - 1

    if argument_count == 0:
        raise Exception("No arguments passed.")

    return arguments[1:]


def read_file_data(path):
    try:
        with open(path, "r") as f:
            lines = f.readlines()
            return lines

    except FileNotFoundError:
        raise Exception("File does not exist.")


def read_byte_count_from_file(path):
    with open(path, "rb") as f:
        return len(f.read())


def read_word_count_from_lines(lines):
    word_count = 0
    for line in lines:
        formatted_line = " ".join(line.split())
        words = formatted_line.split(" ")
        while "" in words:
            words.remove("")
        word_count += len(words)

    return word_count


def get_line_count(lines):
    return len(lines) - (1 if lines[-1][-1] != "\n" else 0)


if __name__ == "__main__":
    arguments = get_sys_args()

    filename = arguments[0]

    data = read_file_data(filename)

    line_count = get_line_count(data)

    word_count = read_word_count_from_lines(data)

    byte_count = read_byte_count_from_file(filename)

    print(f"\t{line_count}\t{word_count}\t{byte_count} {filename}")
