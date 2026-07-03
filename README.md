# 🏡 California Housing Price Prediction Model

An interactive data science project that predicts property values using machine learning algorithms trained on California housing metrics.

---

## 📊 Project Overview
This project analyzes key economic and geographical features—such as median income, house age, and average rooms—to build a predictive system for real estate valuation. 

## ⚙️ How It Works
1. **Data Exploration:** Analyzing relationships using scatter plots (e.g., Median Income vs. House Value).
2. **Baseline Model:** Built a simple Linear Regression model using only income data.
3. **Upgraded Model:** Enhanced accuracy by introducing multi-variable inputs (Age, Rooms, Income).

## 🏆 Model Results
We measured accuracy using **Mean Squared Error (MSE)**, where a lower score means closer, more accurate price predictions:

| Model Version | Features Used | Performance (MSE) |
| :--- | :--- | :--- |
| **Baseline Model** | Median Income only | `0.7091` |
| **Upgraded Model** | Income + Age + Rooms | `0.6589` 🚀 *(Better Accuracy)* |

---
*Developed inside Google Colab using Python, Scikit-Learn, Pandas, and Seaborn.*
