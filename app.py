from flask import Flask,render_template , request
import pickle
import numpy as np

model = pickle.load(open('admi.pkl','rb'))

app = Flask(__name__)
schoolDict={"Govt":0.4,"Private":0.0}
casteDict={"OC":0.1,"BC-A":0.2,"BC-B":0.3,"BC-D":0.4,"BC-E":0.5,"SC":0.6,"ST":0.7}
genderDict={"Male":0.34,"Female":0.66}

@app.route('/')
def man():
	return render_template('reg.html')
	
@app.route('/predict' , methods=['POST'])	
def home():
	gpa = request.form['gpa']
	gender = request.form['gender']
	school_type = request.form['school']
	caste = request.form['caste']
	arr = np.array([[float(gpa), schoolDict[school_type], casteDict[caste], genderDict[gender]]])
	pred = model.predict(arr)
	return render_template('result.html',data=int(float(pred)*100))
	
	

if __name__ == "__main__":
	app.run(debug=True)
