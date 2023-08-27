#### Banking app ####
import time
import os

class Bank():

    filename = 'TransactionHistory.txt'

    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            recentBalance = file.readlines()[-1]
            removeText = 'Balance: '
            recentBalance = recentBalance.replace(removeText, '')
            userBalance = int(recentBalance)
    else:
        with open(filename, 'w') as file:
            userBalance = 0
            file.write(f'Balance: {userBalance}')


    def Menu(self):
        print(
            " \n-----Banking App----\n",
            "--------------------\n",
            "Enter 1 to make a deposit\n",
            "Enter 2 to make a withdraw\n",
            "Enter 9 to exit\n"
        )

    
    def Withdraw(self):
        # User prompt
        self.withdrawAmount = input("\nHow much would you like to withdraw: ")
        
        # Cast input to int
        try:
            self.withdrawAmount = int(self.withdrawAmount)
            
            if self.withdrawAmount >= 1:
                # Checks user balance
                if bank.userBalance >= self.withdrawAmount:
                    print(f'\nYou would like to make a withdraw in the amount of {self.withdrawAmount}')
                
                    # Confirms user decision 
                    confirmation = input("Please enter y or n: ")
                    # User Confirms
                    if confirmation.lower() == 'y':
                        print(f'\nDispensing ${self.withdrawAmount} now...')
                        time.sleep(1)
                        print(f'Please remove the cash from the slot')
                        time.sleep(1)

                        bank.userBalance = bank.userBalance - self.withdrawAmount
                        bank.WriteTransaction(bank.userBalance, 'Withdraw: -', self.withdrawAmount)
                        
                
                    # User Denies  
                    elif confirmation.lower() == 'n':
                        print('Withdraw cancelled\n')
                
                    # Exceptions
                    else:
                        print('Invalid input, please try again\n')
                        bank.Withdraw()
            
                # User has insufficient funds
                else:
                    print('Insufficient Funds')
            else:
                print('Withdraw amount must be $1 or greater')
                bank.Withdraw()
                
        except Exception:
            print("Invalid input")
            bank.Withdraw()


    def Deposit(self):
        # User Prompt
        self.depositAmount = input("\nHow much are you depositing: ")
        
        # Cast to int
        try:
            self.depositAmount = int(self.depositAmount)
            
            # Checking minimum deposit amount
            if self.depositAmount >= 1:
                bank.userBalance = bank.userBalance + self.depositAmount
                print(f"\nDeposit made in the amount of {self.depositAmount}")
                time.sleep(1)
                bank.WriteTransaction(bank.userBalance, 'Deposit: +', self.depositAmount)
            else:
                print('You must deposit a a minimum of $1 or more\n')
                bank.Deposit()
        
        except Exception:
            print("Invalid input\n")
            bank.Deposit()
 

    def WriteTransaction(self, userBalance, transactionType, transactionAmount):
        # Add transaction to file
        with open(bank.filename, 'a') as file:
            file.write(f'\n{transactionType}{transactionAmount}\n')
            file.write(f'Balance: {userBalance}')
        
        print("\n---Transaction complete---")
        
        
        with open(bank.filename, 'r') as file:
            recentBalance = file.readlines()[-1]
            removeText = 'Balance: '
            recentBalance = recentBalance.replace(removeText, '')
            bank.userBalance = int(recentBalance)
        
        print(f'Current Account Balance: {bank.userBalance}\n')
        time.sleep(1)


dontExit = True;
bank = Bank()

while dontExit:
    # Displays the banking menu to the customer
    bank.Menu()
    userInput = input("What would you like to do: ")
    
    # Handles user input
    if userInput in ['1', '2', '9']:
        if userInput == '1':
            bank.Deposit()

        elif userInput == '2':
            bank.Withdraw()

        elif userInput == '9':
            dontExit == False
            break
    else:
        print("Invalid input please try again\n ")


# App sign off message
print(
    "\n Thanks for using the Banking App\n",
    "-------Have a great day!!-------\n"
    )
time.sleep(1)