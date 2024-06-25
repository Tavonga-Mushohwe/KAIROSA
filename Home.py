import streamlit as st
import pickle 
import sklearn 
import pandas as pd
import numpy as np

df = pd.read_csv("card_transdata.csv")
from sklearn.model_selection import train_test_split
# iloc : takes a slice of the dataframe
X = df.iloc[: , :-1]
y = df.iloc[: , -1]

X_train, X_test , y_train , y_test = train_test_split(X,y, random_state=42)
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
dtc.fit(X=X_train , y= y_train)

st.title("Kairosa - Fraud detection Machine Learning Model 🤖")

st.write("Enter The related information \n")
distance_from_home = st.number_input("Distance from Home")
distance_from_last_transaction = st.number_input("Distance from Last transaction")
ratio_to_median_purchase_price = st.number_input("ratio_to_median_purchase_price")
repeat_retailer = st.selectbox("Have you used this retailer before ?",['Yes','No'])
used_chip = st.selectbox("Have you used this card before ?",["Yes","No"])
used_pin_number = st.selectbox("Is the pin number used for other cards ?",["Yes","No"])
online_order = st.selectbox("Was it an online order or physical payment ?",["Yes, it was an online payment","No, physical payment"])
submit = st.button(label="Submit",)



if repeat_retailer =="Yes" :
    repeat_retailer = 1
else:
    repeat_retailer = 0


if used_chip ==" Yes":
    used_chip = 1
else:
    used_chip = 0

if used_pin_number == "Yes":
    used_pin_number = 1
else:
    used_pin_number = 0

if online_order == "Yes":
    online_order = 1
else:
    online_order = 0


def predictions(user_input:list): 
    result = dtc.predict([user_input])
    return result

user_input = [distance_from_home,distance_from_last_transaction,ratio_to_median_purchase_price,repeat_retailer,used_chip,used_pin_number,online_order]


if submit :
    result = predictions(user_input)
    if result == 0.0 :
        st.warning("Strongly advise not to transfer any money on this site",icon="⚠️")
    else:
        st.warning("Site is trusted, can send money ", icon="👍")


st.write("NOTE :\n This process is supposed to be automatic .I plan to use open API to get the data . For now this is the currently running working model . Enjoy 😊 ")