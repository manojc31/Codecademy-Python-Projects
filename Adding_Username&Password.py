def username_generator(first_name, last_name):
    if (len(first_name) >= 3) and (len(last_name) >= 4):
        username = first_name[:3] + last_name[:4]
        return username
    else:
        username = first_name + last_name
        return username

def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i - 1]
    return password

print(username_generator("Abe", "Simpson"))
print(password_generator("AbeSimp"))

print(username_generator("Abe", "Simpson")) #Just to check
