# Check if divisor is a factor of number
def check_divisible(number, divisor):
    return number % divisor == 0

# Convert a number to a string,
# the contents of which depend on the number's factors.


def convert(number):

    # Check to make sure the input is legal
    if not isinstance(number, int) and not isinstance(number, float):
        raise TypeError(
            'The number you provided to convert is not of type int or float.')

    output = ''

    # If the number has 3 as a factor, output 'Pling'.
    if check_divisible(number, 3):
        output = output + 'Pling'

    # If the number has 5 as a factor, output 'Plang'.
    if check_divisible(number, 5):
        output = output + 'Plang'

    # If the number has 7 as a factor, output 'Plong'.
    if check_divisible(number, 7):
        output = output + 'Plong'

    # If the number does not have 3, 5, or 7 as a factor,
    # just pass the number's digits straight through.
    if output == '':
        output = str(number)

    return output
