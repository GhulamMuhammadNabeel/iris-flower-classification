# 🌸 Iris Flower Classifier

A simple **Machine Learning project** that classifies iris flowers into **Setosa, Versicolor, or Virginica** using the **Logistic Regression model**.  
The project includes a **Streamlit web app** for interactive predictions.  

---

## 🔹 Features
- Trains a Logistic Regression model on the famous Iris dataset  
- Saves the trained model (`iris_model.pkl`) using pickle  
- Streamlit frontend for user inputs  
- Predicts the flower type instantly  
- Achieved **100% accuracy** on test data 🎯  

---

## 🔹 Tech Stack
- Python  
- Scikit-learn  
- Pandas  
- Streamlit  
- Matplotlib / Seaborn (for visualization)  

---

## 🔹 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/GhulamMuhammadNabeel/iris-flower-classification.git
   cd iris-flower-classification
   ```
2. **Create venv & install requirements**
    ```bash
    pip install -r requirements.txt 
    ```
3. **Train the model (optional, already included as iris_model.pkl)**
    ```bash
    python model_train.py
    ```
4. **Run Streamlit app**
    ```bash
    streamlit run app.py
    ```

---
## 🔹 Demo

👉 The app will open at: `http://localhost:8501`

---
## ⚡ Learning Outcomes

- With this project, you’ll learn the end-to-end ML pipeline:

- Dataset loading

- Preprocessing & EDA

- Training & evaluation

- Saving & loading ML models

- Deploying with Streamlit