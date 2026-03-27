import streamlit as st
import mysql.connector
import pandas as pd

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Nutrition SQL Dashboard", layout="wide")
st.title("🥗 Nutrition Analytics Dashboard")
st.write("Interactive SQL analysis for Obesity & Malnutrition (25 Queries)")

# -------------------------------
# DATABASE CONNECTION (TiDB / MySQL) 
# -------------------------------
import mysql.connector
import streamlit as st

#
def get_connection():
    return mysql.connector.connect(
        host="hostname",
        port=portnumber,
        user="username",
        password="password",
        database="database name",
        ssl_disabled=False
    )

conn = get_connection()

def run_query(query):
    return pd.read_sql(query, conn)

# -------------------------------
# 🧋 OBESITY QUERIES (10)
# -------------------------------
obesity_queries = {
    "1. Top 5 Regions (2022)": """
        SELECT Region, AVG(Mean_Estimate) AS avg_obesity
        FROM obesity
        WHERE Year = 2022
        GROUP BY Region
        ORDER BY avg_obesity DESC
        LIMIT 5;
    """,

    "2. Top 5 Countries (Overall)": """
        SELECT Country, AVG(Mean_Estimate) AS avg_obesity
        FROM obesity
        GROUP BY Country
        ORDER BY avg_obesity DESC
        LIMIT 5;
    """,

    "3. Obesity Trend in India": """
        SELECT Year, AVG(Mean_Estimate) AS obesity_trend
        FROM obesity
        WHERE Country = 'India'
        GROUP BY Year
        ORDER BY Year;
    """,

    "4. Average Obesity by Gender": """
        SELECT Gender, AVG(Mean_Estimate) AS avg_obesity
        FROM obesity
        GROUP BY Gender;
    """,

    "5. Country Count by Obesity Level & Age Group": """
        SELECT Obesity_Level, Age_Group,
               COUNT(DISTINCT Country) AS country_count
        FROM obesity
        GROUP BY Obesity_Level, Age_Group;
    """,

    "6a. Least Reliable Countries (High CI)": """
        SELECT Country, AVG(CI_Width) AS avg_ci
        FROM obesity
        GROUP BY Country
        ORDER BY avg_ci DESC
        LIMIT 5;
    """,

    "6b. Most Consistent Countries (Low CI)": """
        SELECT Country, AVG(CI_Width) AS avg_ci
        FROM obesity
        GROUP BY Country
        ORDER BY avg_ci ASC
        LIMIT 5;
    """,

    "7. Average Obesity by Age Group": """
        SELECT Age_Group, AVG(Mean_Estimate) AS avg_obesity
        FROM obesity
        GROUP BY Age_Group;
    """,

    "8. Consistent Low Obesity Countries": """
        SELECT Country,
               AVG(Mean_Estimate) AS avg_obesity,
               AVG(CI_Width) AS avg_ci
        FROM obesity
        GROUP BY Country
        HAVING avg_obesity < 25 AND avg_ci < 3
        ORDER BY avg_obesity
        LIMIT 10;
    """,

    "9. Female > Male Obesity Gap": """
        SELECT f.Country, f.Year,
               (f.Mean_Estimate - m.Mean_Estimate) AS gender_gap
        FROM obesity f
        JOIN obesity m
          ON f.Country = m.Country AND f.Year = m.Year
        WHERE f.Gender = 'Female'
          AND m.Gender = 'Male'
          AND (f.Mean_Estimate - m.Mean_Estimate) > 5
        ORDER BY gender_gap DESC;
    """,

    "10. Global Average Obesity per Year": """
        SELECT Year, AVG(Mean_Estimate) AS global_avg
        FROM obesity
        GROUP BY Year
        ORDER BY Year;
    """
}

