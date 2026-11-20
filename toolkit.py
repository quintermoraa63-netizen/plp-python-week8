
import random

# Welcome message
print("=" * 40)
print("WELCOME TO MY PERSONAL MINI-TOOLKIT!")
print("=" * 40)


# Tool 1: Simple Calculator
# Allows users to perform basic mathematical operations.
def calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter your choice (1-4): ")

        if operation == "1":
            result = num1 + num2
            print(f"The answer is: {result}")

        elif operation == "2":
            result = num1 - num2
            print(f"The answer is: {result}")

        elif operation == "3":
            result = num1 * num2
            print(f"The answer is: {result}")

        elif operation == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"The answer is: {result}")
            else:
                print("Sorry, division by zero is not allowed.")

        else:
            print("Invalid operation. Please choose between 1 and 4.")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: Number Guessing Game
# Allows users to guess a randomly selected number.
def number_guessing_game():
    print("\n--- NUMBER GUESSING GAME ---")

    secret_number = random.randint(1, 10)
    attempts = 5

    while attempts > 0:
        try:
            guess = int(input("Guess a number between 1 and 10: "))

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue

            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number}!")
                return

            elif guess < secret_number:
                print("Too low! Try a higher number.")

            else:
                print("Too high! Try a lower number.")

            attempts -= 1
            print(f"You have {attempts} attempts remaining.")

        except ValueError:
            print("Please enter a whole number.")

    print(f"Game over! The correct number was {secret_number}.")


# Tool 3: To-Do List
# Allows users to add, view and remove tasks using a list.
def todo_list():
    tasks = []

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task you want to add: ").strip()

            if task:
                tasks.append(task)
                print(f"Task '{task}' added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is currently empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(input("Enter the task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task '{removed_task}' removed successfully!")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid task number.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please select between 1 and 4.")


# Main menu: Repeats until the user chooses to quit.
def main():
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Simple Calculator")
        print("2. Number Guessing Game")
        print("3. To-Do List")
        print("4. Quit")
        print("===============================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            calculator()

        elif choice == "2":
            number_guessing_game()

        elif choice == "3":
            todo_list()

        elif choice == "4":
            print("\nThank you for using My Personal Mini-Toolkit!")
            print("Goodbye! Have a wonderful day.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Start the program.
main()
