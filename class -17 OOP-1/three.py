class Account:
    '''create by mani'''
    def open_account(self):
        print("Account opened Successfully")
    def deposit_amonut(self):
        print("Amonut Depsited")  
    def withdrawl(self):
        print("Amonut withdrawl")   
    
a1=Account()
a2=Account()

#printing object in the form of dict
print(a1.__dict__)
print(a2.__dict__)
print(Account.__dict__)