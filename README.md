NUTRITION ANALYSIS PROJECT
   #OBESITY AND MALNUTRITION USING WHO DATASET

1. Project Overview
This project analyzes global obesity and malnutrition trends using public WHO (World Health Organization) datasets.

The main objective is to clean, transform, analyze, store, and visualize the data using Python, SQL, Streamlit, and Power BI.

Key Features:
- Data extraction from WHO APIs  
- Data cleaning & feature engineering  
- Exploratory Data Analysis (EDA)  
- SQL database integration (TiDB/MySQL)  
- Query-based analysis  
- Interactive Streamlit dashboard  
- Power BI dashboard  
- Cloud deployment  

2. Dataset
- Source: WHO (World Health Organization)  
- Data Range: 2012 – 2022  
- Includes:
  - Country  
  - Gender  
  - Age groups  
  - Obesity & Malnutrition indicators  

3. Data Cleaning & Feature Engineering

 Key Steps:
 - Renamed columns for consistency  
 - Standardized gender values (Male, Female, Both)  
 - Converted ISO-3 country codes to country names using `pycountry`  
 - Handled WHO region codes  
 - Filtered relevant years (2012–2022)  

New Features Created:
  - `Age_Group`  
  - `CI_Width`  
  - `Obesity_Level`  
  - `Malnutrition_Level`  

4. Exploratory Data Analysis (EDA)

EDA was performed using:
  - Pandas  
  - Matplotlib  
  - Seaborn  

Key Analysis:
  - Data distribution  
  - Missing value analysis  
  - Year-wise trends  
  - Region-wise comparison  
  - Obesity vs Malnutrition patterns  
  - Gender & Age group insights  

5. Database Integration

   - SQL Engine: **TiDB Cloud (MySQL Compatible)**  
   - Database: `nutrition`
Tables:
   - `obesity`  
   - `malnutrition`  

Optimization:
   - Batch inserts using `executemany()` for better performance  

6. SQL Query Analysis

Total Queries: 25
   - Obesity Analysis → 10 queries  
   - Malnutrition Analysis → 10 queries  
   - Combined Analysis → 5 queries
 
7. Streamlit Dashboard

  An interactive dashboard was developed using Streamlit:

Features:
  - Dropdown-based query selection  
  - Separate tabs:
    - Obesity  
    - Malnutrition  
    - Combined Analysis  
  - Live SQL query execution  
  - User-friendly UI  

8. Power BI Dashboard

    An interactive Power BI dashboard was created to visualize global obesity and malnutrition trends.

Key Features:
  - Country-wise comparison of obesity and malnutrition  
  - Year-wise trend analysis (2012–2022)  
  - Gender-based distribution  
  - Age-group analysis  
  - Region-wise insights  

Visualizations:
   - Bar charts  
   - Line charts  
   - Pie charts  
   - KPI cards  

Insights:
   - Identified countries with high obesity rates  
   - Compared malnutrition trends across regions  
   - Highlighted demographic differences  

 File:
   - `nutrition_dashboard.pbix`

9. Deployment

  - Platform: **Streamlit Cloud**

10. Tools & Technologies

  - Python  
  - Pandas, NumPy  
  - Matplotlib, Seaborn  
  - SQL (TiDB/MySQL)  
  - Streamlit  
  - Power BI  

11. Key Insights

  - Identified regions with high obesity trends  
  - Found patterns between malnutrition and demographics  
  - Observed gender-based health differences  

12. Conclusion

   This project provides meaningful insights into global nutrition trends and helps in identifying vulnerable populations.

13. Future Improvements

  - Add machine learning models for prediction  
  - Real-time data updates  
  - More advanced visualizations  

D.Genoviya
