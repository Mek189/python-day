inchar = input("Input on character:")
if inchar >= 'A' and inchar <= 'Z':
    print("You in put upper Case Letter" ,inchar)
elif inchar >= 'a' and inchar <= 'z':   
    print("You in put Lowver Case Letter" ,inchar)
elif inchar >= '0' and inchar <= '9':  
    print("You in put  Number" ,inchar)
else :
    print("It's not a letter or number." ,inchar)