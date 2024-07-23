#Data Types

#String
#Subscripting
print("Hello"[0])

#shows that if numbers are written within quotes than the computer will read a string and concatenate both strings into one
print("123"+"345")

#Integer- whole numbers pos or negative

#likewise if we remove the quotes and try to print the same function we get the result of the sum between both numbers
print(123+345)

#in order to be able to visualize better a large integer we can use underscores. These will be ignrored by the program when the code runs.
print(123_456_789)

#Float - or floating point number is a number with decimal places

print(3.14159)

#Bolean - can only have 2 possible types, needs to start with capital letter.

True
False

#Quiz example, the space in Abbey Road counts as an integer
street_name="Abbey Road"
print(street_name[5])
print(street_name[0])


#Data type checking and conversion

#num_char=len(input("What is your name?\n"))
#print(type(num_char))
#new_num_char=str(num_char)
#if I were to print the below without changing the data type to String from Int then we would get a data type error.
#print("Your name has "+new_num_char+" characters")

#Mathematical Operations in Python and priority (PEMDAS)
() #parenthesis
"**" #exponent
"* /" #multiplication and division, the calculation most to the left will be prioritised
"+ -" #sum and substraction
print(3*3+3/3-3) #will lead to 7
print(3*(3+3)/3-3) #will lead to 3 by changing the priority

result=4/2
# if I want to divide by 2 again then
#result/=2 --> 2/2=1
#print(result)
#result+=2 --> 2+2=4
#print(result)
#result-=2 --> 2-2=0
#print(result)


#F-strings

score=0
height=1.8
iswinning=True

print("your score is "+str(score))

print(f"your score is {score}, your height is {height}")

