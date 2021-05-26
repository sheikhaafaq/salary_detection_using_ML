import pandas, joblib

#Load datset
ds = pandas.read_csv('salary.csv')

ds.columns
ds.info()
x = ds['YearsExperience'].values.reshape(30,1)
type(x)
x.shape
y = ds['Salary']

# Train model using LinearRegression algorithm
from sklearn.linear_model import LinearRegression

# Create model
model = LinearRegression()

# Fit features
model.fit(x , y)

# Get weight
model.coef_

# Predict results
model.predict([[ 1.1 ]] )

# Get Bias
model.intercept_

#save model
joblib.dump(model, "salary_model.pki")

#load model
model2 = joblib.load('model.pki')

#predict
model.predict([[ 1.1 ]] )