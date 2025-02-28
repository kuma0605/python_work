prompt = "what is your age?"
prompt += "\n(Enter 'quit' to end the program.)\n"

while True:
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
