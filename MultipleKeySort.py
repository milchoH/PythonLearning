from operator import itemgetter

users = [
    {'fname': 'someName', 'lname': 'noIdea'},
    {'fname': 'No', 'lname': 'Just'},
    {'fname': 'Creativity', 'lname': 'Follow'},
    {'fname': 'Can', 'lname': 'The'},
    {'fname': 'Be', 'lname': 'Keys'},
    {'fname': 'Found', 'lname': 'And'},
    {'fname': 'Currently', 'lname': 'You'},
    {'fname': 'Here', 'lname': 'Will'},
    {'fname': 'Now', 'lname': 'Understand'},
]

for i in sorted(users, key=itemgetter('fname', 'lname')):
    print(i)