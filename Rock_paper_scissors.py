user1 = input("player1: ")
user2 = input("player2: ")
if user1 == "paper" and user2 == "rock":
    print(user1 + " wins")
elif user1 == "paper" and user2 == "scissors":
    print(user2 + " wins")
elif user1 == "rock" and user2 == "paper":
    print(user2 + " wins")
elif user1 == "rock" and user2 == "scissors":
    print(user1 + " wins")
elif user1 == "scissors" and user2 == "paper":
    print(user1 + " wins")
elif user1 == "scissors" and user2 == "rock":
    print(user2 + " wins")
elif user1 == "paper" and user2 == "paper":
    print("game draws")
elif user1 == "rock" and user2 == "rock":
    print("game draws")
elif user1 == "scissors" and user2 == "scissors":
    print("game draws")
