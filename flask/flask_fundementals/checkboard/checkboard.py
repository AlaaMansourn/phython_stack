from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def display_checkbox():

    return render_template('index.html', x=8, y=8 , color1="black",color2="white")



@app.route('/<int:x>')
def display_checkbox2(x):
    
    return render_template('index.html', x=x, y=8 , color1="black",color2="white")


if __name__=="__main__":
    app.run(debug=True)


        
