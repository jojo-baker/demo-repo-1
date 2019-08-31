# inheritance
# how to decide when to use a class

# Loops

# asking the user a question with two possible answers
# if answer is 'a', show section 1
# if answer is 'b' then do nothing

# ask multiple questions
# questions first, then sections


# user input
# store questions
# store the next sections to go to
# conditional for what section to show
# loop to iterate over the questions and sections


sections = {
    'DAYS OF THE WEEK': {
        'qualifying_question': 'What day is it today?',
        'show_section': False
    },
    'RAINBOWS': {
        'qualifying_question': 'What is Hayley\'s favourite colour?',
        'show_section': False
    },
    'JUMPERS': {
        'qualifying_question': 'What colour is Shae\'s jumper?',
        'show_section': False
    },
}

for section,information in sections.items():
    print(information['qualifying_question'])
    answer = input('what is the answer? ')

    if answer == 'a':
        information['show_section'] = True
    
    print()

for section,information in sections.items():
    if information['show_section']:
        print(section)
