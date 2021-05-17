from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users',methods=['POST'])
def create_users():
    print("post:info")
    print(request.form)
    name=request.form['name']
    return render_template('show.html',name=name)




if __name__=="__main__":
    app.run(debug=True)


