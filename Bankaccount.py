#( **Scenario-Based Question:**
Kalyan recently opened a bank account with an initial balance of ₹25,000. He decides to deposit ₹30,000 into his account and later withdraw ₹5,000 for his monthly expenses.

#### **Question:**  
1. What will be the updated balance after Kalyan deposits ₹30,000?  
2. What will be the remaining balance after he withdraws ₹5,000?  
3. Suppose Kalyan attempts to withdraw ₹60,000 instead. What will happen, and why?  
4. Why is the `__balance` attribute declared as private in the class? How can Kalyan check his current balance safely?  

**Bonus:**  
If we try to access `A1.__balance` directly from outside the class, what will happen, and how can we still retrieve the balance?)


Code:

class bankaccount:
    def __init__(self,acholder,balance):
        self.acholder=acholder
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print(f"Deposited amount ={amount} and Total balance={self.__balance}")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"The withdraw amount={amount} and Remaining blance={self.__balance}")
        else:
            print("Insufficient funds")
A1=bankaccount("Kalyan",25000)
A1.deposit(30000)
A1.withdraw(5000)