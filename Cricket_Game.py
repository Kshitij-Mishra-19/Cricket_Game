

total_score = 0

options = [0, 1, 2, 3, 4, 5, 6]

while True:
    user_input = int(input("Play a shot or Q to quit : "))
    if user_input == "q" :
        break

    if user_input not in options:
        print("----Play a valid shot----")
        continue

    random_number = random.randint(0, 6)
    computer_pick = options[random_number]
    print("computer picked : ", computer_pick)

    if user_input != computer_pick:
        total_score += user_input
        print("Current Score : [", total_score, "]")

    else:
        print("----OUT----")
        break
    
print("Total Score : ", total_score)

print("----GAME OVER----")
