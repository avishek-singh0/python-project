import random

# print(random.randint(1,100))
to_digit_number = input("Type  a number: ")
guess = 0
# print(type(to_digit_number))        
# to_digit_number in string so converted in int

if to_digit_number.isdigit():

     to_digit_number = int(to_digit_number)
     if to_digit_number <= 0:
         print('Please type a number larger then 0')  
         quit()     
    
else: 
     print("Please type a number next time") 
     quit()


random_num  = random.randint(1,to_digit_number)  

while True:
    
    guess += 1
    guess_number = input("guess the number :")
    
    
    if guess_number.isdigit():
     guess_number  = int(guess_number)
                
    else: 
     print("please try the  number next time again")
    
    if guess_number == random_num:
            print('you guess the number right')
            break
    
    else:
         if(guess_number > random_num):
             print("number is large")
         else:
             print("number is small") 
             

print("you got in click" , guess)     