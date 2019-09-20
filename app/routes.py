from app import app
import json
from flask import (
    render_template,
    redirect, url_for,
    request, make_response 
)

from app import engine as eng

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('text'))
    except TypeError:
        data = {}
    return data

def check_key(dictionary, key):

    if key in dictionary.keys():
        return True
    return False

@app.route('/')
def index():
    data = get_saved_data()
    pol = None
    sub = None
    pol_statement = None
    sub_statement = None
    if check_key(data, 'text'):
        pol = eng.polarity(data['text'])
        sub = eng.subjectivity(data['text'])
        pol_statement = eng.polarity_statement(data['text'])
        sub_statement = eng.subjectivity_statement(data['text'])
    context = {
        'polarity': pol, 
        'subjectivity': sub, 
        'data': data,
        'pol_statement': pol_statement,
        'sub_statement': sub_statement
    }
    return render_template('index.html', **context)

@app.route('/save', methods=['POST'])
def save():
    response = make_response(redirect(url_for('index')))
    # Check if a cookie already exists and retrieve it
    data = get_saved_data()
    # If the cookie exists, only update the values that have changed
    data.update(dict(request.form.items()))
    # Set the cookie
    response.set_cookie('text', json.dumps(data))
    return response