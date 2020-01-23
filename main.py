#!/usr/bin/python3
import csv, json
from settings import *
from request import *


file_csv = open('spreadsheets/inicial.csv')

def insertExamples():
    print("starting the post test on your bothub repository...\n")
    for message in csv.DictReader(file_csv):
        
        text = message["text"]
        intent = message["intent"]
        postExample(text, intent)
        print(message["text"])

def insertTests():
    pass

def categorize():
    pass

print("#####WELCOME TO AI SPREADSHEET CONVERTER#####")

if SERVICE_TYPE == 'test':
    print("starting the post test on your bothub repository...\n")
    insertTests()

elif SERVICE_TYPE == 'categorize':
    print("")
    categorize()

elif SERVICE_TYPE == 'examples':
    print()
    insertExamples()