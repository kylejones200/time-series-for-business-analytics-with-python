# Time Series for Business Analytics with Python Time series analysis is a branch of analytics that focuses on data
collected over time. Unlike traditional analytics, where data points are...

### Time Series for Business Analytics with Python
Time series analysis is a branch of analytics that focuses on data collected over time. Unlike traditional analytics, where data points are often treated as independent and identically distributed (i.i.d.), time series data has an inherent structure --- the order of observations matters.


<figcaption>Photo by <a class="markup--anchor markup--figure-anchor" rel="photo-creator noopener" target="_blank">Amritanshu Sikdar</a> on <a class="markup--anchor markup--figure-anchor"


Each observation in a time series is influenced by the previous ones, creating temporal dependencies that we can use for our analysis.

This article explores time series data tools and techniques, and how to begin working with time series data in Python using the pandas library.

#### Why Time Series is Different
In regular analytics, we assume the data is i.i.d. --- values are independent and come from the same underlying distribution. For example, predicting customer age, income, or credit score assumes little relationship between individual observations. All parametric statistics are build on this assumption.

However, time series data violates this assumption because:

1\. Values are Dependent: The value at time often depends on previous values at T-1 (the pervious value). For example, today's stock price is influenced by yesterday's price.

2\. Order Matters: Observations are ordered chronologically, and rearranging them destroys meaningful patterns.

3\. Embedded Information: Trends, seasonality, and cycles are foundational concepts for time series data. For example:

- Trend: A gradual upward or downward movement (e.g., sales growth).
- Seasonality: Repeating patterns over fixed intervals (e.g., higher ice cream sales in summer).
- Cycles: Longer-term irregular fluctuations (e.g., business cycles).

Example: Imagine analyzing monthly electricity demand. Treating each month's demand as independent values would ignore the seasonal patterns (e.g., higher demand in winter) and temporal trends (e.g., increasing demand over years).

#### Why Time Series Uses Special Tools & Techniques
Time series analysis models need to account for account for temporal dependencies (Methods like ARIMA, exponential smoothing, and state-space). Time series values are measured on some frequency but that doesn't mean we want to analyze the data at that frequency. We need tools to resample and aggregate values to fit the frequency we are using for our analysis (for example, sifting daily values to monthly averages).

Traditional parametric statistics assumes the underlying data is stationary --- it assumes the mean, variance, and autocorrelation between variables is constant over the population. We can't make that assumption with time series --- in fact we are often looking for how the underlying population data changes over time.

We also need different feature engineering techniques for time series like creating lagged features, rolling statistics, or derivatives to embed temporal patterns into models.

Without these techniques, we risk building models that fail to capture the time-dependent structure of the data.

#### Getting Started with Time Series in Python
We start by loading and formating the data with the tools in pandas.

Uploading Time Series Data into a DataFrame

Suppose you have a CSV file containing a time series with columns for date and observed values:

Example File (sales_data.csv):


Python Code to Load the Data:


Looking at the top four observations:


Casting the Date Column as Timestamps

We need the date to be cast as a datetime object so Python knows it is a date. We also want to use the date as the index for the dataframe.

Python Code to Cast and Index by Date:



Now, the DataFrame treats date as a time index which will let us use tools like resampling, rolling windows, and time-based slicing.

Resampling to Change the Frequency

Resampling allows you to aggregate or disaggregate time series data to a different frequency. For example:

- Convert daily data to monthly averages.
- Upsample monthly data to daily using interpolation.
- Downsampling Example: Daily to Monthly


Key Points to Remember

1\. Time Index: Always convert and index your time series data using a datetime format to enable time-based operations.

2\. Order Matters: Never shuffle or rearrange time series data randomly.

3\. Resampling: Adjust the frequency of observations as needed for analysis or modeling.

4\. Check for Missing Data: Gaps in time series data can distort analysis and require imputation or handling.

#### Next steps
Time series analytics is different from regular analytics because values are not independent, and the order of observations contains meaningful information. We need to preserve the structure of the data as we do our analysis --- this includes casting dates, setting time indices, and resampling.

Now that we know how to ingest and store data, we are ready to move time series analysis, to do thinks like trend detection, forecasting, and anomaly detection.

#### Beehive Example
As a beekeeper, you install sensors in your hive to monitor its health. The data includes:

- Internal Temperature (°C).
- Weight (kg) of the hive.
- Bee Traffic (number of bees entering/exiting per minute).

Unlike typical analytics where values are independent, beehive data is time-dependent: Temperature changes gradually and depends on previous readings. Weight increases with honey production but drops if honey is harvested. Bee Traffic follows a pattern influenced by the time of day and season.

Here, the order of observations matters. Rearranging the temperature readings randomly would destroy any meaningful patterns, like daily cycles or seasonal trends.


#### Related Posts
This article is part of a series of posts on time series forecasting. Here is the list of articles in the order they were designed to be read.

1.  [[Time Series for Business Analytics with Python](https://medium.com/@kylejones_47003/time-series-for-business-analytics-with-python-a92b30eecf62?source=your_stories_page-------------------------------------)]
2.  [[Time Series Visualization for Business Analysis with Python](https://medium.com/@kylejones_47003/time-series-visualization-for-business-analysis-with-python-5df695543d4a?source=your_stories_page-------------------------------------)]
3.  [[Patterns in Time Series for Forecasting](https://medium.com/@kylejones_47003/patterns-in-time-series-for-forecasting-8a0d3ad3b7f5?source=your_stories_page-------------------------------------)]
4.  [[Imputing Missing Values in Time Series Data for Business Analytics with Python](https://medium.com/@kylejones_47003/imputing-missing-values-in-time-series-data-for-business-analytics-with-python-b30a1ef6aaa6?source=your_stories_page-------------------------------------)]
5.  [[Measuring Error in Time Series Forecasting with Python](https://medium.com/@kylejones_47003/measuring-error-in-time-series-forecasting-with-python-18d743a535fd?source=your_stories_page-------------------------------------)]
6.  [[Univariate and Multivariate Time Series Analysis with Python](https://medium.com/@kylejones_47003/univariate-and-multivariate-time-series-analysis-with-python-b22c6ec8f133?source=your_stories_page-------------------------------------)]
7.  [[Feature Engineering for Time Series Forecasting in Python](https://medium.com/@kylejones_47003/feature-engineering-for-time-series-forecasting-in-python-7c469f69e260?source=your_stories_page-------------------------------------)]
8.  [[Anomaly Detection in Time Series Data with Python](https://medium.com/@kylejones_47003/anomaly-detection-in-time-series-data-with-python-5a15089636db?source=your_stories_page-------------------------------------)]
9.  [[Dickey-Fuller Test for Stationarity in Time Series with Python](https://medium.com/@kylejones_47003/dickey-fuller-test-for-stationarity-in-time-series-with-python-4e4bf1953eed?source=your_stories_page-------------------------------------)]
10. [[Using Classification Model for Time Series Forecasting with Python](https://medium.com/@kylejones_47003/using-classification-model-for-time-series-forecasting-with-python-d74a1021a5c4?source=your_stories_page-------------------------------------)]
11. [[Measuring Error in Time Series Forecasting with Python](https://medium.com/@kylejones_47003/measuring-error-in-time-series-forecasting-with-python-18d743a535fd?source=your_stories_page-------------------------------------)]
12. [[Physics-informed anomaly detection in a wind turbine using Python with an autoencoder transformer](https://medium.com/@kylejones_47003/physics-informed-anomaly-detection-in-a-wind-turbine-using-python-with-an-autoencoder-transformer-06eb68aeb0e8?source=your_stories_page-------------------------------------)]
