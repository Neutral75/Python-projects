import random;

user_wins = 0;
computer_wins = 0;

options = ["rock", "paper", "scissors"];
while True:
    user_option = input("Choose Q to quit or either rock 🪨, paper 📰, or scissors ✂️ : ").lower();
    if user_option == "q":
        break;
    
    if user_option not in options:
        continue;

    random_number = random.randint(0, 2);
    computer_option = options[random_number];

    print("Computer chose" + " " + computer_option + "!");

    if user_option == computer_option:
        print("It\'s a draw!");

    elif user_option == "rock" and computer_option == "scissors":
        print("You won!");
        user_wins += 1;

    elif user_option == "paper" and computer_option == "rock":
        print("You won!");
        user_wins += 1;

    elif user_option == "scissors" and computer_option == "paper":
        print("You won!");
        user_wins += 1;

    else:
        print("You lost!");
        computer_wins += 1;

    print("\n");

print("You got" + " " + str(user_wins) + "!");
print("The computer got" + " " + str(computer_wins) + "!");
print("Goodbye!");

# python rock-paper-scissors.py for it to run!