from flask import Flask  
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'

@app.route('/dojo')          
def hello_dojo():
    return 'Hello dojo'

@app.route('/<name>')          
def hello_name():
    for i in name:
        return 'Hi'+name





 
if __name__=="__main__":     
    app.run(debug=True) 