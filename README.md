## 🍱 Food Delivery Data Warehouse & Analytics:  
End-to-End Data Pipeline for Optimizing Delivery Performance  
- Power BI  
- SQL  
- Python  

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
- Example: Refund rate by region  
![image](https://github.com/user-attachments/assets/8af6da23-bab6-4637-8cc4-f6dff6fc478a)
 

3. Power BI Dashboard:
   ![Dashboard](https://github.com/user-attachments/assets/448dde32-e4f4-4b2d-bc42-ec94bc653d11)

   _<u>KPIs:</u>_  
   - 18,000 Total Orders demonstrate the operational scale.  
   - $922K in Revenue, reflect strong business performance.  
   - $3.48 Average Tip, indicate the customer satisfaction.  
   - A minimal 0.01% Refund Rate, highlight service reliability.  
       
   _<u>Trends & Time Analysis:</u>_  
   - The 'Orders Over Time' graph reveals daily fluctuations. The peak visible on the 12th, aligns with a promotional campaign.  
   - By identifying such trends, the inventory and staffing can be planned proactively & efficiently.  

   _<u>Geographic & Restaurant Performance:</u>_  
   - The 'Revenue by Restaurant' chart shows top performing restaurant outlet.  
   - Restaurant id #63 can be observed to be leading with $40K.  
   - The strategies of top performing outlet can therefore be replicated elsewhere.  
     
   _<u>Customer Behavior Insights:</u>_  
   - The Tip Analysis section correlates average tips with order volume.  
   - Higher tips often accompany peak hours, a cue to incentivize drivers during these times.  
      
   _<u>Operational Efficiency:</u>_  
    - The 'ASAP vs. Scheduled Orders' pie chart reveals 80% of orders are scheduled.  
    - This predictability helps optimize delivery routes and reduce costs.
      
   _<u>Summary:</u>_  
   - The Visualazation via dashboard provides a roadmap to smarter decisions.  
   - From boosting revenue in low-performing regions to rewarding the best drivers, these insights empower to act in right direction.  
   - With real-time filters, strategies can be adapted on the fly.  

## 🚀 How to Run This Project:  
_<u>Prerequisites:</u>_  
MySQL, Python 3.8+, Power BI.  

_<u>Libraries:</u>_  
pandas, mysql-connector-python, tqdm.    

_<u>Setup:<u>_  
-> bash  
git clone https://github.com/Purtee20/data-warehouse-food-delivery.git  
cd data-warehouse-food-delivery  
pip install -r requirements.txt  # Add a requirements file if missing  
Load Data:  

-> bash  
python load_data.py  # Raw data → Staging  
python load_dw.py    # Staging → Data warehouse  

_<u>Analyze:</u>_  
Open dashboard.pbix in Power BI.  
Connect to your MySQL DB for live updates.  

## 🔍 Key Challenges & Solutions:  
_<u>Challenges:</u>_	 
- Messy datetime formats	 
- High refund rates in Mountain View 	
- Slow query performance	   

_<u>Solutions:</u>_  
- Custom Python parser with error logging (parse_datetime()).
- Identified restaurant #23 as outlier (12% refund rate).
- Added indexes on fact_orders.date_id (40% faster).


## 📈 Business Impact:  
- Cost Reduction: Refund analysis could save ~$15K/month by addressing outlier restaurants.  
- Revenue Growth: Targeted promotions for high-tip regions (Palo Alto).  
- Scalability: Pipeline handles 100K+ rows (tested with synthetic data).  

## 🛠️ Tools & Technologies:  
- Data Warehousing: MySQL (Star Schema), Snowflake (compatible).  
- ETL: Python (Pandas), SQL.  
- Visualization: Power BI.  
- Design: Draw.io, Power BI.(Schema Diagram)  

## 📂 Repository Structure:  
```
data-warehouse-food-delivery/  
├── data/                                           # Sample CSV files  
├── scripts/  
│   ├── load_data.py                                # Raw data → Staging  
│   ├── load_dw.py                                  # Staging → DW (optimized)  
│   └── analysis.ipynb                              # Advanced analytics  
├── sql/  
│   └── Food_Delivery_Data_Analytics.sql           # Schema + EDA queries  
├── Dashboard.pbix                                 # Power BI dashboard  
└── README.md                                      # You are here!  
```
## 🧑‍💻 Next Steps:  
Extend This Project:  
- Add real-time streaming (Kafka, Spark).  
- Deploy to cloud (AWS RDS, Snowflake).  

