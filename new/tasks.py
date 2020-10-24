from celery import Celery
import pandas as pd

# backend = 'mongodb+srv://naveen:good@cluster0.jhu84.mongodb.net/test' 

app = Celery('tasks', broker = 'amqp://localhost')


@app.task
def deleting_column(x,y):
     #x,y = input().split()
     #x=input("enter the first column to be deleted")
     #y=input("enter the first column to be deleted")
     cut_off = pd.read_csv("TNEA_2018.csv")
     cut_off.drop(cut_off.columns[[x,y]],axis = 1, inplace = True)
     return cut_off.to_json()


