from flask import Flask, render_template , jsonify

app = Flask(__name__)



JOBS =[
{
  'id':1,
  'title':'Data analyst',
  'location':'NIT NAGALAND',
'salary':'Rs.1000000'

},
{
  'id':2,
    'title':'Data scientist',
    'location':'BENGULURU',
  'salary':'Rs.1500000'
},
{
  'id':3,
    'title':'Toilet cleaner',
    'location':'Dubai',
  'salary':'Rs.500000'
},
{
  'id':4,
    'title':'fronted engineer',
    'location':'BENGULURU',
  
}
]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)
@app.route("/api/jobs")
def list_jobs():
  return jsoniy(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
