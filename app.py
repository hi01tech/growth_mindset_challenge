import streamlit as st

# Function to calculate BMR
def calculate_bmr(weight, height, age, gender):
    # Harris-Benedict equation
    if gender == "Male":
       
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
       
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr

# Function to calculate TDEE 
def calculate_tdee(bmr, activity_level):
    if activity_level == "Sedentary (little or no exercise)":
        tdee = bmr * 1.2
    elif activity_level == "Lightly Active (light exercise/sports 1-3 days/week)":
        tdee = bmr * 1.375
    elif activity_level == "Moderately Active (moderate exercise/sports 3-5 days/week)":
        tdee = bmr * 1.55
    elif activity_level == "Very Active (hard exercise/sports 6-7 days a week)":
        tdee = bmr * 1.725
    else:
        tdee = bmr * 1.9
    return tdee


st.markdown(
    """
    <style>
     .stApp {
            background-color:rgb(154, 224, 175);
            text-align:center;
            color:rgb(190, 212, 170)
        }
    .title {
        font-size: 39px;
        color:rgba(55, 141, 59, 0.97);
        font-weight: bold;
        text-align: center;
        font-family: 'Roboto', sans-serif;
    }
   
    .intro {
        font-size: 18px;
        text-align: center;
        color: #555555;
    }
    .section-header {
        font-size: 30px;
        font-weight: bold;
        color:rgba(55, 141, 59, 0.97);
        margin-top: 30px;
        margin-bottom: 10px;
    }
    .header {
        font-size: 30px;
        font-weight: bold;
        color: #4CAF50;
        margin-top: -13px;
        margin-bottom: 30px;
    }
    .result {
        font-size: 20px;
        color: #333333;
        background-color: #f1f1f1;
        padding: 15px;
        border-radius: 8px;
        margin-top: 10px;
    }
    .goal {
        font-size: 18px;
        font-weight: bold;
        color: #ff5722;
        background-color: #ffe0b2;
        padding: 10px;
        border-radius: 8px;
        margin-top: 15px;
    }
     div.stButton > button {
        color: rgb(214, 27, 27);
        background-color: white;
        border: 2px solid rgb(214, 60, 60);
        padding: 10px 20px;
        font-size: 16px;
        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        background-color: rgb(214, 52, 52);
        color: #ffffff;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.markdown('<div class="title">🔥Calorie Counter & Calculator🔥</div>', unsafe_allow_html=True)

st.markdown('<div class="intro">This app calculates your daily calorie needs or BMR (Basal Metabolic Rate) based on your age, gender, height, weight, and activity level. Fill in the details and get your Total Daily Energy Expenditure (TDEE).</div>', unsafe_allow_html=True)

# Inputs for user details 
st.sidebar.markdown('<div class="header">📊Calculate Here:</div>', unsafe_allow_html=True)
with st.sidebar.container():
    gender = st.selectbox( "  Select your gender", ["Male", "Female"])
    age = st.number_input("Enter your age", min_value=1, max_value=120, value=25)
    weight = st.number_input("Enter your weight (kg)", min_value=1.0, max_value=200.0, value=70.0)
    height = st.number_input("Enter your height (cm)", min_value=50, max_value=250, value=170)
    activity_level = st.selectbox(
        "Select your activity level",
        [
            "Sedentary (little or no exercise)",
            "Lightly Active (light exercise/sports 1-3 days/week)",
            "Moderately Active (moderate exercise/sports 3-5 days/week)",
            "Very Active (hard exercise/sports 6-7 days a week)",
            "Super Active (very hard exercise or physical job)"
        ]
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Initializing BMR and TDEE variables
bmr = 0
tdee = 0

# Calculate BMR and TDEE 
if  st.sidebar.button("Calculate Calories"):
   
    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity_level)

    # Results
    st.markdown(f'<div class="result">Your BMR is: {bmr:.2f} calories/day</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result">Your TDEE is: {tdee:.2f} calories/day</div>', unsafe_allow_html=True)

    # Suggested calorie intake
    st.markdown('<div class="section-header">Suggested Calorie Intake Goals:</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="goal"> For Weight Loss: {tdee - 500:.2f} calories/day (500 calorie deficit)</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="goal"> For Weight Maintenance: {tdee:.2f} calories/day</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="goal"> For Muscle Gain: {tdee + 500:.2f} calories/day (500 calorie surplus)</div>', unsafe_allow_html=True)

    
    

