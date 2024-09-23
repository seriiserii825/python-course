from replit import clear
from logos.auction_logo import logo
print(logo)
users = []

def createUser():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    user = { "name": name, "bid": bid }
    users.append(user)

def calcMax():
    max = 0
    name = ''
    for item in users:
        if item['bid'] > max:
            max = item['bid']
            name = item['name']
    print(f"Won {name}, with max bid: {max}")


while True:
    createUser()
    more = input("Are there any other bidders? Type 'yes' or 'no':")
    if more == 'no':
        print(users)
        calcMax()
        break
    clear()

