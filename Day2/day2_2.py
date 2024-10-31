#Open and read file
f = open("Day2\\input.txt", "r")

def cal_score(O_hand, M_hand):
    #x = lose
    #Y = draw
    #z = win
    #1 point for Rock, 2 for Paper, and 3 for Scissors
    #0 if you lost, 3 if the round was a draw, and 6 if you won
    #A = Rock - B = Papir - C = Scissors

    #My action is win
    if M_hand == "Z":
        if O_hand == "A":
            score = 6+2
        elif O_hand == "B":
            score = 6+3
        else: score =6+1

    #My action is draw
    if M_hand == "Y":
        if O_hand == "A":
            score = 3+1
        elif O_hand == "B":
            score = 3+2
        else: score =3+3

    #My action is lose
    if M_hand == "X":
        if O_hand == "A":
            score = 0+3
        elif O_hand == "B":
            score = 0+1
        else: score =0+2

    return score


total_score = 0
for i in f: 
    total_score = total_score + cal_score(i[0],i[2])

print(f'The total_score is: {total_score}')