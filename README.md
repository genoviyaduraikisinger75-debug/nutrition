NUTRITION ANALYTICS PROJECT
  Obesity & Malnutrition Analysis using WHO Data
1. Project Overview
      *This project analyzes global obesity and malnutrition trends using public WHO (World Health Organization) datasets.
       The goal is to clean, transform, analyze, store, and visualize the data using Python, SQL, and Streamlit.

  -The project covers:
       1. Data extraction from WHO APIs
       2.Data cleaning & feature engineering
       3.Exploratory Data Analysis (EDA)
       4.SQL database integration (TiDB/MySQL)
       5.Query-based analysis
       6.Interactive Streamlit dashboard
       7.Cloud deployment


2. Data Cleaning & Feature Engineering
   - Key Steps:
        Renamed columns for consistency
        Standardized gender values (Male, Female, Both)
        Converted ISO-3 country codes to full names using pycountry
        Handled special WHO region codes
        Filtered data between 2012–2022

  -Created new features:
       Age_Group
       CI_Width
       Obesity_Level
       Malnutrition_Level


3. Exploratory Data Analysis (EDA)

    - EDA was performed using Python (Pandas, Matplotlib, Seaborn) to:
        Understand data distribution
        Identify missing/unusual values
        Analyze trends across years and regions
        Compare obesity vs malnutrition patterns
        Study gender and age-group differences

4. Database Integration

      SQL Engine: TiDB Cloud (MySQL compatible)
      Database name: nutrition
      Tables:
        obesity
        malnutrition
  -Data insertion was optimized using batch inserts (executemany) for performance.

5.  SQL Query Analysis
    Total Queries Implemented: 25
    Obesity (10 Queries)
    Malnutrition (10 Queries)
    Combined Analysis (5 Queries)

6. Streamlit Dashboard

  - An interactive Streamlit application was built with:
     Dropdown-based query selection
     Separate tabs for Obesity, Malnutrition, and Combined analysis
     SQL-backed live results
     Cloud deployment support

7. Deployment
     Platform: Streamlit Cloud



Database hosted on TiDB Cloud

Fully cloud-accessible dashboard
