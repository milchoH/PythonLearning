from operator import attrgetter

class User:

    def __init__(self, username, age):
        self.name = username
        self.age = age

    def __repr__(self):
        return self.name + "'s age = " + str(self.age)

users = [
    User('Milcho', 24),
    User('Gordon', 25),
    User('Ivan', 13),
    User('Liubo', 29),
    User('Koko', 45),
]

for user in users:
    print(user)
print('---------------------')
for user in sorted(users, key=attrgetter('name')):
    print (user)
print('---------------------')
for user in sorted(users, key=attrgetter('age')):
    print (user)
