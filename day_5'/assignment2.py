class bank_account:
    pass

def create(acc_no, name, password, balance, irate, entered_password):
    b = bank_account()
    b.acc_no = acc_no
    b.name = name
    b.password = password
    b.balance = balance
    b.irate = irate
    b.entered_password = entered_password

    return b

def is_valid_password(b):
        return isinstance(b,bank_account) and b.password == b.entered_password

def is_valid(b, withdraw_amount):
       # if is_valid_password(b):

            return isinstance(b,bank_account) and withdraw_amount > 0
       # else:
       #      print(f' <PASSWORD MISMATCH> ')



def deposit(b, d_amount):
    if d_amount > 0:
        b.balance += d_amount
        return b.balance
    

def withdraw(b, withdraw_amount):
    if b.balance > withdraw_amount:
        b.balance = b.balance - withdraw_amount
        return b.balance  
    else:
        return f'<Insufficient Balance>' 


def credit_interest(b):
    b.balance += (b.balance*b.irate/1200) 
    return (b.balance) 

def info(b):
    return f'Bank Account<{b.acc_no, b.name, b.password, b.balance, b.irate}>'

def draw(b):
    print(info(b))

def test_bank_account(acc_no, name, password, balance, irate, entered_password):
    b = create(acc_no, name, password, balance, irate, entered_password)
    draw(b)
    credit_interest(b)
    deposit_amount = float(input('Amount to be deposited '))

    print(f'balance after deposit = {deposit(b,deposit_amount)}')

    draw(b)
    withdraw_amount = float(input('Amount to be Withdrawn '))
    if is_valid_password(b):
        if is_valid(b, withdraw_amount):
            print(f'balance after withdraw = {withdraw(b,withdraw_amount)}')
        
        else:
            print(f' <Enter a positive value> ')
    else:
         print(f' <PASSWORD MISMATCH> ')
    


test_bank_account(acc_no = 12345678945,name = "Amitabh Devnath", password = "abcd", balance = 10000, irate = 5, entered_password = "abcd")









