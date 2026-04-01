# Description: Short example for Time Series for Business Analytics with Python.



from data_io import read_csv
import logging
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)


# date,sales
# 2023-01-01,150
# 2023-01-02,170
# 2023-01-03,160
# 2023-01-04,180

# Load CSV into a DataFrame
df = read_csv("sales_data.csv")
# Inspect the DataFrame
logger.info(df.head())

# Output:
# date sales
# 0 2023-01-01 150
# 1 2023-01-02 170
# 2 2023-01-03 160
# 3 2023-01-04 180

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])
# Set 'date' column as the DataFrame index
df.set_index('date', inplace=True)
# Inspect the DataFrame
logger.info(df.head())

# Output:
# date sales
# 2023-01-01 150
# 2023-01-02 170
# 2023-01-03 160
# 2023-01-04 180

# Resample to monthly frequency, taking the mean of sales
monthly_sales = df.resample('M').mean()
logger.info(monthly_sales)
# Upsampling Example: Monthly to Daily
# Upsample to daily frequency with linear interpolation
daily_sales = monthly_sales.resample('D').interpolate(method='linear')
logger.info(daily_sales.head())


# Simulated beehive data
date_range = pd.date_range(start="2024-01-01", periods=48, freq="H")
data = {'temperature': np.random.normal(35, 2, len(date_range)),
        'weight': 50 + np.cumsum(np.random.normal(0.2, 0.1, len(date_range))),
        'bee_traffic': np.sin(np.linspace(0, 3*np.pi, len(date_range))) * 50 + 200}
df = pd.DataFrame(data, index=date_range)
df.index.name = 'time'
df.head()
