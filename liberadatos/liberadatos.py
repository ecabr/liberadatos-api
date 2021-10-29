from flask import Flask, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)
app.config["DEBUG"] = True

def load_contributions():
    return pd.read_csv('datasets/aportes_pres_parlam_cores.csv')

def load_datasets():
    datasets = {}
    datasets['contributions'] = load_contributions().fillna('')
    return datasets

@app.route('/api/v1/elections/2021/contributions', methods=['GET'])
def get_contributions():
    # TODO: Apply filters if needed
    contributions = datasets['contributions'].to_dict('index')
    return jsonify(contributions)

datasets = load_datasets()
app.run()