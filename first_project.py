def avg(*list_numbers):
    total = 0
    for num in list_numbers:
        total += num

    return total / len(list_numbers)