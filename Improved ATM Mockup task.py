database = {}
import  random
#welcome page
def init():
    print('you are welcome to JC Bank plc')
    have_acct = int(input('Do you have an account with us? 1: YES, 2: NO \n'))
    if have_acct == 1 :
        login()
    elif have_acct == 2 :
        register()
    else:
        print('invalid response')
        init()


def login() :
    print('******LOGIN PAGE*****')
    user_number = int(input('Enter your account number: \n'))
    password = input('Enter your password: \n')
    for account_no, details in database.items():
        if account_no == user_number :
            if details[3] == password:
                bank_operations()
            else:
                print('invalid account no or password')
                login()
        else:
            print('invalid account no or password')
            login()


def register():
    print('*******REGISTRATION******')
    first_name = input('Enter your first name: \n')
    last_name = input('Enter your last name: \n')
    email = input('Enter a valid email address: \n')
    pass_word1 = input('Enter your desired password: \n')
    pass_word2 = input('Enter your desired password again: \n')
    if pass_word1 == pass_word2 :
        print('password is match')
    else:
        print('password doesnt match')
        register()
    first_deposit = int(input('Make Your First deposit: \n'))
    account_no = gen_acct_no()
    database[account_no]= [first_name, last_name, email, pass_word1, first_deposit]
    print('Registration Successful !!!')
    print('Account Number:')
    print(account_no)
    login()




def gen_acct_no():
    return random.randrange(1111111111, 9999999999)

def bank_operations():
    for account_no, details in database.items():
        print('********WELCOME '+ details[1] +'********')
        print('What would like to do today?')
        print('1. cash Deposit')
        print('2. withdrawal')
        print('3. Make Complaint')
        print('4. Logout')
        print('5. Exit')
        selected_option= int(float(input('please select an option: \n')))
        if selected_option == 1 :
            cash_deposit()
        elif selected_option == 2:
            with_drawal()
        elif selected_option == 3:
            make_complaint()
        elif selected_option == 4:
            login()
        elif selected_option == 5:
             print('Thank you for banking with us')
             init()
        else:
            print('invalid selection')
            print('pls select a valid response')
            bank_operations()



def cash_deposit():
     for account_no, details in database.items():
        amount = int(input('Enter amount : \n'))
        deposit = details[4] + amount
        print('Transaction successful !!! ')
        print('ACCOUNT BALANCE =  ' + str (deposit))
        opp_return()

def with_drawal():
    for account_no, details in database.items():
        amount = int(input('Enter amount : \n'))
        if amount <= details[4] :
            withdrawal = details[4] - amount
            print('Transaction successful !!! ')
            print('ACCOUNT BALANCE =  ' + str (withdrawal))
            opp_return()
    if amount > details[4] :
        print('Insufficient Funds')
        opp_return()


def make_complaint():
    complain = (input('What issue would you like to inform us:  \n '))
    print('Your Complaints has been Recorded')
    opp_return()

def logout():
    login()









def opp_return():
    another_transaction =int(input('Do you want to perform another transaction? 1.YES  2. NO '))
    if another_transaction == 1 :
        print('1. cash Deposit')
        print('2. withdrawal')
        print('3. Make Complaint')
        print('4. Logout')
        print('5. Exit')
        selected_option= int(float(input('please select an option: \n')))
        if selected_option == 1 :
            cash_deposit()
        elif selected_option == 2:
            with_drawal()
        elif selected_option == 3:
            make_complaint()
        elif selected_option == 4:
            login()
        elif selected_option == 5:
            init()
        else:
            print('invalid selection')
            print('pls select a valid response')
            bank_operations()
    elif another_transaction == 2 :
        logout()
    else:
        print('invalid response')
        opp_return()


def operation (Acct_balance , deposit):
    deposit = int(input('Enter Amount: \n'))
    new_balance = Acct_balance + deposit
    return





init()
#gen_acct_no()
#register()
#with_drawal()
