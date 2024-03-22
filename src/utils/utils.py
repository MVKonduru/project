import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.logger.logger import logging
from src.exception.exception import customexception
from sklearn.metrics import precision_score,recall_score,  accuracy_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise customexception(e, sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        logging.info(training)
        for i in range(len(models)):
            logging.info("training with ",models.values[i])
            model = list(models.values())[i]
            # Train model
            model.fit(X_train,y_train)

            

            # Predict Testing data
            y_test_pred =model.predict(X_test)

            # Get R2 scores for train and test data
            #train_model_score = r2_score(ytrain,y_train_pred)
            test_model_score_accuracy = accuracy_score(y_test,y_test_pred)
            test_model_score_precision = precision_score(y_test,y_test_pred)
            test_model_score_recall = recall_score(y_test,y_test_pred)

            report[list(models.keys())[i]] =  (test_model_score_accuracy,
                                                test_model_score_precision,
                                                test_model_score_recall)

        return report

    except Exception as e:
        logging.info('Exception occured during model training')
        raise customexception(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise customexception(e,sys)

    