# -------------------------------
# 👾 MALNUTRITION QUERIES (10)
# -------------------------------
malnutrition_queries = {
    "1. Avg Malnutrition by Age Group": """
        SELECT Age_Group, AVG(Mean_Estimate) AS avg_malnutrition
        FROM malnutrition
        GROUP BY Age_Group;
    """,

    "2. Top 5 Countries (Malnutrition)": """
        SELECT Country, AVG(Mean_Estimate) AS avg_malnutrition
        FROM malnutrition
        GROUP BY Country
        ORDER BY avg_malnutrition DESC
        LIMIT 5;
    """,

    "3. Trend in Africa": """
        SELECT Year, AVG(Mean_Estimate) AS trend
        FROM malnutrition
        WHERE Region = 'Africa'
        GROUP BY Year
        ORDER BY Year;
    """,

    "4. Gender-based Average": """
        SELECT Gender, AVG(Mean_Estimate) AS avg_malnutrition
        FROM malnutrition
        GROUP BY Gender;
    """,

    "5. Avg CI Width by Level & Age": """
        SELECT Malnutrition_Level, Age_Group,
               AVG(CI_Width) AS avg_ci
        FROM malnutrition
        GROUP BY Malnutrition_Level, Age_Group;
    """,

    "6. Yearly Change (India, Nigeria, Brazil)": """
        SELECT Country, Year, AVG(Mean_Estimate) AS avg_val
        FROM malnutrition
        WHERE Country IN ('India','Nigeria','Brazil')
        GROUP BY Country, Year
        ORDER BY Country, Year;
    """,

    "7. Regions with Lowest Malnutrition": """
        SELECT Region, AVG(Mean_Estimate) AS avg_malnutrition
        FROM malnutrition
        GROUP BY Region
        ORDER BY avg_malnutrition ASC;
    """,

    "8. Increasing Malnutrition Countries": """
        SELECT Country,
               MIN(Mean_Estimate) AS min_val,
               MAX(Mean_Estimate) AS max_val
        FROM malnutrition
        GROUP BY Country
        HAVING (MAX(Mean_Estimate) - MIN(Mean_Estimate)) > 0;
    """,

    "9. Min/Max Malnutrition Year-wise": """
        SELECT Year,
               MIN(Mean_Estimate) AS min_val,
               MAX(Mean_Estimate) AS max_val
        FROM malnutrition
        GROUP BY Year
        ORDER BY Year;
    """,

    "10. High CI Width Alerts (>5)": """
        SELECT Country, Year, CI_Width
        FROM malnutrition
        WHERE CI_Width > 5
        ORDER BY CI_Width DESC;
    """
}

# -------------------------------
# 🔗 COMBINED QUERIES (5)
# -------------------------------
combined_queries = {
    "1. Obesity vs Malnutrition (5 Countries)": """
        SELECT o.Country,
               AVG(o.Mean_Estimate) AS avg_obesity,
               AVG(m.Mean_Estimate) AS avg_malnutrition
        FROM obesity o
        LEFT JOIN malnutrition m
          ON o.Country = m.Country
        WHERE o.Country IN ('India','United States','Brazil','Nigeria','China')
        GROUP BY o.Country;
    """,

    "2. Gender Disparity Comparison": """
        SELECT 'Obesity' AS Type, Gender, AVG(Mean_Estimate) AS avg_val
        FROM obesity
        GROUP BY Gender
        UNION ALL
        SELECT 'Malnutrition', Gender, AVG(Mean_Estimate)
        FROM malnutrition
        GROUP BY Gender;
    """,

    "3. Region-wise Comparison (Africa & Americas)": """
        SELECT o.Region,
               AVG(o.Mean_Estimate) AS avg_obesity,
               AVG(m.Mean_Estimate) AS avg_malnutrition
        FROM obesity o
        LEFT JOIN malnutrition m
          ON o.Region = m.Region
        WHERE o.Region IN ('Africa','Americas')
        GROUP BY o.Region;
    """,

    "4. Obesity ↑ & Malnutrition ↓ Countries": """
        SELECT o.Country
        FROM obesity o
        LEFT JOIN malnutrition m
          ON o.Country = m.Country
        GROUP BY o.Country
        HAVING MAX(o.Mean_Estimate) > MIN(o.Mean_Estimate)
           AND MAX(m.Mean_Estimate) < MIN(m.Mean_Estimate);
    """,

    "5. Age-wise Trend Analysis": """
        SELECT Age_Group, Year, AVG(Mean_Estimate) AS avg_val
        FROM obesity
        GROUP BY Age_Group, Year
        ORDER BY Age_Group, Year;
    """
}

# -------------------------------
# UI TABS
# -------------------------------
tab1, tab2, tab3 = st.tabs(["🧋 Obesity (10)", "👾 Malnutrition (10)", "🔗 Combined (5)"])

with tab1:
    q = st.selectbox("Select Obesity Query", obesity_queries.keys())
    if st.button("Run Obesity Query"):
        df = run_query(obesity_queries[q])
        st.dataframe(df, width="stretch")

with tab2:
    q = st.selectbox("Select Malnutrition Query", malnutrition_queries.keys())
    if st.button("Run Malnutrition Query"):
        df = run_query(malnutrition_queries[q])
        st.dataframe(df, width="stretch")

with tab3:
    q = st.selectbox("Select Combined Query", combined_queries.keys())
    if st.button("Run Combined Query"):
        df = run_query(combined_queries[q])
        if df.empty:
            st.warning("⚠️ No matching records found. Check JOIN conditions.")
        else:
            st.dataframe(df, width="stretch")

st.caption("📊 Nutrition SQL Dashboard")
