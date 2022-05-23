import art
from replit import clear
print("Welcome to Secret bid Auction:")
print(art.logo)
data={}
while True:
    bidder=input("what is your name:")
    bid_amount=int(input("How much amount you want to Bid :"+"$"))
    data[bidder]=bid_amount
    any_other=input("Are there any other bidder? Type 'yes' or 'no' : ").lower()
    clear()
    if any_other=="no":
        break
winning_amount=0 
winning_person=""
for key,value in data.items():
      if value>winning_amount:
          winning_amount=value
          winning_person=key
print(f"The winner is {winning_person} with a bid of ${winning_amount}.")