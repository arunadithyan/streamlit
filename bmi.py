#bmi=weight/height^2
import streamlit as st
st.title("BMI CALCULATOR")
weight = st.number_input("Enter your Weight (Kgs)")

#radio button 
status=st.radio("Select Your Height Format: ",("cms","meters","feet"))
if(status == 'cms'):
    # take height input in centimeters
    height = st.number_input('Centimeters')
 
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")
elif(status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')
 
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")
 
else:
    # take height input in feet
    height = st.number_input('Feet')
 
    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")
if st.button('Calculate BMI'):
    if weight and height:
        # print the BMI INDEX
        st.text("Your BMI Index is {}.".format(bmi))
 
        # give the interpretation of BMI index
        if bmi < 16:
            st.error("You are Extremely Underweight")
        elif 16 <= bmi < 18.5:
            st.warning("You are Underweight")
        elif 18.5 <= bmi < 25:
            st.success("Healthy")
        elif 25 <= bmi < 30:
            st.warning("Overweight")
        elif bmi >= 30:
            st.error("Extremely Overweight")
    else:
        st.warning("Please enter values for weight and height")