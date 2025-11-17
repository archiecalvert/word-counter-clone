import sys


def get_sys_args():
    arguments = sys.argv

    argument_count = len(arguments) - 1

    if argument_count == 0:
        raise Exception("No arguments passed.")

    return arguments[1:]


def read_file_data(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
            return data

    except FileNotFoundError:
        raise Exception("File does not exist.")


def read_byte_count_from_file(path):
    return len(read_file_data(path))


def read_word_count_from_file(path):
    data = read_file_data(path)

    word_count = 0
    is_word = False

    for b in data:
        if b in (9, 10, 11, 12, 13, 32):
            is_word = False
        else:
            if not is_word:
                word_count += 1
                is_word = True

    return word_count


def get_line_count(path):
    data = read_file_data(path)

    return data.count(ord("\n"))


if __name__ == "__main__":
    arguments = get_sys_args()

    filename = arguments[0]

    data = read_file_data(filename)

    line_count = get_line_count(filename)

    word_count = read_word_count_from_file(filename)

    byte_count = read_byte_count_from_file(filename)

    print(f"\t{line_count}\t{word_count}\t{byte_count} {filename}")
