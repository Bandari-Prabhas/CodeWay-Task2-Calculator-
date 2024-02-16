# Taking inputs from the user to perform mathematical calculations


a=int(input("Enter the first Number:")) # taking first input number from the user and assign it to a variable a
b=int(input("Enter the second Number:")) # taking second input number from the user and assign it to a variable b  


op=input("Enter any opertor(+,-,*,/,%) you want:")
# taking the input operation from the user and assign it to a variable op

# Using the match case like switch case in other languages
match op:
     case '+':
          c=a+b #performing the addition operation and store it in a variable c
          print("The Addition of ",a," and ",b," is =",c) #printing the input 
     case '-':
          c=a-b  #performing the subtraction operation and store it in a variable c
          print("The Subtraction of ",a," and",b," is =",c)
     case '*':
          c=a*b  #performing the multiplication operation and store it in a variable c
          print("The Multiplication of ",a," and",b," is =",c)
     case '/':
          c=a/b  #performing the division operation and store it in a variable c
          print("The Division of ",a," and",b," is =",c)
     case '%':
          c=a%b  #performing the Modulus operation and store it in a variable c
          print("The Modulus of ",a," and",b," is =",c)
     case _:
          print("Wrong option Please Enter CORRECT operator...")