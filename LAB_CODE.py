# Student Marks Management System
# Simple Python program for undergraduate students


def get_student_data():
    """Ask the user for student names and marks."""
    while True:
        try:
            n = int(input("Enter the number of students: "))
            if n > 0:
                break
            print("Number of students must be greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

    marks = {}

    for i in range(n):
        name = input(f"Enter student {i + 1} name: ").strip()
        while name == "":
            print("Name cannot be empty.")
            name = input(f"Enter student {i + 1} name: ").strip()

        while True:
            try:
                mark = float(input(f"Enter marks for {name}: "))
                if 0 <= mark <= 100:
                    marks[name] = mark
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number for marks.")

    return marks


def class_average(marks):
    """Calculate the class average."""
    if len(marks) == 0:
        return 0
    total = sum(marks.values())
    return total / len(marks)


def top_student(marks):
    """Return the student with the highest marks."""
    if len(marks) == 0:
        return "No students", 0

    name = max(marks, key=marks.get)
    return name, marks[name]


def below_40(marks):
    """Return students scoring below 40."""
    low_students = []
    for name, mark in marks.items():
        if mark < 40:
            low_students.append((name, mark))
    return low_students


def main():
    """Main function to run the program."""
    marks = get_student_data()

    print("\n--- Student Marks Report ---")
    print(f"Class Average: {class_average(marks):.2f}")

    topper_name, topper_mark = top_student(marks)
    print(f"Topper: {topper_name} with {topper_mark}")

    failed = below_40(marks)
    if failed:
        print("Students below 40:")
        for name, mark in failed:
            print(f"{name}: {mark}")
    else:
        print("No student scored below 40.")


if __name__ == "__main__":
    main()
