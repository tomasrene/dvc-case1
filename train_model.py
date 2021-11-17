import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import pickle
import yaml
from yaml.loader import FullLoader

def main():
    # get train data
    data = pd.read_csv("data_train.csv")

    with open("params.yaml","r") as f:
        params = yaml.safe_load(f)

    # do some processing
    X,y = process(data)

    # create model
    model = train(X,y,params['train_model'])

    # save pickled model
    save_model(model)

def process(data):
    # some boring preprocessing
    X,y = data.iloc[:,:-1], data.iloc[:,-1]
    
    return X,y

def train(X,y,params):
    # create model
    model = DecisionTreeClassifier(**params)

    print(model)

    # fitting to data
    model.fit(X,y)

    return model

def save_model(model):
    # pickling model
    with open("model.pickle","wb") as f:
        pickle.dump(model,f)

if __name__ == "__main__":
    main()
