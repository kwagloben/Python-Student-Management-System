from customtkinter import *
from tkinter import messagebox, StringVar
import matplotlib.pyplot as plt

def Main():
    root = CTk()
    root.title("Student Management System")
    root.iconbitmap("./assets/illustration.ico")
    root._set_appearance_mode("Dark")
    set_default_color_theme("./assets/breeze.json")

    width = 800
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(False, False)

    student_records = {
        "41032564": {
                "full_name": "James Asante",
                "basic_electronics": {
                    "midsem": 16,
                    "exam": 58,
                },
                "electrical_machines": {
                    "midsem": 26,
                    "exam": 63,
                },
                "calculus": {
                    "midsem": 18,
                    "exam": 63,
                },
                "total_marks": {
                    "average": ((16) + (58) + (26) + (63) + (18) + (63)) / 3,
                    "basic_electronics": (16) + (58),
                    "electrical_machines": (26) + (63),
                    "calculus": (18) + (63)
                }
            },
        "40987542": {
                "full_name": "Francisca Owusu",
                "basic_electronics": {
                    "midsem": 12,
                    "exam": 63,
                },
                "electrical_machines": {
                    "midsem": 26,
                    "exam": 59,
                },
                "calculus": {
                    "midsem": 29,
                    "exam": 56,
                },
                "total_marks": {
                    "average": ((12) + (63) + (26) + (59) + (29) + (56)) / 3,
                    "basic_electronics": (12) + (63),
                    "electrical_machines": (26) + (59),
                    "calculus": (29) + (56)
                }
            },
        "40836952": {
                "full_name": "Maxwell Osei",
                "basic_electronics": {
                    "midsem": 27,
                    "exam": 48,
                },
                "electrical_machines": {
                    "midsem": 19,
                    "exam": 63,
                },
                "calculus": {
                    "midsem": 21,
                    "exam": 60,
                },
                "total_marks": {
                    "average": ((27) + (48) + (19) + (63) + (21) + (60)) / 3,
                    "basic_electronics": (27) + (48),
                    "electrical_machines": (19) + (63),
                    "calculus": (21) + (60)
                }
            },
        "41074102": {
                "full_name": "Kwame Mensah",
                "basic_electronics": {
                    "midsem": 19,
                    "exam": 63,
                },
                "electrical_machines": {
                    "midsem": 23,
                    "exam": 48,
                },
                "calculus": {
                    "midsem": 12,
                    "exam": 58,
                },
                "total_marks": {
                    "average": ((19) + (63) + (23) + (48) + (12) + (58)) / 3,
                    "basic_electronics": (19) + (63),
                    "electrical_machines": (23) + (48),
                    "calculus": (12) + (58)
                }
            },
        "40988536": {
                "full_name": "Lily Adjei",
                "basic_electronics": {
                    "midsem": 30,
                    "exam": 69,
                },
                "electrical_machines": {
                    "midsem": 27,
                    "exam": 64,
                },
                "calculus": {
                    "midsem": 24,
                    "exam": 62,
                },
                "total_marks": {
                    "average": ((30) + (69) + (27) + (64) + (24) + (62)) / 3,
                    "basic_electronics": (30) + (69),
                    "electrical_machines": (27) + (64),
                    "calculus": (24) + (62)
                }
            },
    }

    def grade(s_avg):
        if s_avg is None:
            return "N/A"
        elif s_avg >= 80:
            return "A"
        elif s_avg >= 70:
            return "B"
        elif s_avg >= 60:
            return "C"
        elif s_avg >= 50:
            return "D"
        elif s_avg >= 30:
            return "E"
        else:
            return "F"

    def update_students_list():
        students_listbox.configure(state="normal")
        students_listbox.delete("1.0", "end")
        if not student_records:
            students_listbox.insert("end", "No student records.\n")
        else:
            # Sort by average in descending order
            sorted_records = sorted(
                student_records.items(),
                key=lambda item: item[1].get("total_marks", {}).get("average", 0),
                reverse=True
            )
            for sid, data in sorted_records:
                avg = data.get("total_marks", {}).get("average", "N/A")
                students_listbox.insert("end", f"{sid}:     {avg:.2f}   {grade(float(avg))}\n" if isinstance(avg, (int, float)) else f"{sid}: N/A\n")
        students_listbox.configure(state="disabled")

    def view_all_records():
        if not student_records:
            messagebox.showinfo("No Records", "No student records available.")
            return

        be_scores = []
        ee_scores = []
        calc_scores = []
        total_averages = []
        labels = []

        for sid, data in student_records.items():
            labels.append(sid)
            be = data["total_marks"]["basic_electronics"]
            ee = data["total_marks"]["electrical_machines"]
            calc = data["total_marks"]["calculus"]
            avg = data["total_marks"]["average"]
            be_scores.append(be)
            ee_scores.append(ee)
            calc_scores.append(calc)
            total_averages.append(avg)

        fig, axs = plt.subplots(2, 2, figsize=(10, 8))
        fig.suptitle("Student Performance Overview", fontsize=16)

        # Pie chart for Basic Electronics
        axs[0, 0].pie(be_scores, labels=labels, autopct='%1.1f%%', startangle=140)
        axs[0, 0].set_title("Basic Electronics")

        # Pie chart for Electrical Machines
        axs[0, 1].pie(ee_scores, labels=labels, autopct='%1.1f%%', startangle=140)
        axs[0, 1].set_title("Electrical Machines")

        # Pie chart for Calculus
        axs[1, 0].pie(calc_scores, labels=labels, autopct='%1.1f%%', startangle=140)
        axs[1, 0].set_title("Calculus With Analysis")

        # Donut chart for Total Averages
        wedges, texts, autotexts = axs[1, 1].pie(
            total_averages,
            labels=labels,
            autopct='%1.1f%%',
            startangle=140,
            wedgeprops={'width': 0.5}  # Makes it a donut chart
        )
        axs[1, 1].set_title("Overall Performance (Average)")

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()

    def reset_fields():
        id_entry.delete(0, END)
        st_name_entry.delete(0, END)
        be_midsem_entry.delete(0, END)
        be_exam_entry.delete(0, END)
        ee_midsem_entry.delete(0, END)
        ee_exam_entry.delete(0, END)
        calc_midsem_entry.delete(0, END)
        calc_exam_entry.delete(0, END)
        messagebox.showinfo("Reset", "All fields have been reset.")

    def add_record():
        valid = False
        student_id = id_entry.get()
        full_name = st_name_entry.get()
        be_midsem = be_midsem_entry.get()
        be_exam = be_exam_entry.get()
        ee_midsem = ee_midsem_entry.get()
        ee_exam = ee_exam_entry.get()
        calc_midsem = calc_midsem_entry.get()
        calc_exam = calc_exam_entry.get()

        if not student_id or not full_name:
            messagebox.showerror("Error", "Index number and Full name are required.")
            return
        if student_id in student_records:
            messagebox.showerror("Error", "Record with this Index number already exists.")
            return
        try:
            be_midsem = float(be_midsem)
            be_exam = float(be_exam)
            ee_midsem = float(ee_midsem)
            ee_exam = float(ee_exam)
            calc_midsem = float(calc_midsem)
            calc_exam = float(calc_exam)
            valid = True
        except ValueError:
            messagebox.showerror("Error", "Marks must be numeric values.")
            valid = False
            return
        if valid:
            student_data = {
                "full_name": full_name,
                "basic_electronics": {
                    "midsem": be_midsem,
                    "exam": be_exam,
                },
                "electrical_machines": {
                    "midsem": ee_midsem,
                    "exam": ee_exam,
                },
                "calculus": {
                    "midsem": calc_midsem,
                    "exam": calc_exam,
                },
                "total_marks": {
                    "average": ((be_midsem) + (be_exam) + (ee_midsem) + (ee_exam) + (calc_midsem) + (calc_exam)) / 3,
                    "basic_electronics": (be_midsem) + (be_exam),
                    "electrical_machines": (ee_midsem) + (ee_exam),
                    "calculus": (calc_midsem) + (calc_exam)
                }
            }
            student_records[student_id] = student_data
            messagebox.showinfo("Success", "Student record added successfully.")
            # print(f"Record for {full_name} with ID {student_id} added successfully.")
            # print("Student Records:", student_records)
            update_students_list()
            reset_fields()
    
    def search_student():
        query = search_entry.get().strip().lower()
        if not query:
            messagebox.showinfo("Search", "Please enter a student's name to search.")
            return
        found = False
        for sid, data in student_records.items():
            name = data.get("full_name", "").lower()
            if query in name:
                found = True
                avg = data.get("total_marks", {}).get("average", "N/A")
                be = data.get("total_marks", {}).get("basic_electronics", "N/A")
                ee = data.get("total_marks", {}).get("electrical_machines", "N/A")
                calc = data.get("total_marks", {}).get("calculus", "N/A")
                avg_str = f"{avg:.2f}" if isinstance(avg, (int, float)) else "N/A"
                be_str = f"{be:.2f}" if isinstance(be, (int, float)) else "N/A"
                ee_str = f"{ee:.2f}" if isinstance(ee, (int, float)) else "N/A"
                calc_str = f"{calc:.2f}" if isinstance(calc, (int, float)) else "N/A"
                messagebox.showinfo(
                    "Student Found",
                    f"Name: {data['full_name']}     {sid}\n\nBasic Electronics: {be_str}\nElectrical Machines: {ee_str}\nCalculus: {calc_str}\nAverage: {avg_str}   {grade(float(avg))}"
                )
        if not found:
            messagebox.showinfo("Not Found", "No student found with that name.")


    main_frame = CTkFrame(root)
    main_frame.pack(fill=BOTH, expand=True)

    # Side frame and its contents
    side_frame = CTkFrame(main_frame, width=200)
    side_frame.pack(side=LEFT, fill=Y)
    side_label = CTkLabel(side_frame, text="Enrolled Students", font=("Kanit", 16))
    side_label.pack(pady=10, padx=20)

    students_list_var = StringVar()
    students_listbox = CTkTextbox(side_frame, height=300, width=180, font=("Kanit", 14, "bold"), fg_color="transparent")
    students_listbox.pack(padx=10, pady=(0, 10), fill="both", expand=False)
    students_listbox.configure(state="disabled")

    # Middle frame and its contents
    middle_frame = CTkFrame(main_frame, fg_color="transparent")
    middle_frame.pack(side=LEFT, fill=BOTH, expand=True)

    search_frame = CTkFrame(middle_frame, fg_color="transparent")
    search_frame.pack(fill=X, padx=10, pady=(10, 0))
    search_entry = CTkEntry(search_frame, placeholder_text="Search student by name")
    search_entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))
    search_btn = CTkButton(search_frame, text="Search", command=search_student, width=80)
    search_btn.pack(side=LEFT)


    middle_label = CTkLabel(middle_frame, text="Student Details", font=("Kanit", 20, "bold"))
    middle_label.pack(pady=10, padx=10)

    left_form_frame = CTkFrame(middle_frame, fg_color="transparent")
    left_form_frame.pack(side=LEFT, fill=BOTH, expand=True)
    right_form_frame = CTkFrame(middle_frame, fg_color="transparent")
    right_form_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(10, 0))

    id_label = CTkLabel(left_form_frame, text="Index number", font=("Kanit", 14))
    id_label.pack(padx=10, anchor=W)
    id_entry = CTkEntry(left_form_frame, placeholder_text="Enter Student ID")
    id_entry.pack(padx=10, fill=X)

    st_name_label = CTkLabel(right_form_frame, text="Full name", font=("Kanit", 14))
    st_name_label.pack(padx=10, anchor=W)
    st_name_entry = CTkEntry(right_form_frame, placeholder_text="Enter Student's Full name")
    st_name_entry.pack(padx=10, fill=X)

    be_label = CTkLabel(left_form_frame, text="Basic Electronics", font=("Kanit", 18))
    be_label.pack(pady=(25, 0), padx=10, anchor=W)

    be_midsem_label = CTkLabel(left_form_frame, text="Midsem(30%)", font=("Kanit", 14))
    be_midsem_label.pack(padx=10, anchor=W)
    be_midsem_entry = CTkEntry(left_form_frame, placeholder_text="Enter Midsem Marks")
    be_midsem_entry.pack(padx=10, fill=X)
    be_exam_label = CTkLabel(left_form_frame, text="End Of Sem(70%)", font=("Kanit", 14))
    be_exam_label.pack(padx=10, anchor=W)
    be_exam_entry = CTkEntry(left_form_frame, placeholder_text="Enter End of Sem Marks")
    be_exam_entry.pack(padx=10, fill=X)

    ee_label = CTkLabel(right_form_frame, text="Electrical Machines", font=("Kanit", 18))
    ee_label.pack(pady=(25, 0), padx=10, anchor=W)

    ee_midsem_label = CTkLabel(right_form_frame, text="Midsem(30%)", font=("Kanit", 14))
    ee_midsem_label.pack(padx=10, anchor=W)
    ee_midsem_entry = CTkEntry(right_form_frame, placeholder_text="Enter Midsem Marks")
    ee_midsem_entry.pack(padx=10, fill=X)
    ee_exam_label = CTkLabel(right_form_frame, text="End Of Sem(70%)", font=("Kanit", 14))
    ee_exam_label.pack(padx=10, anchor=W)
    ee_exam_entry = CTkEntry(right_form_frame, placeholder_text="Enter End of Sem Marks")
    ee_exam_entry.pack(padx=10, fill=X)

    calc_label = CTkLabel(left_form_frame, text="Calculus With Analysis", font=("Kanit", 18))
    calc_label.pack(pady=(25, 0), padx=10, anchor=W)

    calc_midsem_label = CTkLabel(left_form_frame, text="Midsem(30%)", font=("Kanit", 14))
    calc_midsem_label.pack(padx=10, anchor=W)
    calc_midsem_entry = CTkEntry(left_form_frame, placeholder_text="Enter Midsem Marks")
    calc_midsem_entry.pack(padx=10, fill=X)
    calc_exam_label = CTkLabel(left_form_frame, text="End Of Sem(70%)", font=("Kanit", 14))
    calc_exam_label.pack(padx=10, anchor=W)
    calc_exam_entry = CTkEntry(left_form_frame, placeholder_text="Enter End of Sem Marks")
    calc_exam_entry.pack(padx=10, fill=X)

    reset_btn = CTkButton(right_form_frame, text="Reset All", height=35, fg_color="#e75d5d", hover_color="#d32f2f" , command=reset_fields)
    reset_btn.pack(pady=(45, 0), padx=10, fill=X)

    add_btn = CTkButton(right_form_frame, text="Add Record", height=35, fg_color="#27ae60", hover_color="#219150", command=add_record)
    add_btn.pack(pady=15, padx=10, fill=X)

    view_all_btn = CTkButton(right_form_frame, text="View All Records", height=35, command=view_all_records, fg_color="#3498db", hover_color="#2980b9")
    view_all_btn.pack(padx=10, fill=X)

    update_students_list()
    root.mainloop()