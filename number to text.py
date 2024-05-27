def number_to_words(number):
    one_digit_words = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
        '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }

    two_digit_words = {
        '10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen',
        '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen',
        '20': 'Twenty', '30': 'Thirty', '40': 'Forty', '50': 'Fifty',
        '60': 'Sixty', '70': 'Seventy', '80': 'Eighty', '90': 'Ninety'
    }

    if 0 <= number < 10:
        return one_digit_words[str(number)]
    elif 10 <= number < 100:
        if number in two_digit_words:
            return two_digit_words[str(number)]
        else:
            return two_digit_words[str(number // 10 * 10)] + ' ' + one_digit_words[str(number % 10)]
    elif 100 <= number < 1000:
        hundreds = one_digit_words[str(number // 100)] + ' Hundred'
        remainder = number % 100
        if remainder == 0:
            return hundreds
        else:
            return hundreds + ' and ' + number_to_words(remainder)
    elif 1000 <= number <= 9999:
        thousands = number_to_words(number // 1000) + ' Thousand'
        remainder = number % 1000
        if remainder == 0:
            return thousands
        else:
            return thousands + ' ' + number_to_words(remainder)
    else:
        return "Number out of range (0-9999)"

# Example usa
number = int(input("Enter a number (0-9999): "))
result = number_to_words(number)
print(f"{number} in words: {result}")
