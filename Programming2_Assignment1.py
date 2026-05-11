#Question 1
class Employee:
    def __init__(self, code, name, current_date, date_of_joining, age):
        self.__code = code
        self.__name = name
        self.__date_of_joining = date_of_joining
        self.__age = age
        self.__current_date = current_date
    def get_code(self):
        return self.__code
    def set_code(self, new_code):
        self.__code = new_code
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def get_date_of_joining(self):
        return self.__date_of_joining
    def set_date_of_joining(self, new_date_of_joining):
        self.__date_of_joining = new_date_of_joining
    def get_current_date(self):
        return self.__current_date
    def set_current_date(self, new_current_date):
        self.__current_date = new_current_date
    def get_age(self):
        return self.__age
    def set_age(self, new_age):
        self.__age = new_age
    def experience(self):
        split1 = self.__current_date.split("-")
        split2 = self.__date_of_joining.split("-")
        current_day = int(split1[0])
        current_month = int(split1[1])
        current_year = int(split1[2])
        day_of_joining = int(split2[0])
        month_of_joining = int(split2[1])
        year_of_joining = int(split2[2])       
        years_of_experience = current_year - year_of_joining
        if current_month < month_of_joining:
            years_of_experience -= 1
        elif current_month == month_of_joining and current_day < day_of_joining:
            years_of_experience -= 1
        return years_of_experience
    def display(self):
        print(self.__name)
def display_employees(lst, year):
    for employee in lst:
        if employee.experience() >= year:
            employee.display()
def main():
    Employees_list = []
    file = open("C:/Users/HP/Documents/E.txt", "r")
    lines = file.readlines()
    for line in lines:
        line = line.strip().split(", ")
        employee1obj = Employee(line[0], line[1], line[2], line[3], line[4])
        Employees_list.append(employee1obj)
    minimum_years = 2
    display_employees(Employees_list, minimum_years)
    file.close()
main()

#Question 2
class Bug:
    def __init__(self, initialPosition = 0):
        self.initialPosition = initialPosition
        self.moving = "right"
    def turn(self):
        if self.moving == "right":
            self.moving = "left"
        elif self.moving == "left":
            self.moving = "right"
    def move(self):
        if self.moving == "right":
            self.initialPosition += 1
        else:
            self.initialPosition -= 1
    def getPosition(self):
        return self.initialPosition
bugobj = Bug(7)
bugobj.move()
bugobj.turn()
bugobj.move()
bugobj.move()
print(bugobj.getPosition())

#Question 3
class ATM:
    CHECKING_ACCOUNT_PATH = "C:/Users/HP/Documents/CheckingAccount.txt"
    SAVINGS_ACCOUNT_PATH = "C:/Users/HP/Documents/SavingsAccount.txt"  
    def __init__(self, user_id, PIN):
        self.user_id = user_id
        self.PIN = str(PIN) 
        self.saving = False
        self.checking = False
    def check_checking_account(self):
        try:
            file = open(ATM.CHECKING_ACCOUNT_PATH, "r")
            lines = file.readlines()
            name = lines[0].strip()
            pin = lines[1].strip()    
            if self.user_id == name and self.PIN == pin:
                self.checking = True
                return True
            return False
        except FileNotFoundError:
            return "The Checking Account file was not found."
    def check_saving_account(self):
        try:
            file = open(ATM.SAVINGS_ACCOUNT_PATH, "r")
            lines = file.readlines()
            name = lines[0].strip()
            pin = lines[1].strip()
            if self.user_id == name and self.PIN == pin:
                self.saving = True
                return True
            return False
        except FileNotFoundError:
            return "The Savings Account file was not found."
    def check_balance_checking_account(self):
        if self.checking:
            file = open(ATM.CHECKING_ACCOUNT_PATH, "r")
            balance = file.readlines()[2].strip()
            return balance
        return "Please log in to your account."
    def check_balance_saving_account(self):
        if self.saving:
            file = open(ATM.SAVINGS_ACCOUNT_PATH, "r")
            balance = file.readlines()[2].strip()
            return balance
        return "Please log in to your account."
    def withdraw_checking_account(self, withdraw):
        if self.checking:
            file = open(ATM.CHECKING_ACCOUNT_PATH, "r")
            info = file.readlines()
            balance = int(info[2].strip())
            if balance >= withdraw:
                balance -= withdraw
                info[2] = str(balance) + "\n"
                file = open(ATM.CHECKING_ACCOUNT_PATH, "w") 
                file.writelines(info)
                return "Your transaction was successful."
            return "Not enough balance."
        return "Please log in to your account."
    def withdraw_saving_account(self, withdraw):
        if self.saving:
            file = open(ATM.SAVINGS_ACCOUNT_PATH, "r") 
            info = file.readlines()
            balance = int(info[2].strip())
            if balance >= withdraw:
                balance -= withdraw
                info[2] = str(balance) + "\n"
                file = open(ATM.SAVINGS_ACCOUNT_PATH, "w")
                file.writelines(info)
                return "Your transaction was successful."
            return "Not enough balance."
        return "Please log in to your account."
    def transfer_money_check_to_saving(self, transfer):
        if self.checking:
            try:
                file = open(ATM.CHECKING_ACCOUNT_PATH, "r")
                check_info = file.readlines()
                check_balance = int(check_info[2].strip())    
                file1 = open(ATM.SAVINGS_ACCOUNT_PATH, "r")
                save_info = file1.readlines()
                save_balance = int(save_info[2].strip())
                if transfer <= check_balance:
                    check_balance -= transfer
                    save_balance += transfer
                    check_info[2] = str(check_balance) + "\n"
                    save_info[2] = str(save_balance) + "\n"
                    file.close()   
                    file = open(ATM.CHECKING_ACCOUNT_PATH, "w")
                    file.writelines(check_info)
                    file.close()
                    file1.close()
                    file1 = open(ATM.SAVINGS_ACCOUNT_PATH, "w") 
                    file1.writelines(save_info)
                    file1.close()
                    return "Your transfer is complete."
                return "Not enough balance."
            except FileNotFoundError:
                return "The account file was not found."
        return "Please log in to your account."
    def transfer_money_saving_to_check(self, transfer):
        if self.saving:
            try:
                file = open(ATM.SAVINGS_ACCOUNT_PATH, "r")
                save_info = file.readlines()
                save_balance = int(save_info[2].strip())
                file1 = open(ATM.CHECKING_ACCOUNT_PATH, "r")
                check_info = file1.readlines()
                check_balance = int(check_info[2].strip())
                if transfer <= save_balance:
                    save_balance -= transfer
                    check_balance += transfer
                    save_info[2] = str(save_balance) + "\n"
                    check_info[2] = str(check_balance) + "\n"
                    file.close()
                    file = open(ATM.SAVINGS_ACCOUNT_PATH, "w")
                    file.writelines(save_info)
                    file.close()
                    file1.close()
                    file1 = open(ATM.CHECKING_ACCOUNT_PATH, "w")
                    file1.writelines(check_info)
                    file1.close()
                    return "Your transfer is complete."
                return "Not enough balance."
            except FileNotFoundError:
                return "The account file was not found."
        return "Please log in to your account."
