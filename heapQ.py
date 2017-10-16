import heapq

grades = [32,43,12,3254,345,324,65,76,234,564]
print(heapq.nlargest(3,grades))

customData = [
    {'boxingGloves': 'Everlast', 'price': 70},
    {'boxingGloves': 'Lonsdale', 'price': 65},
    {'boxingGloves': 'BadBoy', 'price': 150},
    {'boxingGloves': 'Adidas', 'price': 300},
    {'boxingGloves': 'Nike', 'price': 200},
]

print (heapq.nlargest(2, customData, key=lambda customData: customData['price']))