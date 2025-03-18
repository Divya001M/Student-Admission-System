# 🎓 Student Admission System  

A **Python-based GUI system** that automates **student admissions and school assignments** based on GPA calculations. Built using **Tkinter**, this system securely collects student details, processes their grades, and assigns them to schools based on predefined criteria.  

## 📌 Features  

✅ **Secure Login System** 🔐  
   - Requires users to enter a **strong password** before accessing the system  
   - Enforces password constraints (min 10 characters, uppercase, numbers, special characters)  
   - Limits **login attempts** to **three tries** before exiting  

✅ **Student Data Entry 🏫**  
   - Users enter the **number of students** (1–50 limit)  
   - Collects **student names and grades** for six subjects  
   - Validates that **grades are numeric** and between **0–100**  

✅ **Automatic GPA Calculation 📊**  
   - Computes **weighted GPA** based on subject credit hours  
   - Assigns students to **schools** based on GPA:  
     - **≥ 90%** → School of Engineering 🏗️  
     - **80–89%** → School of Business 📈  
     - **70–79%** → Law School ⚖️  
     - **Below 70%** → Not Accepted ❌  

✅ **Reports & Insights 📄**  
   - Displays **4 reports** summarizing admission results:  
     1. **Student Name & Assigned School**  
     2. **Number of students in each school**  
     3. **Number of students not accepted**  
     4. **Average GPA of accepted students**  

---

## 🛠️ Tech Stack  

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-lightgrey?style=for-the-badge)  

---