def main():
    while True:
            account = int(input("Please enter 1 for checking account, 2 for saving account, or 0 to exit: "))
            if account == 0:
                print("Exiting the system.")
                break
            if account == 1:
                checking_name = input("Please enter your name: ")
                checking_PIN = input("Please enter your PIN: ")
                atm = ATM(checking_name, checking_PIN)
                if atm.check_checking_account():  
                    while True:  
                            method = int(input("Enter 1 to check your balance, 2 to withdraw, or 3 to transfer to savings, or 0 to exit: "))
                            if method == 1:
                                print(atm.check_balance_checking_account())
                            elif method == 2:
                                withdraw_amount = int(input("Enter amount to withdraw: "))
                                print(atm.withdraw_checking_account(withdraw_amount))
                            elif method == 3:
                                transfer_amount = int(input("Enter amount to transfer: "))
                                print(atm.transfer_money_check_to_saving(transfer_amount))
                            elif method == 0:
                                print("Exiting to main menu.")
                                break  
            elif account == 2:
                saving_name = input("Please enter your name: ")
                saving_PIN = input("Please enter your PIN: ")
                atm = ATM(saving_name, saving_PIN)
                if atm.check_saving_account(): 
                    while True:  
                            method = int(input("Enter 1 to check your balance, 2 to withdraw, or 3 to transfer to checking, or 0 to exit: "))
                            if method == 1:
                                print(atm.check_balance_saving_account())
                            elif method == 2:
                                withdraw_amount = int(input("Enter amount to withdraw: "))
                                print(atm.withdraw_saving_account(withdraw_amount))
                            elif method == 3:
                                transfer_amount = int(input("Enter amount to transfer: "))
                                print(atm.transfer_money_saving_to_check(transfer_amount))
                            elif method == 0:
                                print("Exiting to main menu.")
                                break  
            else:
                print("You have to enter 1, 2, or 0 to exit.")
main()

#Question 4
def indexOf(text, string, n = 0):
    if string not in text:
        return -1
    if text[ : len(string)] == string:
        return n
    else:
        return indexOf(text[1 : ], string, n + 1)
print(indexOf("Mississippi","sip"))

#Question 5
class BurgerStand:
    total_burgers_sold = 0
    def __init__(self, ID_number, burgers_sold):
        self.ID_number = ID_number
        self.burgers_sold = burgers_sold
        BurgerStand.total_burgers_sold += burgers_sold
    def JustSold(self):
        self.burgers_sold += 1
        BurgerStand.total_burgers_sold += 1
    def get_burgers_sold(self):
        return self.burgers_sold
    def get_total_burgers_sold(self):
        return BurgerStand.total_burgers_sold
def main():
    all_burger_stands = []
    while True:
        answer = int(input("Do you want to enter the number of burgers sold? Enter 1 to add information, 2 to view the total number of burgers sold, and 0 to exit."))
        if answer == 1:
            id_number = int(input("Please enter the id number of your burger stand."))
            burgers_sold = int(input("Please enter the number of burgers sold by your burger stand."))
            burgerobj = BurgerStand(id_number, burgers_sold)
            all_burger_stands.append(burgerobj)
        elif answer == 2:
            if all_burger_stands:
                print(all_burger_stands[0].get_total_burgers_sold())
            else:
                print("No burgers have been sold.")
        elif answer == 0:
            print("You are exiting the program.")
            break
main()

    

    
        
        
    

    
        


        


        
    

