#!/usr/bin/python
import os
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

class UberPriceEstimate(object):
	SERVER_TOKEN = os.environ.get('UBER_SERVER_TOKEN') 
	def __init__(self):
		self.session = Session(server_token=UberPriceEstimate.SERVER_TOKEN) 
		self.client = UberRidesClient(self.session)

	def getProducts(self, type, lat, long):
		response = self.client.get_products(lat, long)
		products = response.json.get('products')
		for product in products:
			if product["display_name"] == type:
				return product
		return None
	def getEstimate(self, product, startLat, startLong, endLat, endLong):
		estimate = self.client.estimate_ride( product_id=product.get('product_id'), start_latitude=startLat, start_longitude=startLong, end_latitude=endLat, end_longitude=endLong )
		print estimate

#uber = UberPriceEstimate()
#product = uber.getProducts("POOL", 37.5334522, -122.2718777)
#print uber.getEstimate(product, 37.5334522, -122.2718777, 37.4059503, -121.9399195)
#print uber.getEstimate(product, 37.770, -122.411, 37.791, -122.405)

session = Session(server_token=os.environ.get('UBER_SERVER_TOKEN'))
client = UberRidesClient(session, sandbox_mode=True)
response = client.get_products(37.77, -122.41)
products = response.json.get('products')
print products
estimate = client.estimate_ride(
    product_id=products[0].get('product_id'),
    start_latitude=37.770,
    start_longitude=-122.411,
    end_latitude=37.791,
    end_longitude=-122.405
)
print estimate
