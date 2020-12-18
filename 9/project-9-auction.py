from art import logo
import os


def clear():
    return os.system('cls')

    # HINT: You can call clear() to clear the output in the console.


def find_highest_bidder(dict):
    highest_bid = 0
    winner = ''
    # { 'nauman': 35, 'Usman': 45}
    for key in dict:
        bid = dict[key]
        if bid > highest_bid:
            highest_bid = bid
            winner = key
    print(f'The winner is {winner} with a bid of ${highest_bid}')


print(logo)

# bidders dict
bidders = {
    # name: bid
}

auction_going = True

while auction_going:
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))
    bidders[name] = bid

    restart = input(
        'Are there other users who want to bid?: "y" or "n" ').lower()

    if restart == 'no' or restart == 'n':
        print('Bidding ended')
        find_highest_bidder(bidders)
        auction_going = False
    else:
        clear()

print(bidders)
