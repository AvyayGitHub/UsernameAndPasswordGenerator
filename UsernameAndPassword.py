# Use This Code To Create A Username And Password Login Sheet

ask = input("Do You Want To Create A Login Sheet. ")
if ask == 'yes' and 'YES' and 'Yes':
    print("Let's Get Started!")
elif ask == 'no' and 'NO' and 'No':
    print("Maybe Later.")
else:
    print("That Was Not Recognizeable. Try Again Please.")
    ask1 = input("Do You Want To Create A Login Sheet. ")
    if ask1 == 'yes' and 'YES' and 'Yes':
        print("Let's Get Started!")
    elif ask1 == 'no' and 'NO' and 'No':
        print("Maybe Later.")

def username():
    username = input("What Is Your Username? DON'T Use Your Name!!! ")
    print("Your Username Is", username)

username()

def password():
    password = input("What Is Your Password? Make It 8 Characters With One Number And One Capital Letter. ")
    print("Your Password Is", password)

password()

print("Thanks For Using Login Sheet. Bye")
