from flask import Flask, render_template, request, url_for;

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('text-submit.html')
	
@app.route('/form', methods=['GET', 'POST'] )
def test():
	if request.method=='GET':
		text_to_filter= request.args.get('text_to_check')
		return "OK this is a get method" + text_to_filter
		
	elif request.method=='POST':
		#return "OK this is a post method"
		text_to_filter = request.form['text_to_check']
		if (text_to_filter.lstrip().rstrip() == ''):
			return render_template('text-submit.html')
			
		return render_template('text-results.html', text_to_filter=text_to_filter)
		
	else:
		return("ok")


if __name__ == "__main__":
    app.run()