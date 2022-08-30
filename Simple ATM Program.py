import time

print("Please insert Your CARD")

time.sleep(2)

password = 1268

pin = int(input("enter your atm pin "))

balance = 12400

if pin == password:
            while True:
                    print(""" 
                        1 -- Balance Inquiry
                        2 -- Withdrawal
                        3 -- Deposit
                        4 -- exit
                        """
                        )

                    try:    
                        option = int(input("Please enter your choise "))
                
                        if option == 1:
                            print(f"Your current balance is {balance}")
                                                    
                        if option == 2:

                            withdraw_amount = int(input("please enter withdraw_amount "))  

                            balance = balance - withdraw_amount

                            print(f"{withdraw_amount} is debited from your account")

                            print(f"your updated balance is {balance}")


                        if option == 3:

                            deposit_amount = int(input("please enter deposit_amount"))

                            balance = balance + deposit_amount

                            print(f"{deposit_amount} is credited to your account")

                            print(f"your updated balance is {balance}")

                        if option == 4:

                            break
                    except:
                        print("Please enter valid option")    
else:
    print("Please enter valid pin") 

            
  


