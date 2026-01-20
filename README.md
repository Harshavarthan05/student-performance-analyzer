Student Insight Performance Analyzer
Project Overview:

The project is based on Visualize and analysis the student Academic grades, Past fails and Absences of higher eduction that 
whould analyze risk and high performance predict by acadmeic side.

Problem Statement:

1. Management of academic analysis risk and high performance of student
2. Predict average percentage value of student analyzer
3. Visualize the model in dashboard of web app
4. Data can be store in Database

Features:

1.Analyze student academic performance across multiple grade
2.Identifies high performing and at-risk student
3.Visualize your percentage of risk and high performance using web app
4.Provide insight into attendance, grades and past fail list
5.Supports CSV based student data upload
6.User friendly and Interactive Interface

Tech Stack:

1.Programming Language: Python
2.Framework: Streamlit
3.Libraries: Pandas, Numpy, Matplotlib, Seaborn
4.Machine Learning: Scikit-learn
5.Database: CSV

Project Structure:

student_analyzer/
│── model/ 
│ └── model.pkl 
│ └──cat_cols.pkl
│ └──num_cols.pkl
│── app.py 
│── README.md
│── requirements.txt 
│── student_data.csv 
│──student.py

Installation & Setup:

1. Navigate to the project folder:
  cd student_analyzer_dashboard
2. Install required packages:
   pip install -r requirments.txt
3. Run the application:
   streamlit run app.py

Data Source:

1. Sample student dataset(CSV)
2. Public business dataset(Kaggle)

Machine Learning:

1. Model: Logistic Regression
2. Purpose: High and risk performance of failures to identifies
3. Preprocess: StandardScalar, OneHotencoder
4. Evaluation Metrics, F1 score, Accuracy Score

Output:

Charts and KPIs
Interactive of Student performance
