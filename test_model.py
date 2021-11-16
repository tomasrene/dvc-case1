import pandas as pd
from sklearn.metrics import accuracy_score, f1_score
import pickle
import json

def main():
    # open saved model
    with open("model.pickle","rb") as f:
        model = pickle.load(f)

    # open test data
    data = pd.read_csv("data_test.csv")    

    # do some processing
    X,y = process(data)

    # get metrics from predictions
    metrics = test(X,y,model)

    # save to JSON file
    save_result(metrics)

def process(data):
    # boring preprocessing
    X,y = data.iloc[:,:-1], data.iloc[:,-1]
    
    return X,y

def test(X,y,model):
    # using model to predict
    y_predicted = model.predict(X)

    # gathering metrics
    metrics = {
        'accuracy': round(accuracy_score(y,y_predicted),4),
        'f1_score': round(f1_score(y,y_predicted),4)
    }
    
    return metrics

def save_result(metrics):
    # save results to JSON file
    with open("metrics.json",'w') as f:
        json.dump(metrics,f)    

if __name__ == "__main__":
    main()
