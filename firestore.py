# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:47:31 2020

@author: Jack
"""
import os
import csv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#firestore
# 引用私密金鑰
cred = credentials.Certificate('cht-iot-81bb9-firebase-adminsdk-mcyo1-f485f36332.json') #Firestore金鑰
# 初始化firebase，注意不能重複初始化
try:
    firebase_admin.initialize_app(cred)
except:
    print("重複初始化")    
# 初始化firestore
db = firestore.client()

for csv_name in os.listdir('./csv'):
    print(csv_name)
    with open(os.path.join('./csv',csv_name), 'r', newline='') as csvfile:
        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)
        doc = {}
        # 以迴圈輸出每一列
        for row in rows:
          if row[0] != 'date':
              doc_ref = db.collection(csv_name[:-4]).document(row[0])
              doc['Dissolved']=row[1]
              doc['pH_value']=row[2]
              doc['oxidation-reduction_potential']=row[3]
              doc['salinity']=row[4]
              doc['temperature']=row[5]
              doc_ref.set(doc)
