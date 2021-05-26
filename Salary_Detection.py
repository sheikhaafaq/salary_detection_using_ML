import  joblib

#load model
model = joblib.load('salary_model.pki')

#predict
x = model.predict([[ float(input("How much yearsOfExperience you have? ") ) ]] )

print(f"Your salary should be Rs { x[0] }")
