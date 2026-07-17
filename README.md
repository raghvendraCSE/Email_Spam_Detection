# 📧 Email Spam Detection

A Machine Learning web application that predicts whether an email is **Spam** or **Not Spam** using a **Random Forest Classifier**. The application is built with **Python**, **Scikit-learn**, and **Streamlit**, providing a simple and interactive interface for email spam detection.

---

## 🚀 Live Demo

🔗 Add your Streamlit link here after deployment

Example:

https://your-app-name.streamlit.app/

---

## 📌 Project Overview

This project analyzes email characteristics and predicts whether an email is spam based on several extracted features.

The model was trained using a **Random Forest Classifier** with hyperparameter tuning using **GridSearchCV** to improve prediction performance.

---

## ✨ Features

- 📧 Predict whether an email is Spam or Not Spam
- 📝 Enter Email Subject and Email Body
- 📎 Attachment option
- 🤖 Machine Learning Prediction
- 📊 Confidence Score
- 🎨 Clean and Responsive Streamlit Interface

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

---

## 📂 Dataset Features

The model uses the following features:

- Subject
- Email Length
- Number of Links
- Number of Special Characters
- Number of Capital Words
- Has Attachment

Target Variable:

- Spam
  - 0 → Not Spam
  - 1 → Spam

---

## 🤖 Machine Learning Model

Algorithm Used:

- Random Forest Classifier

Hyperparameter Tuning:

- GridSearchCV

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score

---

## 📁 Project Structure

```
EMAIL_SPAM_DETECTION/
│
├── app.py
├── spam_model.pkl
├── requirements.txt
├── README.md
├── Email_Spam_Detection.ipynb
├── email_spam_detection.csv
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YourUsername/Email-Spam-Detection.git
```

Move into the project folder

```bash
cd Email-Spam-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 💻 Screenshots

### Home Page

_Add a screenshot here_

### Prediction Result

_Add a screenshot here_

---

## 📈 Future Improvements

- NLP-based spam detection using TF-IDF
- Email body analysis
- Deep Learning models
- Multiple language support
- Explainable AI predictions

---

## 👨‍💻 Author

**Raghavendra Nath Chaturvedi**

GitHub: https://github.com/YourUsername

LinkedIn: https://www.linkedin.com/in/raghavendra-nath-chaturvedi-617830302/

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.
