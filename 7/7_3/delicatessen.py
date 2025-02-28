sandwich_orders=['pastrami','tuna','pastrami','chicken','pastrami']
finished_sandwiches=[]
print("Sorry, we've run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
while sandwich_orders:
    current_sandwich=sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nI made the following sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)