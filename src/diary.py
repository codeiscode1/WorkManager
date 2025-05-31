from tkinter import Tk,Toplevel,Label
from datetime import datetime
from pandas import DataFrame,read_csv
from tkcalendar import DateEntry

app = Tk()

def diary(tkinter_app):
    app_diary = Toplevel(tkinter_app)
    a = Label(app_diary,text="Welcome to your diary.")
