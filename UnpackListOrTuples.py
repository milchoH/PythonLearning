date, name, age = ['7 november', 'milcho', 25]
print(name)

def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) /len(middle)
    print(avg)

drop_first_last([65,76,98,54,21])
drop_first_last([65,76,98,54,21,33,45,67,89,43,56,45,65,55])