import json
import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from mcqgenerator.utils import read_file,get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from mcqgenerator.MCQGenerator import generate_evaluate_chain

#loading json file
with open('D:\projectt1\Response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

#print(RESPONSE_JSON)