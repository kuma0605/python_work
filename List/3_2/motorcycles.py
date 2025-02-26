motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles.append('ducati')
motorcycles.insert(0, 'ducati')
print(motorcycles)

""" del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# 删除任意位置的元素
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.") """

# 根据值删除元素
motorcycles.remove('ducati')
print(motorcycles)