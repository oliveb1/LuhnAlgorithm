"""
 ------------------------------------------
|Luhn Algorithm by Brian Oliver, 07/15/19  |
 ------------------------------------------

The Luhn Algorithm is commonly used to verify credit card numbers, IMEI numbers, etc...

Luhn makes it possible to check numbers (credit card, SIRET, etc.) via a control key (called checksum, it is a number
of the number which makes it possible to check the others). If a character is incorrect, then Luhn's algorithm will
detect the error.

Starting with the right-most digit, double every other digit to the left of it. Then all of the undoubled and doubled
digits together. If the total is a multiple of 10, then the number passes the Luhn Algorithm.

For Luhn to be true:
    (double digits + undoubled digits) % 10 == 0
========================================================================================================================
"""

def luhn_algorithm_test(number):
    digit_list = list(map(int, str(number)))
    luhn_digits = []
    total = 0

    for digit in digit_list[-2::-2]:
        double_digit = digit * 2
        if double_digit >= 10:
            double_digit = double_digit - 9
        luhn_digits.append(double_digit)
        digit_list.remove(digit)

    total = sum(digit_list) + sum(luhn_digits)

    if total % 10 == 0:
        return "Luhn Algorithm Test Passed"
    else:
        return "Luhn Algorithm Test Failed"

def main():
    while True:
        try:
            number = int(input("Please enter a number: "))
            print(luhn_algorithm_test(number))
        except ValueError:
            print("Sorry, please input numbers only.")
            continue
        else:
            break

if __name__ == '__main__':
    main()