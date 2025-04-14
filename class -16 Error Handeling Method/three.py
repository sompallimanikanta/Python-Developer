from insuffientBalError import InsuffientBalErr as LowBalanceError

acc_Bal=15000
try:
    amount = int(input("Enter Amonut:"))
    if acc_Bal < amount:
        raise LowBalanceError("Buddy - Low Bal! Please Check!")
    else:
        print("Please withdrawl and Enjoy!")
except LowBalanceError as err:
    print(err)
except:
    print("Check the Code! Default Errors")
    
print("Good Morning")



















'''#with Error Handling

acc_Bal =15000
amount = int(input("Enter Amount:"))
try:
    if acc_Bal < amount:
        raise InsuffientBalError("Low Balance")
    else:
        '''