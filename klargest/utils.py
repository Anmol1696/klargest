"""
Utils for klargest package
"""

def get_num_key_from_line(line: str):
    """
    Given a line str, of form f"{key} {num}\n"
    Return int num and key
    """
    key, num = line.split("\n")[0].split(" ")
    return int(num), key
