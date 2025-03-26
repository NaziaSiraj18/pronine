import streamlit as st   
import pandas as pd  
import random

st.set_page_config(page_title="Student Data Generator", layout="wide")
st.title("Student CSV File Generator")

names = ["Ameen", "Anum", "Ahmed", "Fariha", "Umair", "Zain", "Bilal", "Mehak", "Faiza"]

students = []
for i in range(1, 16):
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 25),
        "Grade": random.choice(["A", "B", "C", "D", "E", "F"]),  # Fixed this
        "Marks": random.randint(40, 100)
    }
    students.append(student)
    
df = pd.DataFrame(students)  # Fixed this

st.subheader("Generated Students Data")
st.dataframe(df)

csv_file = df.to_csv(index=False).encode('utf-8')  # Fixed this
st.download_button("Download CSV File", csv_file, "students.csv", "text/csv")

st.success("Students Record Generated Successfully!")  

