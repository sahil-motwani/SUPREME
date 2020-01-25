# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 23:02:20 2020

@author: USER
"""


import requests
import json
print("enter the hash you want to store in the blockchain")
hash=input()
dictToSend = {'sender':'3d7b318e462c4c09acc554607d6d342d','recipient':'someone-other-address','amount':hash}
res = requests.post('http://localhost:5000/transactions/new',json=dictToSend)
print('response from server:',res.text)
res = requests.get('http://localhost:8000/mine')
print(res)
data=res.json()
i=data['transactions'][0]
print(i)
