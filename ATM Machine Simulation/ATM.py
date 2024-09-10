import time
print("Please Insert Your Card")

time.sleep(5)

password = 1234

pin = int(input("Enter Your Pin"))

balance = 5000

if pin == password:
    while True:
        print("""
              1 == balance
              2 == withdraw amount
              3 == deposit balance
              4 == exit
              
              """)

        try:
            option = int(input("Please Enter Your Choice"))
        except:
            print("Please Enter Valid Option")

        if option == 1:
           print(f"Your Balance Is {balance}")
        if option == 2:
           withdraw_amount=int(input("please enter your withdraw_amount"))
           balance = balance-withdraw_amount
           print(f"{withdraw_amount} is debited from your account")

           print(f"your current balance is {balance}")

        if option == 3:
          deposit_amount = int(input("please enter your deposit_amount"))
          balance = balance+deposit_amount
          print(f"{deposit_amount} is credited to your account")
          print(f"your current balance is {balance}")

        if option == 4:
           break

else:
    print("Wrong Pin Please Try Again")
