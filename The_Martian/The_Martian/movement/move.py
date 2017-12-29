from The_Martian import hex_alphabet

"""
This file should move the rover head to the hex-literals.
"""


def get_index_pair(x, y):
    x_ind = hex_alphabet.index(x)
    y_ind = hex_alphabet.index(y)
    return x_ind, y_ind


def get_possible_movement(ind_x, ind_y):
    return (ind_x - ind_y) % 16


def get_alternative_movement(ind_x, ind_y):
    return get_possible_movement(ind_y, ind_x)
