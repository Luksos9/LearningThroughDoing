"""Here’s what the program does:

1.It searches all the filenames in the current working directory for American-style dates: MM-DD-YYYY
2.When one is found, it renames the file with the month and day swapped to make it European-style: DD-MM-YYYY"""

import shutil, os, re

#Create a regex that matches files with the American date format
datePattern = re.compile(r"""^(.*?) #all text before date
((0|1)?\d)-                         #one or two digits for the month
((0|1|2|3)?\d)-                     #one or two digits for the day
((19|20)\d\d)                       #four digits for the year
(.*?)$                              #all text after the date
""", re.VERBOSE)

# TODO: Loop over the files in the working directory.

# TODO: Skip files without a date.

# TODO: Get the different parts of the filename.

# TODO: Form the European-style filename.

# TODO: Get the full, absolute file paths.

# TODO: Rename the files.
