
# coding: utf-8

# In[1]:

import pandas as pd
import pymysql
import warnings
import time

warnings.filterwarnings("ignore")
######live database connection
from sqlalchemy import create_engine
cnx = create_engine('mysql+pymysql://Ajit:T8Zy4ZnDDNqYw2Cm@sttash-website-new-main-live.c3mhtvbf3juk.ap-south-1.rds.amazonaws.com:3306/Data_Analytics', echo=False)

stashln = pd.read_excel("D:\\Ajit Singh\\Reporting\\Collections\\PTP\\20190313.xlsx")
stashln.head

stashln.to_sql('Collections_PTP_Cases', con = cnx, if_exists='replace', index=False, chunksize = 1000)

