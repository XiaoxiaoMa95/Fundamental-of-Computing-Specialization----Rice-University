"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    transfer_lst = [0] * len(line)
    result_line = [0] * len(line)

    print(line)

    loc = 0
    for item in line:
        if item != 0:
            transfer_lst[loc] = item
            loc += 1

    print(transfer_lst)

    for dummy_i in range(len(transfer_lst ) - 1):
        if transfer_lst [dummy_i] == transfer_lst [dummy_i + 1]:
            transfer_lst [dummy_i] = transfer_lst [dummy_i] + transfer_lst [dummy_i + 1]
            transfer_lst [dummy_i + 1] = 0
            dummy_i += 1

    print(transfer_lst)

    loc = 0
    reverse_loc = -1
    while loc - reverse_loc <= len(line):
        for dummy_item in transfer_lst :
            if dummy_item != 0:
                result_line[loc] = dummy_item
                loc += 1
            else:
                result_line[reverse_loc] = 0
                reverse_loc -= 1

    print(result_line,'\n')

    return result_line


merge([2,0,2,4])
merge([0,0,2,2])
merge([2,2,0,0])
merge([2,2,2,2,2])
merge([8,16,16,8])