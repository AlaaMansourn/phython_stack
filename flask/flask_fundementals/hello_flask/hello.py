from flask import Flask  
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'

@app.route('/dojo')          
def hello_dojo():
    return 'Hello dojo'

@app.route('/say/<name>')          
def hello_name(name):
    for i in name:
        return 'Hi '+name

@app.route('/repeat/<times>/<word>')
def repeat_word(times,word):
    string=""
    for i in range(int(times)):
        string+="<p>" + word + "</p>"
    return string





 
if __name__=="__main__":     
    app.run(debug=True) 