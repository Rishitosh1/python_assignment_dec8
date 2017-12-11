def password_read():
    pwd = input("Enter the password: ")
    return(pwd)


def password_check(pwd):
    if(pwd == password):
        print("Welcome the password is correct.")
    else:
        print("Password is incorrect.")


password = 'singham'

pwd= password_read()
password_check(pwd)
