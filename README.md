# Week 1 Content - Creating a mini wc
We needed to implement a mini wc (word counter) clone using python, with the following speficiation:

1. There are no flag options.
2. The output is linecount ```wordcount bytecount filepath``` (each separated by tab characters)
3. There is exactly one filepath passed as an argument.
4. That path argument is not stdin (i.e., “-”)
5. It should handle errors as wc for things inside the spec. I.e., if wc would give an error for a one argument invocation, you should give the same error.

This means that commands are restricted to '''wc \<some file name which isn't '-'\>'''.

We also need the following constraints:
1. You cannot use any other imported library, including built in modules. The only exception is '''sys'''.
2. Your program needs to be executed by '''python wc.py <filepath>''' on the command line.

# Week 2 Content - Building out wc
For this week, we needed to implement:

1. Flag support into the command line, specifically '''l, w, c, m, L'''.
2. Multiple file support in the arguments.

For the flags, they are as follows:
- l: line count.
- w: word count.
- c: byte count.
- m: 'correct' character count, as some characters take more than one byte.
- L: length of longest line.

This weeks coursework also mentioned adding in alternative flags, specifically '''--lines''', '''--files0-from''', and '''--libxo'''. These haven't been implemented

# Week 3 Content - Fleshing out
This week essentially was fleshing out and polishing the feature set of the wc, and also creating a test suite.

# Week 4 Content - Checking
This week, we should have:

- “Mini”-wc…no flags, only all -wlc counting, single file input; the simplest version that does anything.
- “Simple”-wc…-wlcL option handling, multi-file input; an easy version of POSIX compatibility.
- POSIX -wlcmL option handling, multi-file input; -m handling is tricky to get completely correct.
- BSD functionality
- GNU coretools functionality
- The union of all these with some configuration options to enable any specific variant.

We also should create a table of claims about our system, considering:
- Line coverage
- Testability
- Features (flag handling, counts, and other)
