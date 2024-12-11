from cryptography.fernet import Fernet

master_pwd = input("What is master your  password ")

def view():
 with open('passwrod.txt','r') as f:
  for line in f.readlines():
         
         [user,passw] = line.split("|") 
         print('name :',user,"password :",passw )

def add():
   name = input('What is ACCount name ')
   pwd = input('What is your password ')

   with open('passwrod.txt','a') as f:
      f.write(name + "|" + pwd + '\n')
      



while True:
   mode = input("What You want to do View/add/Quit for q ").lower()

   if mode == 'q':
     break
   elif mode == 'view':
     view()
   elif mode == 'add':
     add()
   else:
     print("Not a valid options")
     continue



     
 
