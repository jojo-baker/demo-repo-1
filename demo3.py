# 1 - 3: dogs
# AND if 2: dogs dogs
# 4- 6: cats
# 7 - 9: zebras
# 10: elephants
# 14: meerkats
# 17: monkeys
# else: NOTHING

def dogs_message(message):
    return '{} {}'.format(message, message)


def message(number):
    if number >= 1 and number <= 3:
        message = 'dogs'
        if number == 2:
            message = dogs_message(message)
        return message
    
    if number >= 4 and number <= 6:
        return 'cats'
    
    if number >= 7 and number <= 9:
        return 'zebras'
    
    if number == 10:
        return 'elephants'
    
    if number == 14:
        return 'meerkats'
    
    if number == 17:
        return 'monkeys'
    
    return 'NOTHING'


print(message(2))
# print(message(1))
# print(message(3))
# print(message(5))
# print(message(7))
# print(message(10))
# print(message(14))
# print(message(17))
# print(message(13))