import time
from motor import turn
from translator import translate_to_hex
from sequenzer import add_start_and_end_position, split_into_sequences
from move import get_index_pair, get_possible_movement,\
				 get_alternative_movement


def turn_head(turns, direction):
	print("Turn {0} {1}".format(turns, direction))
	for i in range(0, turns):
		turn(direction)
	time.sleep(0.5)

def move_rover_head(text):
	hex_string = translate_to_hex(text)
	hex_string = add_start_and_end_position(hex_string)
	precursor, successor = split_into_sequences(hex_string)
	for x, y in zip(precursor, successor):
		x_ind, y_ind = get_index_pair(x, y)
		possible = get_possible_movement(x_ind, y_ind)
		alternative = get_alternative_movement(x_ind, y_ind)
		if alternative < possible:
			turns = abs(alternative)
			turn_head(turns, "right")
		else:
			turns = abs(possible)
			turn_head(turns, "left")
				
	print(precursor, successor)

if __name__ == "__main__":
	move_rover_head("Status")
