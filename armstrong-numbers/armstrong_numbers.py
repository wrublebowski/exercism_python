def is_armstrong_number(number):

    num_list = [int(x) for x in str(number)]
    armstrong = 0
    for i in num_list:
        armstrong += i**len(num_list)

    return number == armstrong 
