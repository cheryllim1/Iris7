import streamlit as st
import pandas as pd
from tabulate import tabulate
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = pd.read_csv('https://raw.githubusercontent.com/Cher-rylllll/Iris7/main/IRIS.csv')
X = iris.drop('species',axis = 1)
Y = iris['species']

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(['Iris-Setosa','Iris-Versicolor','Iris-Virginica'])

st.subheader('Class labels and their corresponding index number')
st.write(tabulate([['Iris-Setosa'], ['Iris-Versicolor'],['Iris-Virginica']], headers=['FlowerName'], tablefmt='orgtbl'))

st.image("https://miro.medium.com/max/700/1*uo6VfVH87jRjMZWVdwq3Vw.png")

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
