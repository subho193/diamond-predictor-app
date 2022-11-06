import xgboost as xgb
from xgboost import XGBRegressor
import streamlit as st
import pandas as pd

#Loding the Regression model we created
model=xgb.XGBRegressor()
model.load_model('xgb_model.json')

#caching the model for faster loading
@st.cache
def predict(carat,cut,color,clarity,depth,table,x,y,z):
    #predicting the price of the carat
    if cut=='Fair':
        cut=0
    elif cut=='Good':
        cut=1
    elif cut=='Very Good':
        cut=2
    elif cut=='Premium':
        cut=3
    elif cut=='Ideal':
        cut=4
    
    if color == 'J':
        color = 0
    elif color == 'I':
        color = 1
    elif color == 'H':
        color = 2
    elif color == 'G':
        color = 3
    elif color == 'F':
        color = 4
    elif color == 'E':
        color = 5
    elif color == 'D':
        color = 6
    
    if clarity == 'I1':
        clarity = 0
    elif clarity == 'SI2':
        clarity = 1
    elif clarity == 'SI1':
        clarity = 2
    elif clarity == 'VS2':
        clarity = 3
    elif clarity == 'VS1':
        clarity = 4
    elif clarity == 'VVS2':
        clarity = 5
    elif clarity == 'VVS1':
        clarity = 6
    elif clarity == 'IF':
        clarity = 7
    prediction=model.predict(pd.DataFrame([[carat, cut, color, clarity, depth, table, x, y, z]],columns=['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']))
    return prediction

#Let's start building the app:
st.title('Diamond_Price_Predictor_SD')
st.image('https://thumbs.dreamstime.com/b/diamond-3342797.jpg')
st.header('Enter the characteristics of the diamond : ')

#Let's define user inputs:
carat=st.number_input('Carat Weight: ',min_value=0.1,max_value=10.0,value=1.0)
cut=st.selectbox('Color Rating',['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
color = st.selectbox('Color Rating:', ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
clarity = st.selectbox('Clarity Rating:', ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
depth = st.number_input('Diamond Depth Percentage:', min_value=0.1, max_value=100.0, value=1.0)
table = st.number_input('Diamond Table Percentage:', min_value=0.1, max_value=100.0, value=1.0)
x = st.number_input('Diamond Length (X) in mm:', min_value=0.1, max_value=100.0, value=1.0)
y = st.number_input('Diamond Width (Y) in mm:', min_value=0.1, max_value=100.0, value=1.0)
z = st.number_input('Diamond Height (Z) in mm:', min_value=0.1, max_value=100.0, value=1.0)


#Let's define an input that will call our prediction function:
if st.button('Predict Price'):
    price=predict(carat, cut, color, clarity, depth, table, x, y, z)
    st.success(f'The predicted price of the diamond is ${price[0]:.2f} USD')










    

    