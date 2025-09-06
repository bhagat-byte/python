import random
import sys

def get_user_choice():
    """Get user's choice with input validation"""
    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper") 
        print("3. Scissors")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            return 'rock'
        elif choice == '2':
            return 'paper'
        elif choice == '3':
            return 'scissors'
        elif choice == '4':
            return 'quit'
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

def get_computer_choice():
    """Get computer's random choice"""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the round"""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, result):
    """Display the result of the round"""
    print(f"\nYou chose: {user_choice.upper()}")
    print(f"Computer chose: {computer_choice.upper()}")
    
    if result == 'tie':
        print("It's a tie! 🤝")
    elif result == 'user':
        print("You win! 🎉")
    else:
        print("Computer wins! 🤖")

def play_game():
    """Main game function"""
    print("=" * 50)
    print("🎮 WELCOME TO ROCK, PAPER, SCISSORS! 🎮")
    print("First to reach 5 points wins!")
    print("=" * 50)
    
    user_score = 0
    computer_score = 0
    round_number = 1
    
    while True:
        print(f"\n--- ROUND {round_number} ---")
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        user_choice = get_user_choice()
        
        if user_choice == 'quit':
            print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
            if user_score > computer_score:
                print("🏆 Congratulations! You won the game!")
            elif computer_score > user_score:
                print("😔 Computer won the game. Better luck next time!")
            else:
                print("🤝 It's a tie game!")
            print("Thanks for playing! 👋")
            break
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, result)
        
        if result == 'user':
            user_score += 1
        elif result == 'computer':
            computer_score += 1
        
        round_number += 1
        
        # Check if either player has reached 5 points
        if user_score >= 5:
            print(f"\n🎉 CONGRATULATIONS! You reached 5 points first!")
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            print("You are the champion! 🏆")
            print("Thanks for playing! 👋")
            break
        elif computer_score >= 5:
            print(f"\n😔 GAME OVER! Computer reached 5 points first!")
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            print("Better luck next time! 🤖")
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing! 👋")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)
