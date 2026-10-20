import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()

#print(iris)

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df.head()

df = df.sample(frac=1).reset_index(drop=True)

#print(df)
train = df.iloc[:120]
test = df.iloc[120:]

x_train = train.drop(columns=["target"], axis=1)
x_test = test.drop(columns=["target"], axis=1)

y_train = train["target"]
y_test = test["target"]

y_pred=y_test.copy(deep=True)
    
for index, row in x_test.iterrows():
    a = ((x_train - row)**2).sum(axis=1).sort_values()[:5].index
    a = y_train.iloc[a].mode()[0]

    y_pred[index] = a

    #print(a)

    # curr_train = x_train
    # curr_train = curr_train - [row[1], row[2], row[3], row[4]]

    # curr_train = curr_train**2
    # curr_train['sum'] = curr_train.sum(axis=1)

    # #print(curr_train)
    # curr_train = curr_train.sort_values("sum")

    # our_indexes = curr_train[:5].drop(columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])
    # print(our_indexes)

    # print(y_train.iloc[our_indexes.index])

    

    #ans = y_train().index(our_indexes[0])

    #print(our_indexes)

print((y_test == y_pred).mean())


