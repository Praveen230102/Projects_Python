import random
words = ["Boy", "Girl", "Hat", "Chicken", "Egg", "House", "Father", "Brush", "Mother"]


def display_hidden_word(string):
    print(string)


def word_splitter(string):
    new_string = ""
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i]
        else:
            new_string += "-"
    return new_string


def input_(word1, hidden_ans1):

    if not check_equality(word1, hidden_ans1):
        pos = int(input("Enter the position you want to enter the character > ")) - 1
        character = input("Enter the character > ")
        if pos > len(word1):
            print("Input is Invalid !!! ")
            input_(word1, hidden_ans1)
        elif hidden_ans1[pos] != "-":
            print("You Can't change the original characters please enter with valid input !!")
            input_(word1, hidden_ans1)
        else:
            input_word(pos, character, word1, hidden_ans1)


def check_equality(word, hidden_):
    if word == hidden_:
        return True
    else:
        return False


def play_What_the_word?():

    print("How many times you wanna to play > ")

    score = 0

    for _ in range(int(input())):

        print("Problem >", _+1)
        word = random.choice(words)

        hidden_word = word_splitter(word)

        display_hidden_word(hidden_word)

        input_(word, hidden_word)

        score += 1

    print("Your total score is >", score)


def input_word(index_, string, original, hidden):
    if original[index_] == string:
        print("You entered the correct Character at correct place ...")
        new = list(hidden)
        new[index_] = string
        updated_hidden = "".join(new)

        if check_equality(original, updated_hidden):
            print("You played well ...")
            print("Keep it up !!!")
            return True

        if not check_equality(original, updated_hidden):
            input_(original, updated_hidden)
    else:
        print("You entered wrong character or wrong index !!!")
        print("If you wanna to know the answer type 1 else 0")
        x = int(input())
        if x == 1:
            print("The answer is >", original)
            return False
        else:
            input_(original, hidden)


play_What_the_word?()


