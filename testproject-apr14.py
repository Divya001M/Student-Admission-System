import tkinter as tk
from tkinter import messagebox, PhotoImage, ttk

# The following two lines indicate the file location of Humber logo and celebration banner used in the program. Kindly change the file path to where you downloaded the images in your system.
imgPath = "C:/Humber/humberpic-75px.png"
reportimg = "C:/Humber/celebrate.png"

class Student:
    # This creates an object named Student with name and grade as state, and the compute_gpa method below as the behavior of the object.
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        self.gpa = self.compute_gpa()

    def compute_gpa(self):
        credit_hours = [4, 5, 4, 3, 2, 4]
        total_credit_hours = sum(credit_hours)
        total_points = sum(self.grades[i] * credit_hours[i] for i in range(len(self.grades)))
        return total_points / total_credit_hours

def validate_password(password):
    specialchars = 0
    digits = 0

    # Checking if the password has at least 10 characters
    if len(password) < 10:
        return False

    # Checking if there is at least one upper case letter
    for char in password:
        if char.isupper():
            break
    else:
        return False

    # Checking if it contains two or three numbers
    for num in password:
        if num.isdigit():
            digits += 1
    if digits == 2 or digits == 3 or digits > 3:
        pass
    else:
        return False

    # Checking if it contains one special character
    for special in password:
        if special in "!@#$%^&*()-_+=<>,.?/:;{}[]|~":
            specialchars += 1
    if specialchars == 1:
        return True
    else:
        return False

def login():
    tries = 3

    def check_password():
        # Checks if the user password satisfies the criteria stated above
        nonlocal tries
        password = entry_password.get()
        if validate_password(password):
            messagebox.showinfo("Success", "Login successful!")
            window_login.destroy()
            get_students_window()
        else:
            tries -= 1
            messagebox.showerror("Error", f"Invalid password format. Attempts left: {tries}")
            if tries == 0:
                messagebox.showerror("Error", "Too many incorrect password attempts. Exiting.")
                window_login.destroy()

    window_login = tk.Tk()
    window_login.title("Login")
    window_login.geometry("800x450")
    
    background_image = PhotoImage(file=imgPath)
    """
    background_label = tk.Label(window_login, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image
    """

    label_welcome = tk.Label(window_login, text=" Welcome to Humber College", fg="black", font=("Arial", 32, "bold"), image=background_image, compound="left")
    label_welcome.grid(row=0, column=0, columnspan=2, pady=(50, 10))

    label_password = tk.Label(window_login, text="Enter password", fg="black", font=("Arial", 18, "bold"))
    label_password.grid(row=1, column=0, columnspan=2, pady=10)

    entry_password = tk.Entry(window_login, show="*", bg="white", fg="black")
    entry_password.grid(row=2, column=0, columnspan=2, pady=10)

    button_login = tk.Button(window_login, text="Login", command=check_password, bg="#00265D", fg="white", font=("Arial", 13, "bold"))
    button_login.grid(row=3, column=0, columnspan=2, pady=10)

    for i in range(2):
        tk.Grid.columnconfigure(window_login, i, weight=1)
    for i in range(1):
        tk.Grid.rowconfigure(window_login, i, weight=1)

    window_login.mainloop()

def get_students_window():
    # Asks the user to input the number of students from 1 to 50.
    # System will exit after three invalid attempts.
    invalid_attempts = 0

    def submit_students():
        nonlocal invalid_attempts
        count_students = entry_students.get()
        if not count_students.isdigit() or int(count_students) < 1 or int(count_students) > 50:
            invalid_attempts += 1
            if invalid_attempts >= 3:
                messagebox.showerror("Too Many Attempts", "Too many invalid attempts. Exiting program.")
                window_students.destroy()
            else:
                messagebox.showerror("Input Error", "Invalid number of students. Please enter a number between 1 and 50.")
        else:
            invalid_attempts = 0
            count_students = int(count_students)
            window_students.destroy()
            get_student_grades_window(count_students)

    window_students = tk.Tk()
    window_students.title("Enter Number of Students")
    window_students.geometry("800x450")

    
    background_image = PhotoImage(file=imgPath)
    """
    background_label = tk.Label(window_students, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    """

    label_students = tk.Label(window_students, text=" Enter the number of students between 1 and 50: ", fg="black", font=("Arial", 20, "bold"), image=background_image, compound="left")
    label_students.grid(row=0, column=0, columnspan=2, pady=10)

    entry_students = tk.Entry(window_students, bg="white", fg="black")
    entry_students.grid(row=1, column=0, columnspan=2, pady=10)

    button_submit = tk.Button(window_students, text="Submit", command=submit_students, bg="#00265D", fg="White", font=("Arial", 13, "bold"))
    button_submit.grid(row=2, column=0, columnspan=2, pady=10)

    for i in range(2):
        tk.Grid.columnconfigure(window_students, i, weight=1)

    for i in range(1):
        tk.Grid.rowconfigure(window_students, i, weight=1)

    window_students.mainloop()

