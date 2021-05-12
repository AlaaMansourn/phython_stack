from flask import Flask,render_template
app = Flask(__name__)



@app.route('/play')
@app.route('/play/<int:times>')
@app.route('/play/<int:times>/<color>')
def dispaly_box(times=3,color='blue'):
 return render_template('index.html',times=times,color=color)

if __name__ =="__main__":
    app.run(debug=True)



