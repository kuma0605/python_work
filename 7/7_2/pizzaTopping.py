prompt="what kind of pizza topping would you like?"
prompt+="\n(Enter 'quit' to end the program.)\n"

message = ""
# answer 1
# while True:
#     message = input(prompt)
#     if message == 'quit':
#         break
#     else:
#         print(f"Adding {message} to your pizza.")
# answer 2
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(f"Adding {message} to your pizza.")

# answer 3
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(f"Adding {message} to your pizza.")

