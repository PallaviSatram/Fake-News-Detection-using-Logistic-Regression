# Fake News Detection using Logistic Regression

This project focuses on building a machine learning model to classify news articles as *real* or *fake* using Logistic Regression. The system processes text data with techniques like tokenization, stopword removal, and TF-IDF vectorization to extract meaningful features before training the model.  
The goal of this project is to explore Natural Language Processing (NLP) and machine learning concepts applied to misinformation detection.

🚀 **Status:** Model training completed 

## 📌 Overview
This project focuses on detecting fake news articles using a **Logistic Regression** model.  
The system leverages **Natural Language Processing (NLP)** techniques to preprocess textual data and classify news articles as **real** or **fake** based on their content.

The main objective is to build a reliable ML model that can identify misinformation efficiently — serving as a foundational step toward developing a full-fledged fake news detection application.

---

## 🎯 Objectives
- Preprocess raw text data for analysis  
- Extract relevant features using **TF-IDF Vectorization**  
- Train a **Logistic Regression** model for binary classification  
- Evaluate the model’s accuracy and performance using standard metrics  

---

## 🧠 Machine Learning Workflow
1. **Data Collection:**  
   Used a labeled dataset of real and fake news articles.  
   
2. **Data Preprocessing:**  
   - Removed null values and duplicates  
   - Cleaned text (lowercasing, punctuation removal, stopword removal)  
   - Tokenization  
   - TF-IDF vectorization for feature extraction  

3. **Model Training:**  
   - Algorithm: Logistic Regression  
   - Libraries: scikit-learn, pandas, numpy  

4. **Evaluation Metrics:**  
   - Accuracy Score   

---

## 🧩 Technologies Used
- **Python 3**  
- **Scikit-learn** – for ML model building  
- **Pandas & NumPy** – for data manipulation  
- **Matplotlib / Seaborn** – for visualization (if used)  
- **NLP Tools** – for text cleaning and vectorization  

---

## 📊 Results
- Achieved high 100% accuracy in distinguishing between real and fake news articles.  
- The Logistic Regression model demonstrated strong baseline performance for text classification tasks.  

---

## 🚀 Future Enhancements
- Implement deep learning models (e.g., LSTM, BERT) for better accuracy  
- Create a web interface using **Flask** or **Django** for real-time detection  
- Integrate an API for easier model deployment  
- Add dataset visualization dashboard  

---

## 🧾 Project Structure
Fake-News-Detection/
│
├── data/
│ └── train.csv
│
├── notebooks/
│ └── fake_news_model.ipynb
│
├── README.md
└── fake_news_detection.py


## 🧮 How to Run
1. Clone this repository  
   git clone https://github.com/<your-username>/Fake-News-Detection.git
   cd Fake-News-Detection
2. Install dependencies
   pip install -r requirements.txt
3. Run the model
   python fake_news_detection.py

Copy code
python fake_news_detection.py
