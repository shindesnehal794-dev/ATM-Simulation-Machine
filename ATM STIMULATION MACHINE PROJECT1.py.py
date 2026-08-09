#Atm Stimulation Game

balance=5000
choice=0

while choice !=4:
    print("\n---ATM MENU---")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    
    choice= int(input("Enter your Choice:"))

    if choice==1:
        print("Balance=",balance)
    elif choice==2:
        amount=int(input("Enter amount to deposit:"))
        balance=balance+amount
        print("Deposit Successful!")

    elif choice==3:
        amount=int(input("Enter amount to withdraw:"))

        if amount<=balance:
            balance=balance-amount
            print("Please Collect your cash")
        else:
            print("Insufficient Balance!")

    elif choice==4:
        print("Thank You!")

    else:
        print("Invalid choice!")



