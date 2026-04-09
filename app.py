import streamlit as st

# Title
st.title("Student Marks Analyzer")

# Input fields
name = st.text_input("Enter Student Name")

maths = st.number_input("Maths Marks", 0, 100)
science = st.number_input("Science Marks", 0, 100)
english = st.number_input("English Marks", 0, 100)
hindi = st.number_input("Hindi Marks", 0, 100)
marathi = st.number_input("Marathi Marks", 0, 100)
sst = st.number_input("SST Marks", 0, 100)


# Button
if st.button("Calculate Result"):

    total = maths + science + english + hindi + marathi + sst
    percentage = total / 6

    # Grade logic
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 36:
        grade = "D"
    else:
        grade = "Fail"

    # Output
    st.subheader("Result")
    st.write(f"Name: {name}")
    st.write(f"Total Marks: {total}")
    st.write(f"Percentage: {percentage:.2f}%")
    st.write(f"Grade: {grade}")