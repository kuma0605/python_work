cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# cars.sort(reverse=True)
# print(cars)

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# 在调用 sorted() 函数后，列表元素的排列顺序并没有变。
# 如果要按与字母顺序相反的顺序显示列表，也可向 sorted() 函数传递参数 reverse=True。
print('sorted reverse')
print(sorted(cars, reverse=True))