def get_student_grades_window(count_students):
    # Prompts the user to enter grades in a separate window
    students = []

    def submit_student_grades():
        nonlocal students
        name = entry_name.get()
        if name.strip() == "":
            messagebox.showerror("Input Error", "Please enter a name for the student.")
            return
        grades = []
        for i in range(len(courses)):
            if entry_grades[i].get().isnumeric():
                grade=float(entry_grades[i].get())
                # Handle inputs out of range
                if not 0<=grade<=100:
                    messagebox.showerror("Input Error", "Grade should be between 0 and 100.")
                    return
            else:
                # Handle character input
                messagebox.showerror("Input Error", "Character input detected. Grade should be between 0 and 100.")
                return
            grades.append(grade)

        students.append(Student(name, grades))
        if len(students) == count_students:
            window_student_grades.destroy()
            generate_reports(students)
        else:
            entry_name.delete(0, tk.END)
            for entry_grade in entry_grades:
                entry_grade.delete(0, tk.END)

    window_student_grades = tk.Tk()
    window_student_grades.title("Enter Student Grades")
    window_student_grades.geometry("800x450")

    background_image = PhotoImage(file=imgPath)
    """
    background_label = tk.Label(window_student_grades, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    """

    label_name = tk.Label(window_student_grades, text=" Enter name of student:", font=("Arial", 16, "bold"))
    label_name.grid(row=0, column=0, columnspan=2, pady=10)

    entry_name = tk.Entry(window_student_grades, bg="white", fg="black")
    entry_name.grid(row=1, column=0, columnspan=2, pady=10)

    sep1 = ttk.Separator(window_student_grades, orient = 'horizontal')
    sep1.grid(row=2, columnspan=2, sticky="ew")
   
    label_grades = tk.Label(window_student_grades, text="Enter grades for courses:", font=("Arial", 16, "bold"))
    label_grades.grid(row=3, column=0, columnspan=2, pady=10)

    courses = ['Math', 'Science', 'Language', 'Drama', 'Music', 'Biology']
    entry_grades = []
    for i in range(len(courses)):
        label_course = tk.Label(window_student_grades, text=courses[i], fg="black", font=("Arial", 12))
        label_course.grid(row=i + 4, column=0, pady=10)
        entry_grade = tk.Entry(window_student_grades, fg="black")
        entry_grade.grid(row=i + 4, column=1, pady=10)
        entry_grades.append(entry_grade)

    button_submit = tk.Button(window_student_grades, text="Submit", command=submit_student_grades, bg="#00265D", fg="White", font=("Arial", 12, "bold"))
    button_submit.grid(row=len(courses) + 4, column=0, columnspan=2, pady=10)

    for i in range(2):
        tk.Grid.columnconfigure(window_student_grades, i, weight=1)

    for i in range(len(courses) + 4):
        tk.Grid.rowconfigure(window_student_grades, i, weight=1)

    window_student_grades.mainloop()

def assign_school(student):
    if student.gpa >= 90:
        return "School of Engineering"
    elif 80 <= student.gpa < 90:
        return "School of Business"
    elif 70 <= student.gpa < 80:
        return "Law School"
    else:
        return "Not accepted"

def generate_reports(students):
    # Once all student grades are entered, the system will display four reports in a separate window
    engineering_count = 0
    business_count = 0
    law_count = 0
    not_accepted_count = 0
    school_report = []

    for student in students:
        school = assign_school(student)
        if school == "School of Engineering":
            engineering_count += 1
        elif school == "School of Business":
            business_count += 1
        elif school == "Law School":
            law_count += 1
        else:
            not_accepted_count += 1
        school_report.append([student.name, school])

    report_text = ""
    report_text += "\nReport 1: Student Name, School Name\n"
    for student, school in school_report:
        report_text += f"{student}: {school}\n"

    

    report_text += "\nReport 2: Number of accepted students in Humber College showing students distribution per each school.\n"
    report_text += f"School of Engineering: {engineering_count} students\n"
    report_text += f"School of Business: {business_count} students\n"
    report_text += f"Law School: {law_count} students\n"

    report_text += "\nReport 3: Number of students that were not accepted.\n"
    report_text += f"Not accepted: {not_accepted_count}\n"

    total_accepted_gpa = sum(student.gpa for student in students if assign_school(student) != "Not accepted")
    num_accepted = engineering_count + business_count + law_count
    if num_accepted > 0:
        average_gpa = total_accepted_gpa / num_accepted
        report_text += "\nReport 4: Average GPA of accepted students: {:.2f}".format(average_gpa)

    window_reports = tk.Tk()
    window_reports.title("Reports")
    window_reports.geometry("800x450")

    background_image = PhotoImage(file=reportimg)
    background_label = tk.Label(window_reports, image=background_image)
    background_label.grid(row=0, column=0, sticky="nsew")

    label_reports = tk.Label(window_reports, text=report_text, bg="light pink", fg="black", font=("Calibri", 12, "bold"))
    label_reports.grid(row=0, column=0, pady=10)

    window_reports.grid_columnconfigure(0, weight=1)
    window_reports.grid_columnconfigure(1, weight=1)
    window_reports.grid_rowconfigure(0, weight=1)

    window_reports.mainloop()

def main():
    login()

if __name__ == "__main__":
    main()
