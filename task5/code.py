#importing modules
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics


#set options for pandas
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def cleandata(data):
	"""
	Remove null,nan values along with irrelevant rows and cols
	"""

	#remove irrelevant rows and columns
	drop_col = [0,4,5,7,8,9,10,11,15,16,17,18,19]
	data = data.drop(data.columns[drop_col],axis=1)
	data = data.iloc[1:,]

	#replace blank strings and empty cells with NaN
	data = data.replace(r'\s+',np.nan, regex=True)

	#remove records where magnitude=NaN
	data = data.dropna(subset=['MAGNITUDE'])

	#add values where NaN present
	data['YEAR '] = data['YEAR '].fillna(0)
	data['MONTH '] = data['MONTH '].fillna(0)
	data['DATE'] = data['DATE'].fillna(0)
	data['DEPTH (km)'] = data['DEPTH (km)'].fillna(-1)
	data['LAT (N)'] = data['LAT (N)'].fillna(-1)
	data['LONG (E)'] = data['LONG (E)'].fillna(-1)

	#convert data to float for comparing
	data = data.apply(pd.to_numeric)
	
	#print sample data points
	print("Sample data:\n")
	print(data)
	
	return data


def classification_model(data,C):
	"""
	Returns results of model based on given data and comparision value
	"""

	#setting labels for the classifier
	X,Y = [],[]
	for index,rows in data.iterrows():
		X.append(rows)
		if rows['MAGNITUDE']<C:
			Y.append(0)
		else:
			Y.append(1)

	X = pd.DataFrame(X)
	Y = pd.DataFrame(Y)

	#remove label column
	X = X.drop(X.columns[3],axis=1)

	#split into test and train
	X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

	#Apply decision trees
	clf = DecisionTreeClassifier(criterion='gini',splitter='best')
	clf = clf.fit(X_train,y_train)
	y_pred = clf.predict(X_test)
	


	#print metrics
	print("\n-------")
	print("RESULTS")
	print("-------")
	
	print("Feature Importances/Gini Importances")
	print(list(X_test.columns))
	print(clf.feature_importances_)
	print("")

	print("Depth of tree: ",clf.get_depth())
	print("No. of leaf nodes: ",clf.get_n_leaves())
	print("")
	
	print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
	print("Recall:",metrics.recall_score(y_test, y_pred))
	print("Precision Score:",metrics.precision_score(y_test, y_pred))
	print("F1 Score:",metrics.f1_score(y_test, y_pred))
	print("Confusion Matrix:")
	print(metrics.confusion_matrix(y_test,y_pred))


#read data
data=pd.read_csv("./data.csv",low_memory=False,header=[0])

#clean the data
data=cleandata(data)

#Part A
print("\n----------------------------")
print("Results for combined dataset")
print("----------------------------\n")
classification_model(data,3)
classification_model(data,4)
classification_model(data,5)


#Part B
data1=data.loc[data['YEAR '] < 2000] 
data1=data1.loc[data1['YEAR '] >= 1990] 

data2=data.loc[data['YEAR '] < 2010] 
data2=data2.loc[data2['YEAR '] >= 2000] 

data3=data.loc[data['YEAR '] < 2020] 
data3=data3.loc[data3['YEAR '] >= 2010] 


print("\n-----------------------------")
print("Results for dataset 1990-2000")
print("-----------------------------\n")
classification_model(data1,3)
classification_model(data1,4)
classification_model(data1,5)

print("\n-----------------------------")
print("Results for dataset 2000-2010")
print("-----------------------------\n")
classification_model(data2,3)
classification_model(data2,4)
classification_model(data2,5)

print("\n-----------------------------")
print("Results for dataset 2010-2020")
print("-----------------------------\n")
classification_model(data3,3)
classification_model(data3,4)
classification_model(data3,5)