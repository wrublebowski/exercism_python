def classify(number):

    if number <= 0:
        raise ValueError("greater than zero please")

    else:
        factors = find_factors(number)
        aliquot_sum = sum(factors)
        if aliquot_sum == number:
            return 'perfect'
        elif aliquot_sum < number:
            return 'deficient'
        elif aliquot_sum > number:
            return 'abundant'

def find_factors(number):
    factors = []
    for i in range (1,number):
        if number%i == 0:
            factors.append(i)
    return factors
