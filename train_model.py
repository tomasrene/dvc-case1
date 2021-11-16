import pandas as pd
from sklearn.linear_model import LogisticRegression
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
    lr = LogisticRegression()

    # fitting to data
    lr.fit(X,y)

    return lr

def save_model(model):
    # pickling model
    with open("model.pickle","wb") as f:
        pickle.dump(model,f)

if __name__ == "__main__":
    main()
