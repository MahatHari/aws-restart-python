#working with the if statement

userReply= input ("Do you need to ship a packange ? (Enter yes or no ): ")

if userReply=='yes':
    print("We can help you ship the package")

#working with elif

userReply2= input("would you like to buy stamps, buy an envelope or make a copy ? (Enter stamps, envelope, or copy) :  ")
if userReply2=='stamps':
    print('We have many stams design to choose form')
elif userReply2=='envelope':
    print('We have many envelope sizes to choose from')
elif userReply2=='copy':
    copies=input('How many copies would you like? (Enter a number) : ')
    print('Here are {} copies'.format(copies))
else:
    print('Thank you, Please come again')