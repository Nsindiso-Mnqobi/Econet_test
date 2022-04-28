import csv
from flask import Flask, request, jsonify

app = Flask(__name__)

class Api:
    
    @app.route('/add_area/<name:string>', method = ['GET','POST'])
    def get_area(area):
        if (request.method == "POST"):
            area = request.get_json()
            return jsonify({'Your area : name' : area})
            return area
        else:
            return jsonify({'Only ': 'POST DATA'})
        
    @app.route('/add_name/<name:string>', method = ['GET','POST'])
    def get_name(name):
        if (request.method == "POST"):
            name = request.get_json()
            return jsonify({'Your area : name' :  + name})
            return name
        else:
            return jsonify({'Only ': 'POST DATA'})

class econet_shops:

    def __init__(self,shop):
        self.shop = list(shop)

    ''' create a service for inserting a shop under any area inserted in your database
     and expose the service through a rest endpoint '''
    
    def  insert_shop (self):
        header = ['Area Name','Shop Name ']
        rows = [['CBD','Eco']]
        rows.append(self.shop)
        with open("database.csv", 'w') as shops_database:
            shops= csv.writer(shops_database)
            shops.writerow(header)
            shops.writerows(rows)
        
if  __name__ == "__main__":
    api = Api()
    area = api.get_area()
    shop = api.get_name()
    li_st = [area,shop]
    econet = econet_shops(li_st)
    econet.insert_shop()
    
