def game():
    score = int(input("Enter your score: "))
    return score

score = game()

with open("high_score.txt") as f:
    content = f.read().strip()
    Highscore = int(content) if content else 0

if score > Highscore:
    with open("high_score.txt", "w") as f:
        f.write(str(score))
    print("File updated. New content should be:", score)
    print("Congratulations! You have a new high score.")
else:
    print("Your score is not higher than the current high score.")