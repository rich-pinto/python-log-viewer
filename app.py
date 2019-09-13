import flask
import subprocess
import time 
import os
import sys

global file_path
file_path = './logfile'

app = flask.Flask(__name__)

@app.route('/')
def home():
  return '''
   <style> 
  	textarea {
  	width: 50%;
  	height: 50px;
  	padding: 12px 20px;
  	box-sizing: border-box;
  	border: 2px solid #ccc;
  	border-radius: 4px;
  	background-color: #f8f8f8;
  	font-size: 16px;
  	resize: none;
  	}
        input {
	width: 10%;
	height: 30px;
	#padding: 12px 20px;
        box-sizing: border-box;
        border: 2px solid #ccc;
        border-radius: 4px;
        background-color: #f8f8f8;
        font-size: 16px;
        resize: none;
	text-align: center;
	}
   </style>
   <form method="POST" action="/view_logs">
    <textarea name="textbox">Please enter the logfile path including the filename. Default is ./logfile</textarea>
    <input type="submit" name="submit" value="Submit" class="text-right"/>
   </form> 
   '''
@app.route('/view_logs', methods=['POST'])
def view_logs_post():
  path = flask.request.form['textbox']
  global file_path
  file_path = path
  assert os.path.isfile(path), "I did not find the file at the entered location! Please enter a valid path"
  def inner():
        command = "less +F %s" % (path)
        proc = subprocess.Popen(
	    command,
            shell=True,
            stdout=subprocess.PIPE
        )

        for line in iter(proc.stdout.readline,''):
            time.sleep(1)                           # text delay for a streaming view
            yield line.rstrip() + '<br/>\n'

  return flask.Response(inner(), mimetype='text/html')

@app.route('/view_logs', methods=['GET'])
def view_logs_get():
  path = file_path
  assert os.path.isfile(path), "I did not find the file at the entered location! Please enter a valid path"
  def inner():
        command = "less +F %s" % (path)
        proc = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE
        )

        for line in iter(proc.stdout.readline,''):
            time.sleep(1)                           # text delay for a streaming view
            yield line.rstrip() + '<br/>\n'

  return flask.Response(inner(), mimetype='text/html')
app.run(debug=True, port=5020, host='0.0.0.0')
