import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import pickle

def main():
    # get train data
    data = pd.read_csv("data_train.csv")    

    # do some processing
    X,y = process(data)

    # create model
    model = train(X,y)

    # save pickled model
    save_model(model)

def process(data):
    # some boring preprocessing
    X,y = data.iloc[:,:-1], data.iloc[:,-1]
    
    return X,y

def train(X,y):
    # create model
    model = DecisionTreeClassifier()

    # fitting to data
    model.fit(X,y)

    return model

def save_model(model):
    # pickling model
    with open("model.pickle","wb") as f:
        pickle.dump(model,f)

if __name__ == "__main__":
    main()
