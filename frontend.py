import streamlit as st
import pickle
from sklearn.datasets import load_iris

# Load saved model
with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

iris = load_iris()

# Streamlit UI
st.title("🌸 Iris Flower Classifier")

sepal_length = st.number_input("Sepal length (cm)", min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.number_input("Sepal width (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input("Petal length (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.number_input("Petal width (cm)", min_value=0.0, max_value=10.0, step=0.1)

if st.button("Predict"):
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(input_data)[0]
    flower_name = iris.target_names[prediction]
    st.success(f"🌼 Predicted Flower: {flower_name}")
