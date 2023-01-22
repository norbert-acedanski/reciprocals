from typing import Dict


def calculate_decimal_expansion(number: int) -> Dict[str, str]:
    if number < 2:
        raise ValueError("Enter number greater than 1!")
    expansion = {"non-periodic expansion": None, "periodic expansion": ""}
    multiplied_reminder = 1
    decimal_expansion_list = []
    reminders_list = []
    while True:
        multiplied_reminder *= 10
        whole_division_product = multiplied_reminder // number
        reminder = multiplied_reminder % number
        if reminder == 0:
            decimal_expansion_list.append(str(whole_division_product))
            period_index = -1
            break
        if (next_term := (multiplied_reminder, reminder)) in reminders_list:
            period_index = reminders_list.index(next_term)
            break
        decimal_expansion_list.append(str(whole_division_product))
        reminders_list.append(next_term)
        multiplied_reminder = reminder
    if period_index == -1:
        expansion["non-periodic expansion"] = "".join(decimal_expansion_list)
    else:
        expansion["non-periodic expansion"] = "".join(decimal_expansion_list[:period_index])
        expansion["periodic expansion"] = "".join(decimal_expansion_list[period_index:])
    return expansion


if __name__ == "__main__":
    for num in range(2, 100):
        number_expansion = calculate_decimal_expansion(number=num)
        print(f"Number 1/{num} decimal expansion: ", end="")
        print(f"0.{number_expansion['non-periodic expansion']}", end="")
        period = number_expansion['periodic expansion']
        print(f"({period})") if period else print("")
    # Line of code below currently takes roughly 50s to compute
    calculate_decimal_expansion(60017)
