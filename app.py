from flask import Flask, render_template, request
from pusher import Pusher


app = Flask(__name__)

pusher = Pusher(
  app_id='964516',
  key='517d6d06f71fb261e05e',
  secret='ccb4512730a9a0447c7c',
  cluster='ap1',
  ssl=False
)

#pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route("/orders", methods=["POST"])
def order():
    data = request.form
    pusher.trigger('message', 'place', {
        "units": data['units']
    })
    
    return "units logged"

@app.route('/message', methods=["POST"])
def message():
    data = request.form
    
    pusher.trigger('message', 'send', {
        "name": data["name"],
        "message": data["message"]
    })
    
    return "message sent"

@app.route('/customer', methods=["POST"])
def customer():
    data = request.form
    
    pusher.trigger('customer', 'add',{
        "name": data["name"],
        "position": data["position"],
        "office": data["office"],
        "age": data["age"],
        "salary": data["salary"]
    })
    
    return "customer added"


if __name__ == '__main__':
    app.run(debug=True)