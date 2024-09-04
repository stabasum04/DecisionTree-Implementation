DecisionTree-to-find-out-the-flower-type

This Python project uses a Decision Tree Classifier from the scikit-learn library to classify iris flowers based on user input. The classifier is trained on the famous Iris dataset, which contains features like sepal length, sepal width, petal length, and petal width for three types of iris species: Setosa, Versicolor, and Virginica.

The project allows users to input flower measurements and get a prediction of the iris species.

Features:
•	Trains a Decision Tree Classifier on the Iris dataset.
•	Takes user input for flower measurements (sepal length, sepal width, petal length, petal width).
•	Predicts the species of the iris flower based on user input.
•	Visualizes the trained decision tree using matplotlib and plot_tree(from DecisionTreeClassifer)

Use the cmd if you dont have these modules:

pip install scikit-learn matplotlib numpy

To run the code:

python3 classify_iris.py

Follow the on-screen instructions to enter the flower's features:

Enter sepal length in cm
Enter sepal width in cm
Enter petal length in cm
Enter petal width in cm
The program will output the predicted class (species) of the iris flower.

Example:

Copy code
Enter the features of the flower to classify:
Enter sepal length (cm): 5.1
Enter sepal width (cm): 3.5
Enter petal length (cm): 1.4
Enter petal width (cm): 0.2
The predicted class for the input flower is: setosa

![image](https://github.com/user-attachments/assets/20d626af-8035-42c1-820b-f873e41a70e6)
