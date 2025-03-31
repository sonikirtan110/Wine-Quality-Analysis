# 🍷 Wine Quality Prediction

## 📌 Project Overview
The **Wine Quality Prediction** project aims to analyze the quality of wine (both red and white) based on its chemical composition using **Machine Learning models**. This project includes **data preprocessing, model training, evaluation, and visualization** in **Power BI**.

---
## 📂 Folder Structure
```
Wine-Quality-Prediction
├── data                  # Contains datasets (CSV files)
│   ├── wine-quality-white-and-red.csv
│   ├── images.csv
│
├── notebooks             # Jupyter/Colab notebooks for data exploration & model training
│   ├── WineQuality.ipynb
│
├── src                   # Python scripts for preprocessing & model training
│   ├── app.py
│
├── models                # Saved trained models
│   ├── wine_quality_pipeline.pkl
│   ├── best_wine_model.pkl
│
├── docs                  # Project documentation
│   ├── report.pdf
│
├── images                # Power BI & UI screenshots
│   ├── index.png
│   ├── overview.png
│   ├── analysis.png
│   ├── html_ui.png
│
├── README.md             # Project description
├── requirements.txt      # Required Python libraries
├── LICENSE               # Open-source license
```

---

## 📊 Dataset Information
- **Dataset Source:** [Kaggle - Wine Quality Dataset](https://www.kaggle.com/datasets/ruthgn/wine-quality-data-set-red-white-wine/data)
- **Data Description:** Contains physicochemical tests of **red and white wine samples** along with quality ratings.
- **Target Variable:** `quality` (ranges from 0-10, representing wine quality)
- **Features:**
  - `fixed acidity`
  - `volatile acidity`
  - `citric acid`
  - `type`
  - `residual sugar`
  - `chlorides`
  - `free sulfur dioxide`
  - `total sulfur dioxide`
  - `density`
  - `pH`
  - `sulphates`
  - `alcohol`

---

## 📌 Implementation Steps
### **1️⃣ Data Preprocessing**
- **Handling Missing Values** (if any)
- **Feature Scaling** using StandardScaler
- **Splitting Data** into training and testing sets
- **Encoding Target Variable** (Converting into classification problem)

### **2️⃣ Model Training**
We implemented **5 ML models**:
- **Random Forest** 🌳
- **K-Nearest Neighbors (KNN)** 🔍
- **Decision Tree** 🌿
- **Gradient Boosting** 📈
- **Support Vector Classifier (SVC)** 🏹

### **3️⃣ Model Evaluation**
- **Accuracy Score**
- **Precision, Recall, and F1-Score**
- **Confusion Matrix & ROC Curve**
- **Power BI Visualizations** 📊

### **4️⃣ Power BI Dashboard**
- **Index Page:** Shows dataset summary & wine distribution
- **Overview Page:** Data preprocessing & feature importance
- **Analysis Page:** Model performance comparison

---

## 🔥 Power BI Dashboard (Screenshots)
| Page | Description |
|------|------------|
| ![Index](images/index.png) | Dataset Overview & Distribution |
| ![Overview](images/overview.png) | Feature Engineering & Insights |
| ![Analysis](images/analysis.png) | Model Performance Comparison |

---

## 📌 Code Explanation (src Folder)
| File | Description |
|------|------------|
| `data_preprocessing.py` | Handles data cleaning, missing values, and feature engineering |
| `model_training.py` | Trains the ML models and saves them as `.pkl` files |
| `model_evaluation.py` | Evaluates trained models and generates reports |

---

## 🛠️ Requirements
All required Python libraries are listed in `requirements.txt`.

```
numpy
pandas
scikit-learn
matplotlib
seaborn
jupyterlab
fastapi
uvicorn
powerbiclient
```

Install them using:
```
pip install -r requirements.txt
```

---

## 🚀 GitHub Submission Steps
1. Create a GitHub repository and **push all files**
2. Write meaningful **commit messages**
3. Include **README.md, requirements.txt, and LICENSE**
4. Attach the **Power BI report (PDF/Markdown)**
5. Share the **GitHub repository link** before the deadline.

---

## 📌 Contact Information
📧 Email: [sonikirtan2004@gmail.com](mailto:sonikirtan2004@gmail.com)  
🔗 LinkedIn: [Kirtan Soni](https://www.linkedin.com/in/kirtansoni02/)  

---

## 📜 License
This project is open-source under the **MIT License**.

---

🎯 **Deadline: 08/04/2025**

✅ **If you found this useful, give it a ⭐ on GitHub!** 🚀

