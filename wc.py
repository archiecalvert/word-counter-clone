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
            print(lines)

    except FileNotFoundError:
        raise Exception("File does not exist.")


def read_char_count_from_lines(lines):
    pass


if __name__ == "__main__":
    arguments = get_sys_args()

    filename = arguments[0]

    data = read_file_data(filename)

    line_count = len(data)
