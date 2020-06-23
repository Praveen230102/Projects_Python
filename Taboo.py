# new project

data = {
    "Test": ["Study", "Learn", "School", "Teacher", "Answer"],
    "Sailor": ["Ship", "Sea", "Captain", "Boat", "Ocean"],
    "Cactus": ["Plant", "Green", "Needle", "Desert", "Water"],
    "Raincoat": ["Rain", "Yellow", "Wet", "Umbrella", "Outside"],
    "Pirate": ["Ship", "Evil", "Eyepatch", "Sword", "Pistol"],
    "Nose": ["Smell", "Face", "Sense", "Nostril", "Body"],
    "Ball": ["Air", "Basket", "Bounce", "Circle", "Foot"],
    "Car": ["Driver", "Ride", "Transport", "Fast", "Travel"],
    "Dragonfly": ["Red", "Wings", "Insect", "Fly", "Dragon"],
    "SnowFlake": ["Cold", "Winter", "Flower", "Snow", "Fall"],
    "Hungry": ["Feeling", "Eat", "Food", "Breakfast", "Meal"],
    "Duck": ["Bird", "Yellow", "Chicken", '"Quack"', "Food"],
    "Pillow": ["Head", "Sleep", "Soft", "Bed", "Blanket"],
    "Dance": ["Shoes", "Romantic", "Music", "Sing", "Town Square"],
    "Proud": ["Feeling", "Accomplish", "Great", "Boast", "Humble"]
}


def check_answer(original_answer):
    string = input("Enter your answer > ")
    if string.lower() == original_answer.lower():
        print("You are doing Fucking great ")
        return 1
    else:
        print("oops! You entered the wrong answer :(")
        print("If you want to know the answer type 1 else 0")
        temp = int(input())
        if temp == 1:
            print("The answer is > ", original_answer)
        else:
            check_answer(original_answer)


def give_hints(hint_list):
    print("Here are the hints of that word ")
    for _ in hint_list:
        print(_)


def play_taboo():
    score = 0
    total_score = len(data.keys())
    for name, hints in data.items():
        answer = name
        hint = hints
        give_hints(hint)
        if check_answer(answer) == 1:
            score += 1
            print("here is the next quest !!!")
        # make a function to give hints
        # make a function to input answer
        # make a function to check answer

    print("Your total score is", score, "out of", total_score)


play_taboo()
