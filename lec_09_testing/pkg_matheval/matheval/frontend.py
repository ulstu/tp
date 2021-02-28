#!python3

from flask import Flask, request

from matheval.evaluator import math_eval

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    tree = request.get_json(force=True)
    result = math_eval(tree);
    return str(result) + "\n"

if __name__ == '__main__':
    app.run(debug=True)


#curl -i -H "Content-Type: application/json" charset=utf-8 -X POST --data '["+", 5, 7]' 127.0.0.1:5000/