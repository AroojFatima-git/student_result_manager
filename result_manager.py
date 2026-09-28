"""Student Result Manager
A simple console app to add students, calculate results and save them to CSV.
"""

import csv
import os

FILE_NAME = "results.csv"
FIELDS = ["roll_no", "name", "marks", "total", "percentage", "grade"]
SUBJECTS = ["English", "Urdu", "Maths", "Physics", "Computer"]
MAX_MARKS = 100


def calculate_grade(percentage):
    """Return grade based on percentage."""
    if percentage >= 80:
        return "A+"
    if percentage >= 70:
        return "A"
    if percentage >= 60:
        return "B"
    if percentage >= 50:
        return "C"
    if percentage >= 40:
        return "D"
    return "F"


def load_students():
    """Load all students from the CSV file."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_students(students):
    """Save all students to the CSV file."""
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(students)


def read_marks(subject):
    """Keep asking until a valid mark (0-100) is entered."""
    while True:
        try:
            marks = float(input(f"  {subject} marks (0-{MAX_MARKS}): "))
            if 0 <= marks <= MAX_MARKS:
                return marks
            print("  Marks 0 se 100 ke beech hone chahiye.")
        except ValueError:
            print("  Please number enter karein.")


def add_student(students):
    roll_no = input("Roll number: ").strip()
    if any(s["roll_no"] == roll_no for s in students):
        print("Ye roll number pehle se maujood hai.")
        return
    name = input("Student name: ").strip()

    marks_list = [read_marks(subject) for subject in SUBJECTS]
    total = sum(marks_list)
    percentage = round(total / (MAX_MARKS * len(SUBJECTS)) * 100, 2)

    students.append({
        "roll_no": roll_no,
        "name": name,
        "marks": "|".join(str(int(m)) if m.is_integer() else str(m) for m in marks_list),
        "total": total,
        "percentage": percentage,
        "grade": calculate_grade(percentage),
    })
    save_students(students)
    print(f"Saved! {name}: {percentage}% (Grade {students[-1]['grade']})")


def show_students(students):
    if not students:
        print("Abhi koi record nahi hai.")
        return
    print(f"\n{'Roll':<8}{'Name':<20}{'Total':<8}{'%':<8}{'Grade'}")
    print("-" * 50)
    for s in students:
        print(f"{s['roll_no']:<8}{s['name']:<20}{s['total']:<8}{s['percentage']:<8}{s['grade']}")


def search_student(students):
    roll_no = input("Roll number search karein: ").strip()
    for s in students:
        if s["roll_no"] == roll_no:
            print(f"\nName: {s['name']}")
            for subject, m in zip(SUBJECTS, s["marks"].split("|")):
                print(f"  {subject}: {m}")
            print(f"Total: {s['total']} | Percentage: {s['percentage']}% | Grade: {s['grade']}")
            return
    print("Student nahi mila.")


def delete_student(students):
    roll_no = input("Delete karne wala roll number: ").strip()
    for s in students:
        if s["roll_no"] == roll_no:
            students.remove(s)
            save_students(students)
            print("Record delete ho gaya.")
            return
    print("Student nahi mila.")


def show_topper(students):
    if not students:
        print("Abhi koi record nahi hai.")
        return
    top = max(students, key=lambda s: float(s["percentage"]))
    avg = sum(float(s["percentage"]) for s in students) / len(students)
    print(f"Topper: {top['name']} ({top['percentage']}%)")
    print(f"Class average: {avg:.2f}%")


def main():
    students = load_students()
    while True:
        print("\n=== Student Result Manager ===")
        print("1. Add student")
        print("2. Show all students")
        print("3. Search by roll number")
        print("4. Show topper & class average")
        print("5. Delete student")
        print("6. Exit")
        choice = input("Choose (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            show_topper(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Allah Hafiz!")
            break
        else:
            print("Invalid choice, dobara try karein.")


if __name__ == "__main__":
    main()
