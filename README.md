## 🍱 Food Delivery Data Warehouse & Analytics:  
End-to-End Data Pipeline for Optimizing Delivery Performance  
Power BI  
MySQL  
Python  

## 📌 Business Problem:  
Food delivery platforms need to analyze order trends, delivery efficiency, and customer behavior to:  
1) Reduce refunds and operational costs.  
2) Optimize driver allocation based on regional demand.  
3) Identify high-value customers (e.g., frequent tippers).  

## 🛠️ Solution Architecture:    
Star Schema Diagram:  
![image](https://github.com/user-attachments/assets/f42e15ff-f8a0-423c-87d9-6b662a77ee8e)


1. ETL Pipeline  
Extract: Raw CSV data → Staging tables (staging_orders).  
Transform: Python (pandas) for datetime parsing, error handling, and deduplication.  
Load: Optimized star schema in MySQL:  
Fact Table: fact_orders (metrics: revenue, tips, refunds).  
Dimensions: dim_customer, dim_restaurant, dim_driver, dim_time.  

2. Data Warehouse  
Optimized Queries: Indexing for performance (e.g.: CREATE INDEX idx_fact_orders_date ON fact_orders(date_id);).  
Key Metrics:  
sql  
-- Example: Refund rate by region  
SELECT   
    c.delivery_region,  
    SUM(f.refunded) / SUM(f.order_total) AS refund_rate  
FROM fact_orders f  
JOIN dim_customer c ON f.customer_id = c.customer_id  
GROUP BY c.delivery_region;  

3. Power BI Dashboard:  
   KPIs: Total orders (18K), revenue ($922K), refund rate (1%).  
   Trends: Orders over time, regional performance, ASAP vs. scheduled deliveries.  
   Insights:  
    - Mountain View has the highest tip average ($3.48).  
    - 20% of orders are ASAP → Potential for surge pricing.  

## 🚀 How to Run This Project:  
Prerequisites:  
MySQL, Python 3.8+, Power BI.  
Libraries: pandas, mysql-connector-python, tqdm.  

Setup:  
bash  
git clone https://github.com/Purtee20/data-warehouse-food-delivery.git  
cd data-warehouse-food-delivery  
pip install -r requirements.txt  # Add a requirements file if missing  
Load Data:  

bash  
python load_data.py  # Raw data → Staging  
python load_dw.py    # Staging → Data warehouse  

Analyze:  
Open dashboard.pbix in Power BI.  
Connect to your MySQL DB for live updates.  

## 🔍 Key Challenges & Solutions:  
Challenge	Solution
Messy datetime formats	Custom Python parser with error logging (parse_datetime()).
High refund rates in Mountain View	Identified restaurant #23 as outlier (12% refund rate).
Slow query performance	Added indexes on fact_orders.date_id (40% faster).  

## 📈 Business Impact:  
- Cost Reduction: Refund analysis could save ~$15K/month by addressing outlier restaurants.  
- Revenue Growth: Targeted promotions for high-tip regions (Palo Alto).  
- Scalability: Pipeline handles 100K+ rows (tested with synthetic data).  

## 🛠️ Tools & Technologies:  
- Data Warehousing: MySQL (Star Schema), Snowflake (compatible).  
- ETL: Python (Pandas), SQL.  
- Visualization: Power BI.  
- Design: Draw.io (schema diagrams).  

## 📂 Repository Structure:  
data-warehouse-food-delivery/  
├── data/                                          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Sample CSV files  
├── scripts/  
│   ├── load_data.py                               &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Raw data → Staging  
│   ├── load_dw.py                                 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Staging → DW (optimized)  
│   └── analysis.ipynb                             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Advanced analytics  
├── sql/  
│   └── Food_Delivery_Data_Analytics.sql           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Schema + EDA queries  
├── docs/  
│   └── schema.drawio                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Schema diagram  
├── Dashboard.pbix                                 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Power BI dashboard  
└── README.md                                      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # You are here!  

## 📞 Next Steps:  
Extend This Project:  
- Add real-time streaming (Kafka, Spark).  
- Deploy to cloud (AWS RDS, Snowflake).  

Connect:  
LinkedIn | Portfolio  

