from flask import Flask,render_template,redirect,session,request

app=Flask(__name__)
app.secret_key = "secret"
@app.route('/')
def home():
    if 'counter' not in session:
        session['counter'] =1
    else:
        session['counter']+=1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)