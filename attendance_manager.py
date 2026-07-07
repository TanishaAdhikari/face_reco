import csv
import os
from datetime import datetime

ATTENDANCE_FOLDER = "attendance"

os.makedirs(ATTENDANCE_FOLDER, exist_ok=True)


def mark_attendance(student_name):

    today = datetime.now().strftime("%Y-%m-%d")

    filename = os.path.join(
        ATTENDANCE_FOLDER,
        f"{today}.csv"
    )

    current_time = datetime.now().strftime("%H:%M:%S")

    # Create file if it doesn't exist
    if not os.path.exists(filename):

        with open(filename, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Student",
                "Time"
            ])

    # Prevent duplicate attendance
    already_present = False

    with open(filename, "r") as file:

        reader = csv.reader(file)

        for row in reader:

            if len(row) > 0 and row[0] == student_name:

                already_present = True

                break

    if not already_present:

        with open(filename, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                student_name,
                current_time
            ])

        print(f"{student_name} marked present.")

    else:

        print(f"{student_name} is already marked.")