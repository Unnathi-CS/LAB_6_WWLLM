"""Simple student marks management system."""


def calculate_average(marks):
    """Return the average mark."""
    return sum(marks.values()) / len(marks)


def display_topper(marks):
    """Display the student with the highest mark."""
    topper = max(marks, key=marks.get)
    print(f"Topper: {topper} ({marks[topper]:.2f})")


def display_below_40(marks):
    """Display students who scored below 40."""
    failed_students = [name for name, mark in marks.items() if mark < 40]

    if failed_students:
        print("Students who scored below 40:")
        for name in failed_students:
            print(f"- {name}: {marks[name]:.2f}")
    else:
        print("No student scored below 40.")


def get_students():
    """Read student names and marks from the user."""
    while True:
        try:
            number_of_students = int(input("Enter the number of students: "))
            if number_of_students > 0:
                break
            print("Please enter a positive number of students.")
        except ValueError:
            print("Please enter a valid whole number.")

    marks = {}

    for student_number in range(number_of_students):
        name = input(f"Enter name of student {student_number + 1}: ").strip()
        while not name:
            print("Name cannot be empty.")
            name = input(f"Enter name of student {student_number + 1}: ").strip()

        while True:
            try:
                mark = float(input(f"Enter marks for {name} (0-100): "))
                if 0 <= mark <= 100:
                    marks[name] = mark
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    return marks


def main():
    """Run the student marks management system."""
    marks = get_students()

    print("\n--- Student Marks Report ---")
    print(f"Class average: {calculate_average(marks):.2f}")
    display_topper(marks)
    display_below_40(marks)


if __name__ == "__main__":
    main()
