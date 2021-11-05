mail = input("Enter mail:")
def checkMail(mail):
    if "@" in mail and "." in mail:
        return True
    else:
        return False

print(checkMail(mail))
