def avg(*list_numbers:float) -> float:
    total = 0
    for num in list_numbers:
        if isinstance(num, (int, float)):
            total += num
        else:
            raise TypeError("Wrong input data")

    return total / len(list_numbers)