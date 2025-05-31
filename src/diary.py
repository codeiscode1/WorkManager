from tkinter import Tk,Toplevel,Label
from datetime import datetime
from pandas import DataFrame,read_csv,errors
from tkcalendar import DateEntry

app = Tk()

def diary(tkinter_app):
    try :
        diary_entries = read_csv("diary.csv").to_dict(orients = "records")
    except FileNotFoundError :
        with open("diary.csv", "w" ) as f :
            f.close()
    except errors.EmptyDataError :
        diary_entries = []
    app_diary = Toplevel(tkinter_app)
    a = Label(app_diary,text="Welcome to your diary.")
    a.grid(row = 0, column = 0)
    diary_date_entry_text = Label(app_diary,text="Please Enter Date:")
    diary_date_entry_text.grid(row=1,column=0)
    diary_date_entry = DateEntry(app_diary)
    diary_date_entry.grid(row=1,column=0)
