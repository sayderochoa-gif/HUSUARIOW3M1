import os

def save_blocker():
    blocker = input("Enter your daily blocker: ")

    with open("database.txt", "a", encoding="utf-8") as file:
        file.write(blocker + "\n")

    print("Blocker saved successfully!\n")



def show_blockers():
    if os.path.exists("database.txt"):
        with open("database.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        if len(lines) == 0:
            print("No blockers found.\n")
        else:
            print("\nTeam daily blockers:")
            for line in lines:
                print("- " + line.strip())
            print()
    else:
        print("File does not exist.\n")



def warning_overwrite():
    option = input("This will delete all data. Continue? (yes/no): ")

    if option.lower() == "yes":
        with open("database.txt", "w", encoding="utf-8") as file:
            file.write("")
        print("File cleared successfully!\n")
    else:
        print("Operation cancelled.\n")



def main():
    option = ""

    while option != "4":
        print("===== TEAM DAILY STATUS =====")
        print("1. Add blocker")
        print("2. View blockers")
        print("3. Clear file")
        print("4. Exit")

        option = input("Choose an option (1-4): ")

        if option == "1":
            save_blocker()

        elif option == "2":
            show_blockers()

        elif option == "3":
            warning_overwrite()

        elif option == "4":
            print("Goodbye!")

        else:
            print("Invalid option. Try again.\n")


main()