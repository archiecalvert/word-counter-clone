import sys

COMMANDS = ["w", "c", "l", "m", "L"]

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
        raise Exception(f"File '{path}' does not exist.")


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

def handle_flags(arg):
    '''
    Function to handle flag arguments.

    Parameters:
        arg (str): the argument being evaluated (exluding beginning -)
    '''

    word_count = False
    line_count = False
    byte_count = False

    for char in arg:
        # handles malformed flag arguments
        if char not in COMMANDS:
            raise Exception(f"Flag {char} is not valid.")
        
        # checks to see what the command in the argument does
        match char:
            case "w":
                word_count = True
            case "l":
                line_count = True
            case "c":
                byte_count = True
            case "L":
                raise Exception("Longest line flag not supported.")
            case "m":
                raise Exception("Multi-byte character count flag not supported")
    
    return line_count, word_count, byte_count
                
        

def handle_output(args):
    """
    Responsible for handling the terminal input from the user.
    It handles flags and multiple files.

    Parameters:
        args (list[str]): list of parameters from the terminal.

    """
    
    # flag variables for commandline
    word_count = False
    line_count = False
    byte_count = False

    for i, arg in enumerate(args):

        # if the argument is a flag...
        if arg[0] == "-":
            line_count2, word_count2, byte_count2 = handle_flags(arg[1:])

            # applies or to each flag to update the new true ones
            line_count = line_count or line_count2
            word_count = word_count or word_count2
            byte_count = byte_count or byte_count2
                    
        # when the argument is a filename...
        else:

            filename = args[i]

            # if no flags have been passed
            if not(line_count or word_count or byte_count):
                word_count = True
                line_count = True
                byte_count = True

            print(
                    f"\t{str(get_line_count(filename)) + '\t' if line_count else ''}{str(read_word_count_from_file(filename)) + '\t' if word_count else ''}{str(read_byte_count_from_file(filename)) + '\t' if byte_count else ''}{filename}"
            )

            # reset flags as output has been provided
            word_count = False
            line_count = False
            byte_count = False

if __name__ == "__main__":
    arguments = get_sys_args()

    handle_output(arguments)
