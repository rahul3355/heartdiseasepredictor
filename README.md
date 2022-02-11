# heartdiseasepredictor
http://rahulpatil35.pythonanywhere.com/

Explanation of ML Model
August 20, 2021 by Rahul

Project link : http://rahulpatil35.pythonanywhere.com

The "goal" of this project is to find the presence of heart disease in the patient.

Logistic Regression
Logistic regression is a supervised learning classification algorithm used to predict the probability of a target variable. The nature of target or dependent variable is dichotomous, which means there would be only two possible classes.
Mathematically, a logistic regression model predicts P(Y=1) as a function of X


Features & Target

Features list
•	age
•	sex
•	chest pain type (4 values)
•	resting blood pressure
•	serum cholesterol in mg/dl
•	fasting blood sugar > 120 mg/dl
•	resting electrocardiographic results (values 0,1,2)
•	maximum heart rate achieved
•	exercise induced angina
•	oldpeak = ST depression induced by exercise relative to rest
•	the slope of the peak exercise ST segment
•	number of major vessels (0-3) coloured by fluoroscopy
•	thal (4 values)
Target list
•	result (values 0,1 | 0: heart disease not present, 1: heart disease present)

This is a definition list:

Features
A feature is a measurable property of the object you’re trying to analyse. In datasets, features appear as columns.
Target
The target variable of a dataset is the feature of a dataset about which you want to gain a deeper understanding.

Libraries & Packages 
pandas, sci-kit learn, matplotlib, numpy, os, pickle, flask, flask_mail, sqlite3

Validations
Validation is the process of checking whether the given input/product is up to the mark..
•	Age - 10 to 130
•	Blood Pressure - 80 to 200
•	Cholesterol - 100 to 600
•	Heart Rate - 70 to 210
•	Oldpeak - 0.0 to 6.0

Future Scope
1.	Model can be made more accurate using more attributes and/or more amount of data
2.	API of the project can be made which can be used directly by Third-Party Applications.
3.	Separate Admin Panel and Dashboard for Medical Staff and Users can be implemented
4.	Passwords can be encrypted before they are stored in Database. 	
5.	Nearest Hospital Locations can be displayed using Geo-location and Google Maps API

Contact:
Email : rahulpatil33553@gmail.com		Phone : (+91)8308009372 
LinkedIn : rahulpatil35					GitHub : rahul3355 
