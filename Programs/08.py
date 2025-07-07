passwd = input("Enter Your Password => ")
pswdSize = 0
numChar = 0
uCase = 0
lCase = 0
specialChar = 0
pswdValid = True
for char in passwd :
    pswdSize += 1
    if (char.islower()) :
        lCase += 1
    elif (char.isupper()) :
        uCase += 1
    elif (char.isdigit()) :
        numChar += 1
    else :
        specialChar += 1
print("Errors => ")
if (pswdSize < 8) :
    pswdValid = False
    print("Password Length less than 8 Characters")
if (numChar == 0) :
    pswdValid = False
    print("Password doesn't contain Digits")
if (uCase == 0) :
    pswdValid = False
    print("Password doesn't contain Upper Case Letters")
if (lCase == 0) :
    pswdValid = False
    print("Password doesn't contain Lower Case Letters")
if (specialChar == 0) :
    pswdValid = False
    print("Password doesn't contain Special Characters")
if (pswdValid) :
    print("None")
    print("Result => Password Valid")
else :
    print("Result => Password Invalid")