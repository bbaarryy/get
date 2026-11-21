import pandas as pd
import numpy as np
from sklearn import datasets
from scipy.stats import norm

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 1. Загрузка встроенного датасета Iris
iris = load_iris()
X = iris.data  # Признаки (длина/ширина чашелистика и лепестка)
y = iris.target  # Целевая переменная (классы: Setosa, Versicolor, Virginica)

# 2. Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Проверка размеров полученных выборок
print(f"Размер обучающей выборки (X_train): {X_train.shape}")
print(f"Размер тестовой выборки (X_test): {X_test.shape}")

class GaussianNB:
    def fit(self, X_train, y_train):
        self.m0 = X_train[y_train==0].mean(axis=0)
        self.s0 = X_train[y_train==0].std(axis = 0)
        self.m1 = X_train[y_train==1].mean(axis=0)
        self.s1 = X_train[y_train==1].std(axis = 0)
        self.m2 = X_train[y_train==2].mean(axis=0)
        self.s2 = X_train[y_train==2].std(axis = 0)

    def predict(self, X_test):
        self.y_pred = []
        for x in X_test:
            p0 = norm.pdf(x,self.m0,self.s0).sum()
            p1 = norm.pdf(x,self.m1,self.s1).sum()
            p2 = norm.pdf(x,self.m2,self.s2).sum()

            self.y_pred.append(np.argmax([p0,p1,p2]))

    def score(self, X_test, y_test):
        self.predict(X_test)
        acc = (np.array(self.y_pred) == y_test).mean()
        return(acc)

model = GaussianNB()

model.fit(X_train, y_train)
print(model.score(X_test,y_test))

class KNeighborsClassifier:
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test, y_test):
        self.y_pred = y_test.copy(deep=True)
        for index, row in X_test.iterrows():
            a = ((self.X_train - row)**2).sum(axis=1).sort_values()[:5].index
            a = self.y_train.iloc[a].mode()[0]

            self.y_pred[index] = a

    def score(self, X_test, y_test):
        self.predict(X_test,y_test)

        #print(y_test, self.y_pred[0])

        first_row_list = self.y_pred.iloc[0].values.tolist() 
        first_col_list = y_test.iloc[:, 0].values.tolist()
        #print(first_row_list,first_col_list)
        return((np.array(first_col_list) == np.array(first_row_list)).mean())

model2 = KNeighborsClassifier()
model2.fit(pd.DataFrame(X_train),pd.DataFrame(y_train))
print(model2.score(pd.DataFrame(X_test),pd.DataFrame(y_test)))

X_train = np.array(X_train)

print( ((X_train[:,0].min()) / (X_train[:,0].max() - X_train[:,0].min()))**2  + 
      ((X_train[:,1].min()) / (X_train[:,1].max() - X_train[:,1].min()))**2 +
      ((X_train[:,2].min()) / (X_train[:,2].max() - X_train[:,2].min()))**2 +
      ((X_train[:,3].min()) / (X_train[:,3].max() - X_train[:,3].min()))**2)