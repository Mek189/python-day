score = int(input("Enter a test score"))

while score < 0 or score > 100:
    print('Enter:The score cannot be neagtive')
    print('or greater than 100.')
    score = int(input('Enter the correct score:'))