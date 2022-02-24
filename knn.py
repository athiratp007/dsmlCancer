from sklearn.neighbours import kNeighboursClassifier 
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
irisData=load_iris()
x=IrisData.data
y=IrisData.target
X_train,X_test,Y_train,Y_test=(train_test_split(X,Y,testsize=0.2,random_state=42))
knn=kNeighboursClassifier(n_neighbours=7)
knn.fit(X_train,Y_train)
print(knn.predict(X_test))
