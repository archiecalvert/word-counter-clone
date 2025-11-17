import sys


def get_sys_args() -> list[str]:
    """
    Gets a list of all of the arguments passed in on the terminal by the user.

    Returns:
        list[str]: A list of all the arguments passed in by the user.

    Throws:
        Exception: No arguments passed.
    """
    arguments = sys.argv

    argument_count = len(arguments) - 1

    if argument_count == 0:
        raise Exception("No arguments passed.")

    return arguments[1:]


def read_file_data(path) -> list[bytes]:
    """
    Reads the raw byte data from the secified path.

    Parameters:
        path (str): the filepath where the data will be read from.

    Returns:
        list[byte]: an array of byte data from the file.

    Throws:
        FileNotFoundError: if the specified file cannot be found.

    """
    try:
        with open(path, "rb") as f:
            data = f.read()
            return data

    except FileNotFoundError:
        raise Exception("File does not exist.")


def read_byte_count_from_file(path) -> int:
    """
    Gets the number of bytes inside of a file.

    Parameters:
        path (str): the filepath for the data.

    Returns:
        int: the number of bytes in the specified file.
    """
    return len(read_file_data(path))


def read_word_count_from_file(path) -> int:
    """
    Gets the number of words inside of a file.
    A word is any length of characters which are non-whitespace characters.
    A contiguous string of whitespace characters will not count towards the character count.

    Parameters:
        path (str): the filepath for the data.

    Returns:
        int: the number of words in a file.
    """
    data = read_file_data(path)

    word_count = 0
    is_word = False

    for char in data:
        # if the current character is whitespace (these are the byte equivalents)
        if char in (9, 10, 11, 12, 13, 32):
            is_word = False
        else:
            if not is_word:
                word_count += 1
                is_word = True

    return word_count


def get_line_count(path) -> int:
    """
    Gets the number of lines inside of a file, achieved through counting the number of newline characters.

    Parameters:
        path (str): the filepath for the data.

    Returns:
        int: the number of lines.
    """
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
