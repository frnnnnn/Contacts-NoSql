from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import re

import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import *


myclient = pymongo.MongoClient(
    "mongodb+srv://gdtall:LtjjDyRa0S06jneh@cluster0.ysnuirr.mongodb.net/?retryWrites=true&w=majority"
)
mydb = myclient["telefono"]
mycol = mydb["contactos"]


