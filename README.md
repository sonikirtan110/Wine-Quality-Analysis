---

# 🍷 Wine Quality Prediction

## 📌 Project Overview  
The **Wine Quality Prediction** project analyzes the quality of wine (red and white) based on its chemical properties using **Machine Learning models**. It includes data preprocessing, model training, evaluation, and **Power BI visualization**.

---

## 📂 Folder Structure
```
Wine-Quality-Prediction
├── Images                # Power BI & UI screenshots
│   ├── index.png
│   ├── overview.png
│   ├── analysis.png
│   ├── html_ui.png
│
├── data                  # Contains datasets (CSV files)
│   ├── wine-quality-white-and-red.csv
│   ├── images.csv
│
├── docs                  # Project documentation
│   ├── report.pdf
│
├── models                # Saved trained models
│   ├── wine_quality_pipeline.pkl
│   ├── best_wine_model.pkl
│
├── notebooks             # Jupyter/Colab notebooks
│   ├── WineQuality.ipynb
│
├── src                   # Python scripts for preprocessing & app
│   ├── app.py
│   └── templates
│       └── index.html
│
├── LICENSE               # Open-source license
├── README.md             # Project description
├── requirements.txt      # Required Python libraries
```

---

## 📊 Dataset Information
- **Source:** [Kaggle - Wine Quality Dataset](https://www.kaggle.com/datasets/ruthgn/wine-quality-data-set-red-white-wine/data)  
- **Target Variable:** `quality` (range: 0–10)  
- **Features:**
  - `fixed acidity`, `volatile acidity`, `citric acid`, `residual sugar`
  - `chlorides`, `free sulfur dioxide`, `total sulfur dioxide`, `density`
  - `pH`, `sulphates`, `alcohol`, `type` (red or white)

---

## 🚀 Implementation Steps

### 1️⃣ Data Preprocessing
- Handle missing values
- Feature scaling using `StandardScaler`
- Train-test split
- Label encoding for classification

### 2️⃣ Model Training
Trained **six ML models**:
- Logistic Regression (LR) 🧪  
- Support Vector Classifier (SVC) 🏹  
- K-Nearest Neighbors (KNN) 🔍  
- Decision Tree (DT) 🌳  
- Random Forest (RF) 🌲  
- Gradient Boosting (GBC) 📈  

### 3️⃣ Model Evaluation
- Accuracy, Precision, Recall, F1-score
- Confusion Matrix, ROC Curve, AUC Score
- Results compared in Power BI

### 4️⃣ Power BI Dashboard
- **Index Page:** Dataset overview & wine distribution  
- **Overview Page:** Preprocessing & feature importance  
- **Analysis Page:** Model comparison & evaluation

---

## 🌐 Live Previews
- 🔗 [Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiOTIwYWYyY2MtOTZiYS00MWUxLWI3NzgtMmFkYTFjMmZmMDZlIiwidCI6ImRhYTU5MmNhLWRlN2ItNGM1NC04ODM2LTkxYTY2OTBmZTE5NyJ9&pageName=dd74d0105ec518cb7330)
- 🔗 [NovyPro Live](https://project.novypro.com/PVlKsk)
- 🔗 [Flask UI (Render)](https://wine-quality-analysis-38rf.onrender.com)

---

## 🖼️ Power BI Dashboard Screenshots

### 📋 Index Page  
![Index](./Images/index.png)

### 📊 Overview Page  
![Overview](./Images/overview.png)

### 📈 Analysis Page  
![Analysis](./Images/analysis.png)

### 🌐 HTML UI  
![HTML UI](./Images/html_ui.png)

---

## 📌 Dashboard Insights

### 📋 Index Page
Provides:
- Wine count by type (red/white)
- Quality distribution
- Summary stats of key features
- Correlation matrix
- Wine type percentages

### 🔍 Overview Page
Covers:
- Preprocessing steps
- Feature importance ranking
- Feature distribution by quality
- Outlier detection
- Data transformation

### 📈 Analysis Page
Includes:
- Model metrics (Accuracy, Precision, Recall, F1-score)
- Confusion matrices
- ROC-AUC curves
- Red vs. white wine performance
- Hyperparameter tuning outcomes

---

## 💻 Source Code: `src/app.py`
- Flask-based web interface for wine quality prediction
- Loads trained ML models
- Accepts red & white wine input
- Returns prediction with confidence
- Handles validation, errors & API requests

---

## 🛠️ Installation

### ✅ Requirements
```
Flask==2.0.3
Werkzeug==2.0.3
gunicorn==20.1.0
joblib==1.2.0
numpy==1.23.5
pandas==1.5.3
scikit-learn==1.4.2
matplotlib==3.6.2
seaborn==0.12.2
```

### 📦 Setup
```bash
# Clone the repository
git clone https://github.com/<your-username>/Wine-Quality-Prediction.git

# Navigate into the project directory
cd Wine-Quality-Prediction

# Install dependencies
pip install -r requirements.txt

# Run locally
python src/app.py

# For deployment
gunicorn --bind 0.0.0.0:$PORT src.app:app
```

---

## 📬 Contact

📧 Email: [sonikirtan2004@gmail.com](mailto:sonikirtan2004@gmail.com)  
🔗 LinkedIn: [Kirtan Soni](https://www.linkedin.com/in/kirtansoni02/)

---

## 📜 License
This project is licensed under the **Apache License**.

---

⭐ **If you found this project useful, please give it a star on GitHub!**  

---
