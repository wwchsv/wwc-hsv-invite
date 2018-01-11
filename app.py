#!flask/bin/python
from flask import Flask, jsonify
import requests

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

TOKEN = os.environ.get('OTHER', None)

@app.route('/')
def index():
    return "Hello, World!"
	
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
	
@app.route('/slack-invite/, methods=['POST'])
def invite_slack():
	if not request.json or not 'address' in request.json:
		abort(400)
		
	data = {}
	data["email"] = request.json.address
	data["token"] = requests.json.address
	data["set_active"] = true
	
	payload = jsonify(data)
	
	response = requests.post('https://wwchsv.slack.com/api/users.admin.invite/', data = payload)
	response.text

if __name__ == '__main__':
    app.run(debug=True)