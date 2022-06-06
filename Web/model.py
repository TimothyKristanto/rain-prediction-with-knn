# imports
import pandas as pd

# data visualization
import seaborn as sns

ds = pd.read_excel("rainData.xlsx")
ds.head()

# drop Tanggal column since it does not have any correlation with other data at all
ds = ds.drop(["Tanggal"], axis=1)
ds.info()

ds["ddd_car"] = ds["ddd_car"].astype("string")
ds.info()


# **Drop NaN Values**

ds = ds.dropna()
ds = ds[ds["RR"] != 8888]
ds.info()


# In[22]:


sns.displot(ds["RR"])


# **Data Labeling**


# change "RR" column values to 0 and 1
# 0 means not raining while 1 means the otherwise
ds.loc[(ds["RR"] < 0.5), "RR"] = 0
ds.loc[(ds["RR"] >= 0.5), "RR"] = 1
ds["RR"].value_counts()


print(ds["ddd_car"].value_counts())


from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
ds["ddd_car"] = le.fit_transform(ds["ddd_car"])
print(ds["ddd_car"].value_counts())


# **Model Training and Testing**

# split data
X = ds.drop(columns=["RR"])
y = ds[["RR"]]

print(X.columns)

from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score

# for random in random_state:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=61)

from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score

regular_model = KNeighborsClassifier()
cv = KFold(n_splits=5, shuffle=True, random_state=7)

param_grid = {'n_neighbors': np.arange(1, 26, 2)}
model = GridSearchCV(regular_model, param_grid, cv=cv)
model.fit(X_train, y_train)


def makePrediction(data):
    y_pred = model.predict(data)
    return y_pred


y_pred = makePrediction(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))

