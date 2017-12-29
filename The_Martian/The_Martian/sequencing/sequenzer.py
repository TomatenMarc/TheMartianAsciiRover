"""
This file should split a hex-string into to list.
"""


# since the head of the rover start and ends at 0
# add a 0 at the start and end.
# the literals are positions.
def add_start_and_end_position(hex_string):
    return "0" + hex_string + "0"


# split the string into its precursor and successor
def split_into_sequences(hex_string):
    precursor = hex_string[:-1]
    successor = hex_string[1:]
    return precursor, successor
