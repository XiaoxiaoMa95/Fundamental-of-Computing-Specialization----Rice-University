"""
Merge function for 2048 game.
"""


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    non_zero = []
    is_zero = []
    # print(line)

    for item in line:
        if item == 0:
            is_zero.append(item)
        else:
            non_zero.append(item)
    # print(non_zero)
    # print(is_zero)

    new_line = list(non_zero + is_zero)

    for index in range(len(new_line)-1):
        if new_line[index] == new_line[index + 1] and new_line[index] != 0:
            new_line[index] += new_line[index + 1]
            new_line[index + 1] = 0
            new_line.append(new_line[index + 1])
            new_line.pop(index + 1)

    # print(new_line,'\n')
    return new_line


# merge([2, 0, 2, 4])
# merge([0, 0, 2, 2])
# merge([2, 2, 0, 0])
# merge([2, 2, 2, 2, 2])
# merge([8, 16, 16, 8])
