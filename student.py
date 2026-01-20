import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

data = pd.read_csv("student_data.csv")
X = data.drop(['failures'], axis = 1)
y = data['failures']

print(data.info())
print(data.head())

#print(data.isnull().sum())
#print(data.mean())

numeric_features = X.select_dtypes(include = ["int64"]).columns
categorical_features = X.select_dtypes(include = ["object"]).columns

num_cols = X.select_dtypes(include = "int64").columns.tolist()
cat_cols = X.select_dtypes(include = "object").columns.tolist()

preprocesssor = ColumnTransformer(
    transformers = [
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

model = Pipeline(steps = [
    ('preprocessor', preprocesssor),
    ('classifier', LogisticRegression(
        max_iter = 1000,
        multi_class = 'multinomial',
        random_state = 42
    ))
])


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)

model.fit(X_train,y_train)
y_predict = model.predict(X_test)

print("Accuracy score: ", accuracy_score(y_test, y_predict))
print("f1 score: ", f1_score(y_test, y_predict, average='weighted'))
#print("precision score: ", precision_score(y_test, y_predict))
#print("Recall score: ", recall_score(y_test,y_predict))

plt.figure(figsize=(8,6))
sns.countplot(x=data['failures'])
plt.xlabel('student_data')
plt.ylabel('failures')
plt.show()

corr = data.select_dtypes(include="number").corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot = True, cmap = 'plasma')
plt.show()

joblib.dump(model, 'model/model.pkl')
joblib.dump(num_cols, "model/num_cols.pkl")
joblib.dump(cat_cols, "model/cat_cols.pkl")

print("Model saved successfully")