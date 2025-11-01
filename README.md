📊 Unemployment Analysis Dashboard

📌 Overview

This project visualizes and analyzes unemployment trends across different regions and time periods using Python and Streamlit.
It provides an interactive dashboard to explore patterns in employment, labor participation, and area-wise variations.

🗂️ Folder Structure
UNEMPLOYMENT_ANALYSIS_PYTHON/

│

├── app.py                          # Streamlit main app

├── scripts/

│   └── data_cleaning.py            # Data loading & preprocessing

├── dataset/

│   └── unemployment_data.csv       # Dataset used for analysis

├── reports/                        # Optional folder for charts/reports

└── README.md                       # Project documentation

⚙️ Requirements

Make sure you have Python 3.8+ installed.
Install dependencies using:

pip install -r requirements.txt


requirements.txt

streamlit
pandas
matplotlib
seaborn

▶️ Run the App

Run this command in the project directory:

streamlit run app.py


Then open your browser and go to the URL displayed (usually http://localhost:8501).

📊 Features

📁 Loads and cleans unemployment dataset automatically

🌍 Region-wise filtering

📈 Time series visualization of unemployment rate

🏙️ Top regions by average unemployment rate

🏘️ Area-wise employment comparison (Urban vs Rural)

🧼 Automated data cleaning via data_cleaning.py

📤 Example Output

Bar chart showing top 10 regions with highest average unemployment

Line graph showing trend over time

Box plot comparing Urban and Rural unemployment distribution

🧠 Tech Stack

Python — Data analysis & visualization

Streamlit — Interactive GUI dashboard

Pandas — Data manipulation

Seaborn / Matplotlib — Chart plotting

👨‍💻 Author

Vishal Baburao Patil
Department of Computer Science Engineering
G H Raisoni College of Engineering and Management, Jalgaon
