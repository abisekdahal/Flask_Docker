from flask import Flask ,jsonify,render_template,request
from flask_restful import Api, Resource

app=Flask(__name__)
api=Api(app)
def checkfun(get_value,value):
    if (value=='ADD' or value=='SUB' or  value=='MUL'):
        if "x" not in get_value or "y" not in get_value:
            return 301
        else:
            return 200
    elif(value=='DIV'):

        if "x" not in get_value or "y" not in get_value:
            return 301

        elif (get_value['y'])==0:
            react = {
                    "Mesasge": "Error",
                    "Status": "Can't Divisible"
            }
            return react
        else:
            return 200
class Add(Resource):
    def post(self):
        get_value=request.get_json()
        get_s= checkfun(get_value,'ADD')
        if(get_s!=200):
            retjsa={
                "Message":"Error ",
                "Status Code":get_s

            }
            return retjsa

        x=get_value['x']
        y=get_value['y']
        x=int(x)
        y=int(y)
        value=x+y
        ret_json={
            "Message ":value,
            "Status Code":200
        }
        return jsonify(ret_json)


class Substract(Resource):
    def post(self):
        get_value=request.get_json()
        get_s= checkfun(get_value,'SUB')
        if(get_s!=200):
            retjsa={
                "Message":"Error ",
                "Status Code":get_s

            }
            return retjsa

        x=get_value['x']
        y=get_value['y']
        x=int(x)
        y=int(y)
        value=x-y
        ret_json={
            "Message ":value,
            "Status Code":200
        }
        return jsonify(ret_json)



class Div(Resource):
    def post(self):
        get_value=request.get_json()
        get_s= checkfun(get_value,'DIV')
        if(get_s!=200):
            retjsa={
                "Message":"Error ",
                "Status Code":get_s

            }
            return retjsa

        x=get_value['x']
        y=get_value['y']
        x=int(x)
        y=int(y)
        value=x/y
        ret_json={
            "Message ":value,
            "Status Code":200
        }
        return jsonify(ret_json)

class Mul(Resource):
    def post(self):
        get_value=request.get_json()
        get_s= checkfun(get_value,'MUL')
        if(get_s!=200):
            retjsa={
                "Message":"Error ",
                "Status Code":get_s

            }
            return retjsa

        x=get_value['x']
        y=get_value['y']
        x=int(x)
        y=int(y)

        value=x*y
        ret_json={
            "Message ":value,
            "Status Code":200
        }
        return jsonify(ret_json)



api.add_resource(Add,'/ADD')
api.add_resource(Substract,'/SUB')
api.add_resource(Div,'/DIV')
api.add_resource(Mul,'/MUL')


@app.route('/')
def home():
    return "Home Page"
if __name__=="__main__":
    app.run(debug=True)


