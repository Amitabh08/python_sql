from Banking.bank import Bank
from Banking.atm import ATM
def main():
    print('Hello Banking App')
    boi = Bank('BOI', 12)
    atm = ATM(boi)
    boi.create_account('Amitabh' ,'p@ss', 50000)
    boi.create_account('Aditya' ,'p@ss', 50000)
    boi.create_account('Gary' ,'p@ss', 50000)
    boi.create_account('Bob' ,'p@ss', 50000)
    boi.info_all__accounts()
    while True:
        if atm.start():
            continue



if __name__=='__main__':
    main()