from flask import Flask, render_template,request,redirect
import csv

app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		line = 'email -> ' + email + ' subject -> ' + subject + ' message -> ' + message + '\n'
		database.write(line)

def write_to_csv(data):
	with open('database.csv', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database, delimiter=',', lineterminator='\n', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'something went wrong'

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.run()