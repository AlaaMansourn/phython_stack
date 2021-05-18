from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/results',methods=['POST'])
def create_survey():
    
    name=request.form['name']
    loc=request.form['loc']
    language=request.form['language']
    optional=request.form['optional']

    return render_template('result.html',name=name,loc=loc,language=language,optional=optional)

if __name__=="__main__":
    app.run(debug=True)


