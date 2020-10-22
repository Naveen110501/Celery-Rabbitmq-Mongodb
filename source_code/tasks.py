from celery import Celery
import pandas as pd


app = Celery('tasks', broker = 'amqp://localhost', backend = 'mongodb+srv://naveen:good@cluster0.jhu84.mongodb.net/test' )


@app.task
def deleting_column(x,y):
    cut_off = pd.read_csv("TNEA_2018.csv")
    cut_off.drop(cut_off.columns[[x,y]],axis = 1, inplace = True)
    return cut_off.to_json()


