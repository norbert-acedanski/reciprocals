def calculate_decimal_expansion(number: int, print_short_description: bool=True):
    if number < 2:
        raise ValueError("Enter number greater than 1!")
    decimal_expansion_list = []
    remainder_list = []
    current_remainder = 1
    # whole_division_product = 0
    period_index = -1
    while True:
        current_remainder *= 10
        whole_division_product = current_remainder // number
        current_remainder %= number
        if whole_division_product in decimal_expansion_list:
            indeces = [i for i, x in enumerate(decimal_expansion_list) if x == whole_division_product]
            for i in indeces:
                if remainder_list[i] == current_remainder and current_remainder != 0:
                    period_index = i
                    break
        if current_remainder == 0:
            period_index = -1
            break
        elif period_index >= 0:
            break
        decimal_expansion_list.append(whole_division_product)
        remainder_list.append(current_remainder)
    if current_remainder == 0:
        if print_short_description:
            print("Reciprocal of " + str(number) + " has no period.")
            print("1/" + str(number) + " = ", end="")
        print("0.", end="")
    else:
        if print_short_description:
            print("Number of digits in a period of decinal expansion of " + str(number) + ": " + str(len(decimal_expansion_list)))
            print("Decimal expansion of 1/" + str(number) + ": ", end="")
        print("0.", end="")
    for index, number in enumerate(decimal_expansion_list):
        if index == period_index:
            print("(", end="")
        print(number, end="")
    if current_remainder == 0:
        print(whole_division_product, end="")
    else:
        print(")", end="")
    print("")


if __name__ == "__main__":
    for i in range(2, 100):
        calculate_decimal_expansion(i, True)
    #Line of code below currently takes more than 400s to compute
    calculate_decimal_expansion(60017)