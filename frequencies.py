"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        strItem = str(item)
        if strItem in frequencies:
            frequencies.update({strItem: (frequencies.get(strItem)+1)})
        else:
            frequencies.update({strItem: 1})
    return frequencies
