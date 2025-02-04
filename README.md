# Brain_Stoke_Prediction
"This project builds a Stroke Prediction API using Streamlit, leveraging patient data (age, BMI, glucose levels, lifestyle factors) to predict stroke risk scores. 🚀"

<img src="">

# 🏥 Stroke Prediction API  

## 📌 Overview  
This project builds a **Machine Learning model** to predict stroke risk based on medical and lifestyle factors.  
The model is deployed as an **interactive API using Streamlit**.  

---

## 📂 Dataset Overview  
The dataset includes various features that influence stroke risk: 

📅 Age
👨‍⚕️ Gender (Male, Female, Other)
💼 Work Type (Private, Govt, Self-employed, etc.)
🩸 Average Glucose Level
⚖️ BMI (Body Mass Index)
🏃 Physical Activity Level
🥗 Dietary Habits
🍷 Alcohol Consumption (Yes/No)
😰 Chronic Stress (Yes/No)
😴 Sleep Hours
💓 Stroke Risk Score (Target Variable)


| Feature | Description |
|---------|------------|
| `age` | Age of the patient 📅 |
| `gender` | Gender (Male, Female, Other) 👨‍⚕️ |
| `hypertension` | 1 = Yes, 0 = No 💓 |
| `heart_disease` | 1 = Yes, 0 = No 💔 |
| `ever_married` | Marital Status (Yes/No) 💍 |
| `work_type` | Type of employment 💼 |
| `Residence_type` | Urban/Rural 🏡 |
| `avg_glucose_level` | Average blood glucose level 🩸 |
| `bmi` | Body Mass Index ⚖️ |
| `smoking_status` | Smoking habits 🚬 |
| `stroke` | Target variable (1 = Stroke, 0 = No Stroke) ⚠️ |

---

## 🏗 Tech Stack  
- **Python** 🐍 - Core programming language  
- **Pandas & NumPy** 📊 - Data processing  
- **Scikit-learn** 🤖 - Machine learning model  
- **Streamlit** 🎨 - API deployment  
- **Joblib** 🔁 - Model saving/loading  

---

## 🔬 Data Preprocessing  
1. **Handling Missing Values** 🛠️  
   - Fill missing `bmi` values with median.  
2. **Encoding Categorical Data** 🔤  
   - Convert `gender`, `work_type`, `Residence_type`, `smoking_status` into numeric values.  
3. **Feature Scaling** 📏  
   - Standardize `age`, `avg_glucose_level`, and `bmi`.  
4. **Train-Test Split** 🎯  
   - Split dataset into **80% training** and **20% testing**.  

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
📌 Features
✅ User-friendly Streamlit web app
✅ Predicts stroke risk score based on medical & lifestyle data
✅ Interactive UI for easy input
✅ Fast & scalable API
