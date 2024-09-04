import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings

# Ignore all warnings
warnings.filterwarnings('ignore')

from sklearn.datasets import load_iris #dataset
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree #used for Decision Tree


data = load_iris()
#converting into dimensions for independent(feature_names) and dependent(targetvalues)
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

#spilt in training and testing sets.

X_train, X_test, y_train, y_test = train_test_split(df[data.feature_names], df['target'], random_state=0)

#decide depth as 2
clf = DecisionTreeClassifier(max_depth = 2, random_state = 0)

#fit the tests in the algorithm
clf.fit(X_train, y_train)

#predictions

clf.predict(X_test.iloc[0].values.reshape(1, -1))
clf.predict(X_test[0:10])

#accuracy/performance
score = clf.score(X_test, y_test)
print("The Prediction score is",score)

plt.figure(figsize=(12, 8))
plot_tree(clf, 
          feature_names=data.feature_names, 
          class_names=data.target_names, 
          filled=True, 
          rounded=True)
plt.show()



def classify_flower():
    print("Enter the features of the flower to classify:")

    # Taking input from the user for each feature
    sepal_length = float(input("Enter sepal length (cm): "))
    sepal_width = float(input("Enter sepal width (cm): "))
    petal_length = float(input("Enter petal length (cm): "))
    petal_width = float(input("Enter petal width (cm): "))

    # Create a NumPy array from the input
    new_flower = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Predict the class of the new flower
    predicted_class = clf.predict(new_flower)

    # Get the class name for the predicted class
    class_name = data.target_names[predicted_class[0]]

    print(f"The predicted class for the input flower is: {class_name}")

# Call the function to classify a flower
classify_flower()