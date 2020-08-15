#!/usr/bin/python

# Date: 2020-08-15
#
# Description:
# Split string by space considering substrings enclosed between quotes as
# single string.
#
# Complexity:
# O(n)

def custom_split(log):
    """
    Splits string with space considering subsrtings enclosed between quotes as
    single string.
    """
    running_substring = False
    log = log.strip()
    i = -1
    splitted_string = []
    token = []
    while i < len(log) - 1:
        i += 1
        if log[i] in ('"', "'"):
            if running_substring:
                running_substring = False
                splitted_string.append(''.join(token))
                token = []
            else:
                running_substring = True
        elif log[i] == ' ':
            if running_substring:
                token.append(log[i])
            elif token:
                splitted_string.append(''.join(token))
                token = []
        else:
            token.append(log[i])
    if token:
        splitted_string.append(''.join(token))
    return splitted_string


assert custom_split(
    'This is a "python project"') == ['This', 'is', 'a', 'python project']
assert custom_split(
    'This is a python project') == ['This', 'is', 'a', 'python', 'project']
