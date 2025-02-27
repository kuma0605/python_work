current_users=['admin','dylan','james','john','michael']
current_users_lower=[]
for user in current_users:
    current_users_lower.append(user.lower())
new_users=['dylan','james','john','joseph','michael']
for user in new_users:
    if user.lower() in current_users:
        print(f'Hello {user}, you need to enter a new username')
    else:
        print('Hello '+user+', we are glad to have you here')

    