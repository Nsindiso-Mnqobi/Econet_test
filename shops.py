import csv
from flask import Flask, request, jsonify

app = Flask(__name__)

#class api_end_points:
 #   @app.route("/", method = ['POST'])
  #      def input_variables: 


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
    area = (input("What is the  area: "))
    shop = (input("What is the shop name:  "))
    li_st = [area,shop]
    econet = econet_shops(li_st)
    econet.insert_shop()
    
