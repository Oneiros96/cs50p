def main():
    cost = 50
    payed = 0
    accepted_coins = (5, 10, 25)

    while payed < cost:
        print("Amount Due:", (cost - payed))
        inserted_coin = int(input("Insert Coin: "))
        if inserted_coin in accepted_coins:
            payed += inserted_coin

    print("Change Owed:", (payed - cost))

if __name__ == "__main__":
    main()