# Dictionaries and lists

# shopping_list = [
#     'apples',
#     'bananas',
#     'eggs',
# ]

# for item in shopping_list:
#     print(item)

# print(shopping_list[-1])


# shopping_list.append('soy milk')
# shopping_list[1] = 'spinach'

# # List of students where first item is first name
# # and second item is last name
# students = [
#     ['Hayley', 'van Waas'],
#     ['Cass', 'Gosby']
# ]

# # for student in students:
# #     print(student)

# print(students[1])
# print(students[1][0][0])



students = {
    # key: value
    4: 'Cass Gosby',
    5: 'Hayley van Waas'
}

# print(students[1])
# print(students[2])

# for key,student in students.items():
#     print(key, student)


students = {
    #key: value
    1: ['Cass', 'Gosby'],
    2: ['Hayley', 'van Waas']
}

# for key,student in students.items():
#     # print(key, student)
#     print('{key}: {first_name} {last_name}'.format(
#         key=key,
#         first_name=student[0],
#         last_name=student[1]
#     ))

students = {
    # key: value
    1: {
        'first_name': 'Hayley',
        'last_name': 'van Waas'
    },
    2: {
        'first_name': 'Angela',
        'last_name': 'Moroney'
    }
}
for key,student in students.items():
    print('{key}: {first_name} {last_name}'.format(
        key=key,
        first_name=student['first_name'],
        last_name=student['last_name']
    ))