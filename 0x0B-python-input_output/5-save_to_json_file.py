
#!/usr/bin/python3
"""
A module containing a function to save an object to a text file using JSON representation.
"""


import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Parameters:
    - my_obj: The object to be saved.
    - filename: The name of the text file to save to.

    Returns:
    - None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
