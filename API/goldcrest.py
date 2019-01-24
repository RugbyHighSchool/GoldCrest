from flask import Flask
from flask_restful import Api, Resource, reqparse

import csv, time
from datetime import datetime

app = Flask(__name__)
api = Api(app)

energyUsage = {}

with open('alldata.csv', newline='') as data:
    for row in csv.reader(data):
        energyUsage[int(time.mktime(datetime.strptime(row[0], "%d/%m/%Y %H:%M:%S").timetuple()))] = float(row[1])

class Price(Resource):
    def get(self, timestamp):
        if timestamp in energyUsage:
            return {
                "datetime": datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'),
                "current_price" : energyUsage[timestamp],
            }, 200
        else:
            return "Timestamp Not Found; Check you are in Unix Time.", 404


class Prices(Resource):
    def get(self):
        return energyUsage, 200

class History(Resource):
    def get(self, timestamp):
        parser = reqparse.RequestParser()
        parser.add_argument("histories")
        args = parser.parse_args()

        history = []

        for i in range(1, int(args["histories"])):
            history.append(energyUsage[timestamp - (i * 30 * 60)])

        return {
            "datetime": datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'),
            "current_price" : energyUsage[timestamp],
            "history": history
        }, 200

api.add_resource(Price, "/price/<int:timestamp>")
api.add_resource(Prices, "/prices")
api.add_resource(History, "/price_history/<int:timestamp>")
app.run(debug=True)
