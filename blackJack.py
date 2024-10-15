import random

def getValue(card):
    try:
        return int(card)
    except:
        if card == "J" or "Q" or "K":
            return 10
        else:
            return 11
        
print("Automatic Blackjack Player\n")

games = 0
gameOver = False
deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 5000
stats = []

blackjackCount = 0
over17 = 0
numberBusts = 0 

while not gameOver:
    
    random.shuffle(deck)
    
    hand = []
    score = 0
    
    while score < 17 and len(deck) != 0:
        card = deck.pop()
        hand.append(card)
        score = score + getValue(card)
        
    if score == 21:
        print("Blackjack!!!")
        games += 1
        blackjackCount += 1
    elif score < 21:
        if score == 17:
            print("Won with 17")
        #print("You have scored " + str(score))
        games += 1
    else:   
        print("Bust")
        games += 1
        numberBusts += 1
        
    if score > 17:
        over17 += 1
        
    #print("Your cards were " + str(hand) + "\n")
    
    if len(deck) < 1:
        gameOver = True

numberOfGames = games
print("\nYou played " + str(numberOfGames) + " games.")

def Statistics(blackjackCount, over17, numberBusts, numberOfGames):
     
    stats.append(blackjackCount)
    stats.append(over17)
    stats.append(numberBusts)
    
    bP = round(blackjackCount / numberOfGames * 100, 2)
    o17 = round(over17 / numberOfGames * 100, 2)
    nB = round(numberBusts / numberOfGames * 100, 2)
    
    print(str(bP) + "%" + " of games resulted in a Blackjack")
    print(str(o17) + "%" + " of games resulted in a Value over 17")
    print(str(nB) + "%" + " of games resulted in a Bust")
    
    print(stats)

Statistics(blackjackCount, over17, numberBusts, numberOfGames)


input("press enter to exit")