import csv
from datetime import datetime

FILENAME = "fitness_data.csv"
HEADERS = ["Date", "Workout Type", "Duration/Calories", "Steps", "Weight"]


def initialize_file():
    """Create the CSV file with headers if it does not exist."""
    try:
        with open(FILENAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)
    except FileExistsError:
        pass


def add_entry():
    """Collect and save a new fitness entry."""
    date = input(
        "Enter date (YYYY-MM-DD) or leave blank for today: "
    ).strip()

    if not date:
        date = datetime.today().strftime("%Y-%m-%d")

    workout_type = input(
        "Workout type (e.g., Running, Cycling, Yoga): "
    ).strip()

    duration = input(
        "Duration or calories burned: "
    ).strip()

    steps = input(
        "Steps (optional): "
    ).strip()

    weight = input(
        "Weight (optional): "
    ).strip()

    if not workout_type:
        print("⚠️ Workout type cannot be empty.")
        return

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [date, workout_type, duration, steps, weight]
        )

    print("✅ Fitness entry added successfully!")


def view_entries():
    """Display all saved fitness entries."""
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:
                print("ℹ️ No fitness entries found.")
                return

            print("\n========== FITNESS RECORDS ==========")

            for row in rows:
                print(" | ".join(row))

    except FileNotFoundError:
        print("❌ No fitness data found. Please add an entry first.")


def show_menu():
    """Display the main application menu."""
    initialize_file()

    while True:
        print("\n====== PERSONAL FITNESS TRACKER ======")
        print("1. Add New Entry")
        print("2. View All Entries")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_entry()

        elif choice == "2":
            view_entries()

        elif choice == "3":
            print("👋 Exiting. Stay healthy!")
            break

        else:
            print("⚠️ Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    show_menu()
