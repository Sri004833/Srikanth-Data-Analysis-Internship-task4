# Data Storytelling & Statistical Validation Report  
## Task 4 – Data Analytics Internship

### Intern Name
[Your Name]

### Organization
ApexPlanet Software Pvt. Ltd.

---

## 1. Introduction
This report presents a complete data storytelling and statistical validation workflow using customer purchase behavior data.  
The goal is to convert analytical findings into a clear business narrative and validate insights using hypothesis testing.

---

## 2. Business Problem
The organization wants to understand:
- Which customer segments generate the most revenue
- Whether customer age has a significant impact on spending behavior
- How insights can support marketing and sales strategies

---

## 3. Dataset Overview
The dataset contains:
- Customer demographics (Age, Gender, City)
- Product information (Product Category)
- Transaction details (Purchase Amount)
- Payment methods

Each record represents a customer purchase transaction.

---

## 4. Analysis Summary
The analysis performed across Tasks 2 and 3 includes:
- Exploratory Data Analysis (EDA)
- KPI-based dashboarding
- Customer segmentation by age
- Revenue and category-level analysis

---

## 5. Key Insights
- Customers aged **36–45** generate the highest revenue
- **Electronics** is the top-performing product category
- **Delhi and Bangalore** are the leading cities by sales
- **UPI and Cash** are the most preferred payment methods

These insights highlight clear patterns in customer behavior.

---

## 6. Hypothesis Testing

### 6.1 Hypothesis Definition
**Null Hypothesis (H₀):**  
There is no significant difference in average purchase amount between customers aged 18–25 and 36–45.

**Alternative Hypothesis (H₁):**  
Customers aged 36–45 spend significantly more than customers aged 18–25.

---

### 6.2 Statistical Method
An **independent two-sample t-test** was conducted to compare average purchase amounts between the two age groups.

---

### 6.3 Results & Interpretation
- The p-value obtained was **less than 0.05**
- This indicates a statistically significant difference
- The null hypothesis is rejected

**Conclusion:**  
Customer age has a significant impact on spending behavior.

---

## 7. Business Recommendations
- Target marketing campaigns toward the **36–45 age group**
- Increase focus on **Electronics** category promotions
- Design city-specific strategies for **Delhi and Bangalore**
- Enhance incentives for digital payments such as UPI

---

## 8. Conclusion
This task demonstrates how data storytelling combined with statistical validation can support confident business decision-making.  
The findings provide a strong foundation for strategic planning and future analytics initiatives.

---

## 9. Tools & Technologies Used
- Python
- Pandas
- SciPy
- Power BI / Tableau
- GitHub

---

**End of Report**
