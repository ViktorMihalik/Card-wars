#Head of the game
import random


cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

print("""
.------..------..------..------..------..------..------..------.
|C.--. ||A.--. ||R.--. ||D.--. ||W.--. ||A.--. ||R.--. ||S.--. |
| :/\: || (\/) || :(): || :/\: || :/\: || (\/) || :(): || :/\: |
| :\/: || :\/: || ()() || (__) || :\/: || :\/: || ()() || :\/: |
| '--'C|| '--'A|| '--'R|| '--'D|| '--'W|| '--'A|| '--'R|| '--'S|
`------'`------'`------'`------'`------'`------'`------'`------'
""")

print("Let's play 'card wars'. The rules are easy- who have higher card get a point")
player_name = input("\nWho is my oponet? Add my you name: ")

max_points= int(input("\nTell my {} How many victory points do you want to play?: ".format(player_name)))
number_of_cards= int(input("\nLast question With how many cards will we play?(min 1 and max 10):  "))

#Avoiding player to chose more card or none
while number_of_cards > 10:
    number_of_cards= int(input("\n You can chose only from 1 to 10):  "))
    if number_of_cards < 10:
        break

while number_of_cards < 0:
    number_of_cards= int(input("\n You can chose only from 1 to 10):  "))
    if number_of_cards > 1:
        break

# Flipping coin in case of equal game
def flip_coin():

    player_coin = input("\nIt's a draw, let's flip a coin. What's your choice tail or head: ").lower()
    coin= "tail","head"
    coin_side= random.choice(coin)
    if player_coin not in coin:
        player_coin= input("\nplease choose betwen tail or head: ").lower()

    if player_coin  in coin_side:
        if player_coin == coin_side:
            print("\nYeah god guees {} It's {}, you won.".format(player_name,coin_side))
    else:
        print("\n It's {}, I'ma a winner.".format(coin_side))
    
#Definiton for shuffling cards
def shuffling_cards(r):
    hand = []
    for i in range(r):
        random_cards=[str(random.choice(cards))]
        hand=hand+random_cards
    return hand

# Game mechanism   
player_point_CRD = 0
computer_points_CRD = 0

players_cards = shuffling_cards(number_of_cards)
computer_cards = shuffling_cards(number_of_cards)

while computer_points_CRD or player_point_CRD != max_points:
    
    computer_choice_CRD = str(random.choice(computer_cards))

    player_choice=input("\nPlease choose one card from your hand {}:".format(players_cards)).upper()
   
    if player_choice not in players_cards:
        player_choice = input("\nAgain check your card an dchoose one {}:".format(players_cards)).upper()
            
    if cards.index(computer_choice_CRD) > cards.index(player_choice):
        print("\n{} is higher than {} that means point for me".format(computer_choice_CRD,player_choice))
        computer_points_CRD += 1
    if cards.index(computer_choice_CRD) < cards.index(player_choice):
        print("\nOkay I have {}, point for you {}".format(computer_choice_CRD,player_name))
        player_point_CRD += 1
    if cards.index(computer_choice_CRD) == cards.index(player_choice):
        print("\nMy is also {}, boring no one get a point".format(computer_choice_CRD))
    
    players_cards.remove(player_choice)
    computer_cards.remove(computer_choice_CRD)
    print("{}: {} and computer:{}".format(player_name,player_point_CRD,computer_points_CRD))
    
    if not players_cards:# in case that player is out of cards and game is still running
        if player_point_CRD > computer_points_CRD:
            print("Congratulations {} you are the winner".format(player_name))
            break

        if computer_points_CRD > player_point_CRD:
            print("I beat you {}".format(player_name))
            break
        
        if computer_points_CRD == player_point_CRD:
            flip_coin()
            break
            
    if player_point_CRD == max_points:
        print("Congratulations {} you are the winner".format(player_name))
        break
    if computer_points_CRD == max_points:
        print("I beat you {}".format(player_name))
        break


      

    

    


