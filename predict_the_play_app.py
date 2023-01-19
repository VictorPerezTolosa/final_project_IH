import xgboost as xgb
import streamlit as st
import sklearn
import pandas as pd

# load the regression model that we created
model = xgb.XGBClassifier()
model.load_model("predict_a_play_model.json")

# caching the model for faster loading
@st.cache

# Prediction function
def predict(quarter, drive_number, scoreboard, down, distance, field, hash, formation, motion, box, personnel, rb_position, wr_field_side, wr_boundary_side, defense_front, defense_rush, defense_cover_type):

    # defining 'quarter'
    if quarter == "1st qtr":
        quarter = 1
    elif quarter == "2nd qtr":
        quarter = 2
    elif quarter == "3rd qtr":
        quarter = 3
    elif quarter == "4th qtr":
        quarter = 4

    # defining 'scoreboard'
    if scoreboard == "Tying":
        scoreboard = 0
    elif scoreboard == "Winning":
        scoreboard = 1
    elif scoreboard == "Trailing":
        scoreboard = 2

    # defining 'down'
    if down == "1st down":
        down = 1
    elif down == "2nd down":
        down = 2
    elif down == "3rd down":
        down = 3
    elif down == "4th down":
        down = 4

    # defining 'distance'
    if distance == "Short (4 yds or less)":
        distance = 0
    elif distance == "Medium (between 5 and 10 yds)":
        distance = 1
    elif distance == "Long (more than 10 yds)":
        distance = 2
    
    # defining 'field'
    if field == "Opponent field":
        field = 0
    elif field == "Own field":
        field = 1
    
    # defining 'hash'
    if hash == "Left hash":
        hash = 0
    elif hash == "Middle of the field":
        hash = 1
    elif hash == "Right hash":
        hash = 2
    
    # defining 'formation'
    if formation == "Trips":
        formation = 0
    elif formation == "Gun":
        formation = 1
    elif formation == "Empty":
        formation = 2
    elif formation == "Bunch Close":
        formation = 3
    elif formation == "Gun Power":
        formation = 4
    elif formation == "Wing Trips Strong":
        formation = 5
    elif formation == "Wing Close":
        formation = 6
    elif formation == "Pro Gun":
        formation = 7
    elif formation == "Pistol":
        formation = 8
    elif formation == "Bunch":
        formation = 9
    elif formation == "Wing":
        formation = 10
    elif formation == "Ace Wing":
        formation = 11
    
    # defining 'motion'
    if motion == "No":
        motion = 0
    elif motion == "Yes":
        motion = 1
    
    # defining 'personnel'
    if personnel == "Empty personnel":
        personnel = 0
    elif personnel == "10 personnel":
        personnel = 1
    elif personnel == "11 personnel":
        personnel = 2
    elif personnel == "12 personnel":
        personnel = 3
    elif personnel == "20 personnel":
        personnel = 4
    
    # defining 'rb_position'
    if rb_position == "No RB":
        rb_position = 0
    elif rb_position == "Next to the QB, field side":
        rb_position = 1
    elif rb_position == "Next to the QB, boundary side":
        rb_position = 2
    elif rb_position == "Symmetrical position":
        rb_position = 3
    
    # defining 'defense_cover_type'
    if defense_cover_type == "Zone coverage":
        defense_cover_type = 0
    elif defense_cover_type == "Mix coverage":
        defense_cover_type = 1
    elif defense_cover_type == "Man to Man coverage":
        defense_cover_type = 2
    
    prediction = model.predict(pd.DataFrame([[quarter, drive_number, scoreboard, down, distance, field, hash, formation, motion, box, personnel, rb_position, wr_field_side, wr_boundary_side, defense_front, defense_rush, defense_cover_type]], columns = ['quarter', 'drive_number', 'scoreboard', 'down', 'distance', 'field', 'hash', 'formation', 'motion', 'box', 'personnel', 'rb_position', 'wr_field_side', 'wr_boundary_side', 'defense_front', 'defense_rush', 'defense_cover_type']))
    return prediction


st.title("Predict the next play")
st.image("""https://static.clubs.nfl.com/image/private/t_editorial_landscape_12_desktop/f_auto/cowboys/qrroz78khavbfnuwaq17.jpg""")
st.header("Fill in the fields with the game situation and the characteristics of their offense:")
quarter =st.selectbox("Quarter:", ["1st qtr", "2nd qtr", "3rd qtr", "4th qtr"])
drive_number =st.selectbox("Number of their drive:", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
scoreboard =st.selectbox("Are they winning, trailing or tying?", ["Winning", "Trailing", "Tying"])
down =st.selectbox("Down:", ["1st down", "2nd down", "3rd down", "4th down"])
distance =st.selectbox("Distance:", ["Short (4 yds or less)", "Medium (between 5 and 10 yds)", "Long (more than 10 yds)"])
field =st.selectbox("Are they on their own field or the opponent field?", ["Opponent field", "Own field"])
hash =st.selectbox("Hash mark:", ["Left hash", "Middle of the field", "Right hash"])
formation =st.selectbox("Offensive formation they are using:", ["Trips", "Gun", "Empty", "Bunch Close", "Gun Power", "Wing Trips Strong", "Wing Close", "Pro Gun", "Pistol", "Bunch", "Wing", "Ace Wing"])
motion =st.selectbox("Is there a motion?", ["No", "Yes"])
box =st.selectbox("How many players are in the box?", [6, 7, 8, 9])
personnel =st.selectbox("Offensive personnel:", ["Empty personnel", "10 personnel", "11 personnel", "12 personnel", "20 personnel"])
rb_position =st.selectbox("Runningback starting position:", ["No RB", "Next to the QB, field side", "Next to the QB, boundary side", "Symmetrical position"])
wr_field_side =st.selectbox("How many WR are on the field side?", [1, 2, 3])
wr_boundary_side =st.selectbox("How many WR are on the boundary side?", [1, 2, 3])
defense_front =st.selectbox("Defensive front they expect:", [33, 34, 42, 52])
defense_rush =st.selectbox("Defensive rush they expect:", [3, 4, 5, 6])
defense_cover_type =st.selectbox("Defensive coverage they expect:", ["Zone coverage", "Mix coverage", "Man to Man coverage"])

if st.button("Predict the next play"):
    play = predict(quarter, drive_number, scoreboard, down, distance, field, hash, formation, motion, box, personnel, rb_position, wr_field_side, wr_boundary_side, defense_front, defense_rush, defense_cover_type)
    if play == 0:
        st.success("They are going to PASS the ball")
    else:
        st.success("They are going to RUN the ball")
