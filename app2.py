import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt

# Sample data setup
# Assume 'data' is a DataFrame with a DateTime index and a 'demand' column representing monthly demand
data = pd.DataFrame({
    'date': pd.date_range(start='2018-01-01', periods=60, freq='M'),
    'demand': np.random.randint(100, 200, size=60)  # Replace with actual demand data
})
data.set_index('date', inplace=True)

# Apply Holt-Winters Exponential Smoothing
# Using multiplicative seasonality to capture more complex seasonal effects
model = ExponentialSmoothing(data['demand'], 
                             seasonal='multiplicative', 
                             trend='additive', 
                             seasonal_periods=12).fit()

# Forecast for the next 12 months
forecast = model.forecast(12)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(data['demand'], label='Historical Demand')
plt.plot(forecast, label='Forecasted Demand', linestyle='--')
plt.title('Winter Demand Forecast using Holt-Winters Model')
plt.xlabel('Date')
plt.ylabel('Demand')
plt.legend()
plt.show()
