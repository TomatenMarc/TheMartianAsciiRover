"""
This file has the task to convert a text to its hex-values.
"""

# translate_to_hex should transform the text to its hex-values.
def translate_to_hex(text):
    hex_string = "".join([hex(ord(char)) for char in text])
    return hex_string.replace("0x", "")
