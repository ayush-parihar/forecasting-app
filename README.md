# 📈 Django Time-Series Forecasting Web App
 
A simple Django-based web application that demonstrates time series forecasting using Facebook Prophet. This project uses daily sales data as an example and allows users to visualize historical trends and generate future forecasts interactively through a web interface.
 
---
 
## 🔧 Features
 
- Forecast future sales based on historical time-series data.
- User input for forecast horizon (number of future days).
- Interactive visualizations using Plotly:
  - Historical data trends
  - Forecasted values
  - Confidence intervals
 
---
 
## 📁 Dataset
 
**Dataset Name:** Daily Sales Data  
**Source:** [Kaggle - Store Sales Time Series Forecasting](https://www.kaggle.com/competitions/store-sales-time-series-forecasting)  
**Columns used:**
- `date`: daily timestamps
- `sales`: daily sales figures
 
The dataset is located in the `data/` directory and preprocessed before modeling.
 
---
 
## 📦 Tech Stack
 
- **Framework:** Django (Python)
- **Model:** Facebook Prophet (for forecasting)
- **Frontend:** HTML, Plotly.js for charts
- **Backend:** Python, Pandas
- **Serialization:** Joblib (for saving/loading model)
 
---
 
## 🚀 Getting Started
 
### 1. Clone the repository
 
```bash
git clone https://github.com/ayush-parihar/forecasting-app.git
bash server.sh
