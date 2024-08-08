# Predicting the Ten-Year Risk of Developing Heart Disease Using Machine Learning

## Introduction

**Coronary Heart Disease (CHD)** remains a critical global health concern, responsible for a substantial portion of cardiovascular-related morbidity and mortality. Identifying individuals at risk of developing CHD is paramount for timely intervention and prevention efforts. This project aims to harness the power of data analysis and predictive modeling to better understand the factors associated with Ten-Year CHD risk and build a reliable predictive model.

## Background

CHD is a complex, multifactorial condition influenced by a myriad of genetic, lifestyle, and medical factors. Understanding the interplay between these factors can significantly improve our ability to identify individuals at heightened risk. This project utilizes a comprehensive dataset encompassing various demographic, medical, and lifestyle-related variables.

## Dataset Description

The dataset contains information on individuals, including features such as age, education level, gender, smoking status, and various health-related measurements (e.g., cholesterol levels, blood pressure, BMI, and glucose levels). The target variable, **"TenYearCHD"**, indicates whether an individual is at risk of developing CHD within the next ten years (1 for at risk, 0 for not at risk).

## Objectives

- **Data Exploration:** Conduct a thorough exploration of the dataset to understand its structure, identify missing values, and gain insights into the distribution of key variables.
- **Feature Analysis:** Analyze the dataset's features to determine their suitability for predicting Ten-Year CHD risk.
- **Dependency Analysis:** Employ statistical tests, including the Chi-squared test for categorical features and Mann-Whitney U test for continuous features, to assess the dependency of each feature on the Ten-Year CHD target variable.
- **Data Preprocessing:** Prepare the dataset for modeling by handling missing values, encoding categorical variables, and scaling or normalizing numeric features.
- **Model Building:** Develop predictive models using machine learning algorithms to predict Ten-Year CHD risk based on the selected features.
- **Model Evaluation:** Assess model performance using metrics such as accuracy, precision, recall, and ROC curve.
- **Interpretation:** Identify the most influential factors contributing to Ten-Year CHD risk.

## Conclusion

In this healthcare-focused project, we leveraged machine learning to extract meaningful insights from medical data. The Random Forest Classifier (RFC) emerged as the top performer, achieving an accuracy of 87.91%. This demonstrates RFC’s effectiveness in identifying health outcomes, which is crucial for improving patient care and optimizing healthcare resources. 

Statistical analyses, including Chi-square and Mann-Whitney U tests, ensured the reliability of our findings and provided deeper insights into the dataset. This project underscores the transformative potential of machine learning in healthcare and highlights its role in driving innovation and enhancing decision-making.

## Web Application

A Flask-based web application is developed to allow users to input health data and receive CHD predictions. The application includes the following pages:

- **Home.html:** Introduction and overview.
- **About.html:** Details about the project and its objectives.
- **Tips.html:** Health tips related to heart disease prevention.
- **Contact.html:** Contact information and feedback form.
- **Prediction.html:** Interface for inputting data and viewing predictions.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask Application:**
   ```bash
   python app.py
   ```

4. **Access the Web Application:**
   Open your browser and go to `http://localhost:5000`.

---
