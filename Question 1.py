class Bank: 

    def __init__(self):
        self.account = 0

    def deposit(self, amount):
        self.account += amount

    def withdraw(self, amount):
        self.account -= amount

    def get_balance(self):
        print("Total amount - $%d" % self.account)

if __name__ == "__main__":
    user = Bank()
    playing = True

    while playing: # Continuous loop until user exits with input "End".
        choice = input("Please enter Deposit or Withdraw, with amount. Enter End to quit.\n").split() #Spltting to get 2 inputs in one line.

        if len(choice) == 2: # Check if 2 inputs were passed.
            choice[1] = int(choice[1]) # Make second input into an integer for math.

            if choice[0].lower() == "deposit":
                user.deposit(choice[1])

            elif choice[0].lower() == "withdraw":
                user.withdraw(choice[1])

            else:
                print("Invalid input\n")

        elif len(choice) == 1: # If only 1 input is passed, assume ending.
            if choice[0].lower() == "end":
                user.get_balance()
                playing = False
                input()

            else:
                print("Invalid input\n")

        else:
            print("Invalid input\n")
