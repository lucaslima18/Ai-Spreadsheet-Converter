#!/usr/bin/python3
import csv, json
from settings import *
from request import *


file_csv = open("spreadsheets/inicial.csv")
categorize_csv = open("spreadsheets/categorize.csv")
categorized_sentences_csv = open("spreadsheets/categorized_sentences.csv", 'w')
categorized_sentences_csv.write("text,intent,confidence\n")


def insertExamples():
    print("starting the post examples on your bothub repository...\n")
    for message in csv.DictReader(file_csv):

        text = message["text"]
        intent = message["intent"]
        postExample(text, intent)
        print(message["text"])


def insertTests():
    print("starting the post tests on your bothub repository...\n")
    for message in csv.DictReader(file_csv):

        text = message["text"]
        intent = message["intent"]
        postTests(text, intent)
        print(message["text"])

def categorize():
    for message in csv.DictReader(categorize_csv):
        text = message["text"]
        function = categorizeText(text)
        intent = next(function)
        confidence = next(function)
        print(f"{text}: intent: {intent}, confidence:, {confidence}")
        categorized_sentences_csv.write(f"{text},{intent},{confidence}\n")


print("#####WELCOME TO AI SPREADSHEET CONVERTER#####")

if SERVICE_TYPE == "test":
    print("starting the post test on your bothub repository...\n")
    insertTests()

elif SERVICE_TYPE == "categorize":
    categorize()

elif SERVICE_TYPE == "examples":
    print()
    insertExamples()
