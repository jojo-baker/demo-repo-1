# types

def multiply(a, b):
    return a * b

# a = input('number a: ')
# b = input('number b: ')

# take an integer, and only a integer

# accept input
# if it is an integer, move on
# if not an integer, give the user another chance



def validate_input(num_digit):
    user_input = input('number ' + num_digit + ':' )
    try:
        user_input = int(user_input)
        return user_input
    except:
        print('sorry that was not an integer')
        validate_input(num_digit)


a = validate_input('a')
b = validate_input('b')


print(a * b)


def function_name(): # parameters # arguments
    pass

