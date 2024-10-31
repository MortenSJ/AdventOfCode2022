#Open and read file
f = open("Day2\\input.txt", "r")

def cal_score(O_hand, M_hand):
    #A = Rock - B = Papir - C = Scissors
    #X = Rock - Y = Paper - Z = Scissors
    #1 point for Rock, 2 for Paper, and 3 for Scissors
    #0 if you lost, 3 if the round was a draw, and 6 if you won

    #My hand value
    if M_hand == "X": hand_val = 1
    elif M_hand == "Y": hand_val = 2
    elif M_hand == "Z": hand_val = 3

    #Win
    if O_hand =="A" and M_hand == "Y" or O_hand =="B" and M_hand =="Z" or O_hand =="C" and M_hand == "X":
        score = 6 + hand_val
        print(f'win and score is {score} O_hand is {O_hand} and M_hand is {M_hand}')

    #Draw
    elif O_hand == "A" and M_hand == "X" or O_hand == "B" and M_hand == "Y" or O_hand == "C" and M_hand == "Z":
        score = 3 + hand_val
        print(f'Draw and score is {score} O_hand is {O_hand} and M_hand is {M_hand}')
    #Lose
    else: 
        score = 0 + hand_val
        print(f'Lose and score is {score} O_hand is {O_hand} and M_hand is {M_hand}')
    return score


total_score = 0
for i in f: 
    total_score = total_score + cal_score(i[0],i[2])

print(f'The total_score is: {total_score}')