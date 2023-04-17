


# e.g. if the item price is $13.92, and the amount paid is $20, we would want to get back
# dict {
# '20': 2000,
# '5': 500,
# '1': 100,
# 'nickel': 5,
# 'penny': 1
# }
mp = {
'20': 2000,
'5': 500,
'1': 100,
'nickel': 5,
'penny': 1
}

def make_change(price, paid):
    result = {}
    change_left = paid - price
    for key in mp:
        mp[key]
        change_left % mp[key]
    # check highest div num
    #     check remainder
    # return change
    return price

make_change(1392,2000)
# result{
#     500: 1,
#     100:1,
#     penny: 3
# }
# result = [500,100,5,1,1,1]
# change_left = 1

# print(5bill, 1bill, nickel, 3 pennies)

# 1 $5.00 bill
# 1 $1.00 bill
# 1 nickel
# 3 pennies

# Assume that the cash register has an unlimited amount of coins and bills - we can assume that we have denominations going from pennies up to 20 dollar bills.

# make_change