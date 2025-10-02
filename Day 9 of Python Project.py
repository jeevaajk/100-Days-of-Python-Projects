import os
print('''
  _______ _             _____ _ _            _                        _   _             
 |__   __| |           / ____(_) |          | |       /\             | | (_)            
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|                                                                                        
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print("Welcome to the Auction Program........")
bids={}
bidding_finished=False
def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The Winner is {winner} with a Highest Bid of ${highest_bid}")
while not bidding_finished is True:
        name=input("Enter Your Name Gentleman : ")
        price=int(input("Enter Your Bid Amount : $"))
        bids[name]=price
        proceed=input("Are there any other Bidders Then Please Type Yes or No Gentleman  :").lower()
        if proceed=="no":
            bidding_finished=True
            find_highest_bidder(bids)
        elif proceed=="yes":
            clear=input("Please Clear the screen to keep Your Bid sceret Enter Yes : ").lower()
            if clear=="yes":
                os.system('cls' if os.name=='nt' else 'clear')
                continue
            else:
                 break
        else:
            print("Please Get out of the Auction this is not a Comedy Show")
            break
