print("==========================")
print("     Expense Tracker      ")
print("==========================")

class Expense:
    def __init__ (self, First_name, Last_name, Profession, Account_number, Balance):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Profession = Profession
        self.Account_number = Account_number
        self.Balance = Balance

    def Details(self):
        print("Name = " + str(self.First_name) + " " + str(Last_name))
        print("Profession = " + str(self.Profession))
        print("Account Number = " + str(self.Account_number))
        print("Balance = " + str(self.Balance))
    
    def Deposit(self):
        A = int(input("Do you wish to Deposite Money (1 = Yes and 2 = No) : "))
        if A == 1:
            money_deposited = float(input("Enter the amount to be deposited : "))
            self.Balance = self.Balance + money_deposited
            print("The amount you deposited " + str(money_deposited) )
            print("Amount in your account with account number " + str(self.Account_number))

    def Credit(self):
         B = int(input("Do you wish to Credit Money (1 = Yes and 2 = No) : "))
         if B == 1:
            money_credited = float(input("Enter the ammount to be credited : "))
            self.Balance = self.Balance - money_credited
            print("The amount you credited " + str(money_credited) )
            print("Amount in your account with account number " + str(self.Account_number))

            if self.Balance == 0:
                print("No more Money can be credited")
            
    def Shopping(self):
        print("Let's Check your expense of this Month")
        print("Please answer the asked question as this is impotant for calculation on your expense ")

        Catagories = ["Dairy", "Electronics", "Entertainment", "Snacks"]


        amounts = []

        for item in Catagories:
            amount = float(input("Enter amount Spend on " + item + " : "))
            amounts.append(amount)

        Total = sum(amounts)
        print("Your Total Spend on Shopping " + str(Total) )

        Max = max(amounts)
        Index = amounts.index(Max)

        if Index == 0:
            A = "Dairy"
        elif Index == 1:
            A = "Electronics"
        elif Index == 2:
            A = "Entertainment"
        elif Index == 3:
            A = "Snacks"
        print("You Spend Most on " + str(A) + " : " + str(Max))



First_name = input("Enter First Name: ")
Last_name = input("Enter Last Name: ")
Profession = input("Enter Profession: ")
Account_number = int(input("Enter Account Number: "))
Balance = float(input("Enter Balance: "))

Grid = Expense(First_name, Last_name, Profession, Account_number, Balance)

Grid.Deposit()
Grid.Credit()
Grid.Shopping()