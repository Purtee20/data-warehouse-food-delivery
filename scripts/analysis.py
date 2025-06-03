import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.ensemble import IsolationForest  # Anomaly detection
warnings.filterwarnings('ignore')
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://user:password@localhost/food_delivery_dw')

# Load ONLY what's needed for analysis
with engine.connect() as conn:
    df = pd.read_sql("""
        SELECT 
            f.order_total, f.tip, f.refunded, f.delivery_time, f.is_asap,
            c.delivery_region, c.is_new,
            t.delivery_datetime
        FROM fact_orders f
        JOIN dim_customer c ON f.customer_id = c.customer_id
        JOIN dim_time t ON f.time_id = t.time_id
    """, conn)

# Optimize memory (no dtype repetition from load_dw.py)
df = df.convert_dtypes()

# Train Isolation Forest on refunds
clf = IsolationForest(contamination=0.01)
df['is_anomaly'] = clf.fit_predict(df[['refunded']])

# Plot anomalies
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='order_total',
    y='refunded',
    hue='is_anomaly',
    palette={1: 'blue', -1: 'red'}
)
plt.title('Anomaly Detection: Refunds vs Order Total')
plt.show()

# Calculate RFM features directly in pandas
clv_data = df.groupby('customer_id').agg({
    'delivery_datetime': lambda x: (pd.Timestamp.now() - x.max()).days,  # Recency
    'order_id': 'count',  # Frequency
    'order_total': 'sum'  # Monetary
}).rename(columns={
    'delivery_datetime': 'recency',
    'order_id': 'frequency',
    'order_total': 'monetary'
})

# Visualize CLV segments:
sns.pairplot(clv_data, diag_kind='kde')
plt.suptitle('RFM Features for CLV Modeling', y=1.02)
plt.show()

# Simulate geo coordinates:
np.random.seed(42)
regions = df['delivery_region'].unique()
geo_mock = {r: (np.random.uniform(-122, -121), np.random.uniform(37, 38)) for r in regions}

# Plot:
plt.figure(figsize=(10, 6))
for r, (lat, lon) in geo_mock.items():
    plt.scatter(lon, lat, label=r, s=df[df['delivery_region']==r]['order_total'].sum()/1000)
plt.legend(title='Order Volume (Size)')
plt.title('Simulated Regional Order Hotspots')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Generate insights programmatically
top_region = df.groupby('delivery_region')['order_total'].sum().idxmax()
avg_tip = df['tip'].mean()
refund_rate = df['refunded'].sum() / df['order_total'].sum()

from IPython.display import Markdown
Markdown(f"""
### 🚀 Auto-Generated Insights  
- **Busiest Region**: {top_region}  
- **Avg Tip**: ${avg_tip:.2f} ({df['tip'].median():.2f} median)  
- **Refund Rate**: {refund_rate:.2%}  
- **Anomalies Detected**: {len(df[df['is_anomaly']==-1]):,} orders  
""")
