from flask import Flask,Jsonify,request
app= Flask(__name__)
stores=[
    {
        'name': "my wonderful store",
        'items':[
            {
            'name':"item name",
            'price':52000
            }
            
        ]
    }
]
@app.route('/')
def home():
    return "Hello,World"
# creating a POST/store data:{name} end piont
@app.route('/store',methods=['POST'])
def create_stores():
    request_data=request.get_json()
    new_store={
        'name':request_data['name'],
        'items':[]
    }
    store.append(new_stores)
    return jsonify(new_store)
    
# creating a GET/store/<string:name> end point
@app.route('/store/<string:name>')
def get_store(name):
    for store  in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message':'store not found'})
# creating a GET/store end point
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})
#creating a POST/store/<string:name>/item{name} endpiont
@app.route('/store/<string:name>/item',method=['POST'])
def create_item_in_store(name):
    request_data=request.get_json()
    for store in stores:
        if store['name']==name:
            new_item={
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
            
    return jsonify({'message':'store not found'})    
# creating a GET/store/<string:name>/item endpoint 
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name']==item:
            return jsonify({'items':store['items']})
    return jsonify({'message':'store not found'})

