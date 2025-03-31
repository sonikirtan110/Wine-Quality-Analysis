# **Wine Quality Prediction**

## **Project Overview**
Wine Quality Prediction is a machine learning project aimed at analyzing wine characteristics and predicting its quality based on chemical attributes. The project involves data preprocessing, model training, performance evaluation, and visualization using Power BI.

---

## **Project Objectives**
- **Data Preprocessing:** Cleaning and normalizing wine quality datasets.
- **Model Training:** Using various machine learning algorithms to predict wine quality.
- **Performance Evaluation:** Comparing models based on accuracy, precision, recall, and F1-score.
- **Visualization:** Creating an interactive Power BI dashboard for insights.
- **Deployment:** Providing an API endpoint for model inference.

---

## **Dataset Used**
- **Name:** Wine Quality Dataset
- **Source:** UCI Machine Learning Repository
- **Attributes:**
  - Fixed acidity
  - Volatile acidity
  - Citric acid
  - Residual sugar
  - Chlorides
  - Free sulfur dioxide
  - Total sulfur dioxide
  - Density
  - pH
  - Sulphates
  - Alcohol
  - Quality (Target Variable)

---

## **Project Structure**
```
Wine-Quality-Prediction
│── data (Store datasets)
│── notebooks (Jupyter/Colab Notebooks)
│── src (Python scripts for preprocessing and training)
│── models (Saved trained models)
│── docs (Project documentation)
│── images (Power BI & UI images)
│    ├── index.png
│    ├── overview.png
│    ├── analysis.png
│    ├── ui.png
│── README.md (Project overview)
│── requirements.txt (List of required libraries)
│── LICENSE (Open-source license)
```

---

## **Implementation Steps**
### **1. Data Preprocessing**
- Load dataset.
- Handle missing values and outliers.
- Feature scaling and normalization.
- Splitting dataset into training and testing sets.

### **2. Model Training**
- Train models: Logistic Regression, SVM, KNN, Gradient Boosting, XGBoost.
- Use hyperparameter tuning to improve performance.

### **3. Model Evaluation**
- Compute accuracy, precision, recall, and F1-score.
- Compare results to select the best model.

### **4. Power BI Visualization**
- **Index Page:** Overview of dataset statistics.
- **Overview Page:** Graphs showing correlations between attributes and quality.
- **Analysis Page:** Model performance comparison using bar charts, heatmaps, etc.

### **5. API Deployment**
- Use FastAPI to deploy a model prediction API.
- Fetch results using Postman or Render.

---

## **Model Performance**
| Model  | Accuracy (%) | Precision | Recall | F1 Score |
|--------|------------|-----------|--------|----------|
| LR     | 74.37      | 0.748     | 0.743  | 0.743    |
| SVC    | 80.07      | 0.811     | 0.800  | 0.800    |
| KNN    | 82.95      | 0.841     | 0.829  | 0.828    |
| GBC    | 83.23      | 0.833     | 0.832  | 0.832    |
| XGBoost| 88.17      | 0.883     | 0.881  | 0.881    |
| RF     | 79.45      | 0.799     | 0.794  | 0.794    |

---

## **Power BI Dashboard**
1. **Index Page:** Summary of dataset statistics.
2. **Overview Page:** Correlation between wine attributes and quality.
3. **Analysis Page:** Performance comparison of ML models.
4. **HTML UI:** User interface for predictions.

---

## **Installation & Requirements**
To run the project, install the necessary libraries using:
```bash
pip install -r requirements.txt
```
### **Contents of requirements.txt**
```
pandas
numpy
scikit-learn
matplotlib
seaborn
fastapi
uvicorn
powerbiclient
requests
flask
```

---

## **How to Run the Project**
### **Step 1: Clone the Repository**
```bash
git clone https://github.com/yourusername/Wine-Quality-Prediction.git
cd Wine-Quality-Prediction
```

### **Step 2: Run Data Preprocessing & Model Training**
```bash
python src/preprocessing.py
python src/train_model.py
```

### **Step 3: Start API for Predictions**
```bash
uvicorn src.api:app --reload
```

### **Step 4: Test API Using Postman**
- Use endpoint: `http://127.0.0.1:8000/predict`
- Send a **POST request** with wine attributes.

---

## **GitHub Submission Guidelines**
1. Push all files to GitHub with proper commit messages.
2. Include `README.md` explaining the project.
3. Attach a documentation file (`docs/project_report.pdf`).
4. Share the repository link before the deadline.

---

## **Contact Information**
- **Author:** Kirtan Soni
- **Email:** [sonikirtan2004@gmail.com](mailto:sonikirtan2004@gmail.com)
- **LinkedIn:** [linkedin.com/in/kirtansoni02](https://www.linkedin.com/in/kirtansoni02)

---

## **License**
This project is licensed under the MIT License.

