from flask import Flask,render_template,request,redirect,url_for,jsonify
app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return "Hello, sumil this is deployed from cloud run!"

@app.route("/index",methods=["GET"])
def index():
    return "Hello, index!"

@app.route('/sucess/<score>')
def sucess(score):
    return "the person has pass and score are :" + score

@app.route('/fail/<score>')
def fail(score):
    return "the person has fail and score are :" + score

@app.route("/form",methods=["GET", "POST"])
def form():
    if request.method=="GET":
      return render_template('form.html')
    else:
        math=float(request.form['math'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(math+science+history)/3

        res=""
        if average_marks>=50:
            res="sucess"
        else:
            res="fail"

        return redirect(url_for(res,score=average_marks))

@app.route('/api', methods=['post'])

def calculate_sum():
    data=request.get_json()
    a_value=float(dict(data)['a'])
    b_value=float(dict(data)['b'])

    return jsonify(a_value+b_value)

       # return render_template('form.html',score=average_marks)


if __name__=="__main__":
    app.run(host ='0.0.0.0', port = 8080, debug=True)

