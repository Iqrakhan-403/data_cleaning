# Task 1: Data Cleaning and Preprocessing

## 📌 Objective

Clean and prepare a raw dataset by handling missing values, removing duplicates, standardizing columns, fixing data types, and ensuring the dataset is ready for analysis or modeling.

---

## 📂 Dataset

**Source:** [Customer Personality Analysis on Kaggle](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)

- Raw dataset used from the above source.
- Final cleaned dataset generated after preprocessing.

---

## ⚙️ Tools Used

- Python 3.x
- Pandas

---

## 🧹 Steps Performed

1. Loaded the raw dataset using Pandas.
2. Identified and removed rows with missing values using `.dropna()`.
3. Removed duplicate records using `.drop_duplicates()`.
4. Standardized column names (lowercase, underscores instead of spaces).
5. Converted the customer date column to proper `datetime` format.
6. Converted income-related columns to appropriate numeric types.
7. Created a new age-related column from the birth year.
8. Saved the cleaned dataset for further analysis.

---

## 🧪 How to Run

1. Make sure the raw dataset file is in the same folder as the script.
2. Run the cleaning script:

```bash
python data_cleaning.py
