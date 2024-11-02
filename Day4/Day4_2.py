#Open and read file
f = open("Day4\\input.txt", "r")

total_score = 0
for i in f: 
    sections = i.strip().split(",")
    range1 = sections[0].split("-")
    range1_1 = range1[0]
    range1_2 = range1[1]
    range2 = sections[1].split("-")
    range2_1 = range2[0]
    range2_2 = range2[1]
    
    if (int(range1_1) >= int(range2_1) and int(range1_1) <= int(range2_2)) or (int(range1_2) >= int(range2_1) and int(range1_2) <= int(range2_2)) or (int(range2_1) >= int(range1_1) and int(range2_1) <= int(range1_2)) or (int(range2_2) >= int(range1_1) and int(range2_2) <= int(range1_2)):
        print(f'Sections: {sections} is true')
        total_score += 1
    else: print(f'Sections: {sections} is false')

print(f'Totalscore is: {total_score}')
