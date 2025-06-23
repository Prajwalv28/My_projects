# 📊 RealStat: A Chi-Square Driven Decision Analytics

---

##  Overview

**RealStat** is a comprehensive statistical analysis project that applies foundational and advanced probability concepts on two distinct datasets. The goal is to perform real-world data modeling, compute descriptive statistics, evaluate distributional properties, and validate distribution assumptions using goodness-of-fit (Chi-Square) hypothesis testing.

---

## Datasets Overview

### Dataset 1: Salaries of Employees
- **Source**: [Kaggle - Salary Prediction Dataset](https://www.kaggle.com/datasets/rkiattisak/salaly-prediction-for-beginer)
- **Objective**: Analyze compensation structure & determine if salary follows a **Normal distribution**

### Dataset 2: Exit Intervals at Chase Building
- **Source**: Primary data collection (field observation)
- **Collection Tool**: Clockface (digital stopwatch tool)
- **Objective**: Model time intervals between exits & test if it follows an **Exponential distribution**

---

## 📊 Statistical Techniques Employed

### 📌 Descriptive Statistics
- Central Tendency: Mean, Median, Mode
- Dispersion: Range, Variance, Standard Deviation
- Percentile Analysis: Q1, Q2 (Median), Q3, IQR

### 📌 Visual Analysis
- Box-and-Whisker Plots (Outlier detection)
- Frequency Histograms
- Relative & Cumulative Frequency Charts

### 📌 Inferential Statistics
- **Chi-Square Goodness-of-Fit Test**  
  - **Dataset 1**: Tested for **Normal Distribution**
  - **Dataset 2**: Tested for **Exponential Distribution**

---

## Key Results & Interpretations

| Dataset | Distribution Tested | χ² Statistic | Critical Value (α = 0.05) | Result                      |
|---------|---------------------|--------------|----------------------------|-----------------------------|
| Salaries        | Normal                | 12.07         | 7.815                      | ❌ Reject Null – Not Normal |
| Exit Intervals  | Exponential           | 1.69          | 7.815                      | ✅ Fail to Reject – Exponential |

---

## 🛠️ Tools & Methods

- **Excel Functions**: `AVERAGE()`, `VAR.S()`, `STDEV.S()`, `MEDIAN()`, `QUARTILE.INC()`, `NORMDIST()`, `GAMMADIST()`
- **Statistical Plots**: Created using Excel’s statistical charting tools
- **Data Preprocessing**: Manual filtering and transformation of columns for focused analysis

---

## 📈 Insights & Conclusions

- Salaries show **high variability** and are **right-skewed**, with outliers in upper salary brackets (e.g., $250,000).
- Exit intervals exhibit characteristics of an **exponential process**, consistent with **Poisson-like events** such as people leaving a building at random time intervals.
- Distribution fitting using **χ² tests** provided rigorous model validation and helped identify whether underlying assumptions hold true.

---

## 📥 Files Included

- `Realstat.xlsx`: Includes raw data, statistical calculations, visualizations
- `Realstat_report`: Full written report with methodology, analysis, charts, and interpretations

---

## How to Use

1. Open the Excel file to explore:
   - Tab-wise breakdown of descriptive analysis
   - Visual plots and percentile summaries
   - Chi-Square fit test calculations

2. Use the report PDF to:
   - Understand the theoretical background
   - See step-by-step explanation of each method
   - View distribution conclusions and project documentation
  
---

## 🧑‍💻 Author

**Prajwal Venkat Venkatesh**  
📧 prajwalvenkatv@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/prajwal-venkat-v-9654a5180)
