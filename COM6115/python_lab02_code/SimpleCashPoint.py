from contextlib import nullcontext

def cashpoint(truepin, request, amount):
    balance = 3415.55
    if check_pin(truepin):
        # Case where PIN check succeeds
        if request == 'balance':
            print("Your current Balance : " + str(balance))
        if request == 'withdraw':
            balance = balance - amount
            if balance < 0 or amount > 100:
                print("Insufficient Funds OR amount exceed limit !!!  ")
                exit(1)
            else:
                print("Your withdraw amount : " + str(amount))
                print("Your balance : " + str(balance))
    else:
        # Case where PIN check fails
        print("Your PIN is incorrect ")

def check_pin(truepin):
    # Code asking user to input their pin
    # Returns True or False, depending on success of check
    if truepin == '1234':
       return True
    else:
       return False


def main():
    pin = input("Enter your ATM pin :  ")
    request_type = input("Choose your request type : ")
    if request_type == 'balance':
        cashpoint(pin, request_type, None)
    if request_type == 'withdraw':
        amount = int(input("Enter your amount :  "))
        cashpoint(pin, request_type, amount)
    if request_type == 'mobile_phone_TopUp':
        print("The service is unavailable  ")
        exit(1)

if __name__ == "__main__":
    main()
#result = cashpoint("1234", 3415.55)
