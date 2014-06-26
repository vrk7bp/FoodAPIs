#!/usr/bin/python

from factual import Factual
import json

KEY = "4RVd3PBB9wVnoiRTUbGe5bdAXVTCVfClPKKvarLu"
SECRET = "IK4klSaSGQnWlkYJQIDYLjU5QEhmGIPxZqFdc83L"

# Phone Number has to be in (XXX) XXX-XXXX format
def getFactualData(phoneNumber):
	factual = Factual(KEY, SECRET)
	table = factual.table('restaurants-us')

	filterMap = {}
	filterMap['tel'] = phoneNumber

	q1 = table.filters(filterMap)
	FactualMap = q1.data()[0]
	print FactualMap
	print "-----------------------------"
	print q1.data()[0]
	print "-----------------------------"
	print 'Factual Data:'

	try: 
		print '\tFactual Name: ' + FactualMap['name']
	except:
		print '\tFactual Name: No Data'

	try: 
		print '\tFactual Address: ' + FactualMap['address']
	except:
		print '\tFactual Address: No Data'

	try: 
		print '\tFactual Address Extended: ' + str(FactualMap['address_extended'])
	except:
		print '\tFactual Address Extended: No Data'

	try: 
		print '\tFactual Locality: ' + FactualMap['locality']
	except:
		print '\tFactual Locality: No Data'

	try: 
		print '\tFactual Neighborhood: ' + str(FactualMap['neighborhood'])
	except:
		print '\tFactual Neighborhood: No Data'

	try: 
		print '\tFactual Region: ' + FactualMap['region']
	except:
		print '\tFactual Region: No Data'

	try: 
		print '\tFactual Postal Code: ' + FactualMap['postcode']
	except:
		print '\tFactual Postal Code: No Data'

	try: 
		print '\tFactual Latitude: ' + str(FactualMap['latitude'])
	except:
		print '\tFactual Latitude: No Data'

	try: 
		print '\tFactual Longitude: ' + str(FactualMap['longitude'])
	except:
		print '\tFactual Longitude: No Data'

	try: 
		print '\tFactual Telephone: ' + FactualMap['tel']
	except:
		print '\tFactual Telephone: No Data'

	try: 
		print '\tFactual Chain ID: ' + FactualMap['chain_id']
	except:
		print '\tFactual Chain ID: No Data'

	try: 
		print '\tFactual Chain Name: ' + FactualMap['chain_name']
	except:
		print '\tFactual Chain Name: No Data'

	try:
		print '\tFactual Category IDs: ' + str(FactualMap['category_ids'])
	except:
		print '\tFactual Category IDs: No Data'

	try:
		print '\tFactual Labels: ' + str(FactualMap['category_labels'])
	except:
		print '\tFactual Labels: No Data'

	try:
		print '\tFactual Website: ' + FactualMap['website']
	except:
		print '\tFactual Website: No Data'

	try:
		print '\tFactual Email: ' + str(FactualMap['email'])
	except:
		print '\tFactual Email: No Data'

	try:
		print '\tFactual Cuisines: ' + str(FactualMap['cuisine'])
	except:
		print '\tFactual Cuisines: No Data'

	try:
		print '\tFactual Price: ' + str(FactualMap['price'])
	except:
		print '\tFactual Price: No Data'

	try:
		print '\tFactual Rating: ' + str(FactualMap['rating'])
	except:
		print '\tFactual Rating: No Data'

	try:
		print '\tFactual Cash Only: ' + str(FactualMap['payment_cashonly'])
	except:
		print '\tFactual Cash Only: No Data'

	try:
		print '\tFactual Reservations: ' + str(FactualMap['reservations'])
	except:
		print '\tFactual Reservations: No Data'

	try:
		print '\tFactual Hours: ' + FactualMap['hours_display']
	except:
		print '\tFactual Hours: No Data'

	try:
		print '\tFactual 24 Hours: ' + str(FactualMap['open_24hrs'])
	except:
		print '\tFactual 24 Hours: No Data'

	try:
		print '\tFactual Attire: ' + FactualMap['attire']
	except:
		print '\tFactual Attire: No Data'

	try:
		print '\tFactual Parking: ' + str(FactualMap['parking'])
	except:
		print '\tFactual Parking: No Data'

	try:
		print '\tFactual Smoking: ' + str(FactualMap['smoking'])
	except:
		print '\tFactual Smoking: No Data'

	try:
		print '\tFactual Breakfast: ' + str(FactualMap['meal_breakfast'])
	except:
		print '\tFactual Breakfast: No Data'

	try:
		print '\tFactual Lunch: ' + str(FactualMap['meal_lunch'])
	except:
		print '\tFactual Lunch: No Data'

	try:
		print '\tFactual Dinner: ' + str(FactualMap['meal_dinner'])
	except:
		print '\tFactual Dinner: No Data'

	try:
		print '\tFactual Deliver: ' + str(FactualMap['meal_deliver'])
	except:
		print '\tFactual Deliver: No Data'

	try:
		print '\tFactual Takeout: ' + str(FactualMap['meal_takeout'])
	except:
		print '\tFactual Takeout: No Data'

	try:
		print '\tFactual Cater: ' + str(FactualMap['meal_cater'])
	except:
		print '\tFactual Cater: No Data'

	try:
		print '\tFactual Alcohol: ' + str(FactualMap['alcohol'])
	except:
		print '\tFactual Alcohol: No Data'

	try:
		print '\tFactual GoodForKids: ' + str(FactualMap['kids_goodfor'])
	except:
		print '\tFactual GoodForKids: No Data'

	try:
		print '\tFactual WiFi: ' + str(FactualMap['wifi'])
	except:
		print '\tFactual WiFi: No Data'

	try:
		print '\tFactual Vegetarian: ' + str(FactualMap['options_vegetarian'])
	except:
		print '\tFactual Vegetarian: No Data'

	try:
		print '\tFactual Vegan: ' + str(FactualMap['options_vegan'])
	except:
		print '\tFactual Vegan: No Data'

	try:
		print '\tFactual Gluten Free: ' + str(FactualMap['options_glutenfree'])
	except:
		print '\tFactual Gluten Free: No Data'

	try:
		print '\tFactual Low Fat: ' + str(FactualMap['options_lowfat'])
	except:
		print '\tFactual Low Fat: No Data'

	try:
		print '\tFactual Organic: ' + str(FactualMap['options_organic'])
	except:
		print '\tFactual Organic: No Data'

	try:
		print '\tFactual Healthy: ' + str(FactualMap['options_healthy'])
	except:
		print '\tFactual Healthy: No Data'

	try:
		print '\tFactual ID: ' + FactualMap['factual_id']
	except:
		print '\tFactual ID: No Data'

	try:
		print '\tFactual URL: ' + q1.get_url()
	except:
		print '\tFactual URL: No Data'

def main():
    factual = Factual(KEY, SECRET)
    
    table = factual.table('restaurants-us')
    
    q1 = table.filters({"tel":"(434) 872-0212"})
    FactualMap = q1.data()[0]
    print 'Factual Data:'

    try: 
    	print '\tFactual Name: ' + FactualMap['name']
    except:
    	print '\tFactual Name: No Data'

    try: 
    	print '\tFactual Address: ' + FactualMap['address']
    except:
    	print '\tFactual Address: No Data'

    try: 
    	print '\tFactual Address Extended: ' + FactualMap['address_extended']
    except:
    	print '\tFactual Address Extended: No Data'

    try: 
    	print '\tFactual Locality: ' + FactualMap['locality']
    except:
    	print '\tFactual Locality: No Data'

    try: 
    	print '\tFactual Neighborhood: ' + FactualMap['neighborhood']
    except:
    	print '\tFactual Neighborhood: No Data'

    try: 
    	print '\tFactual Region: ' + FactualMap['region']
    except:
    	print '\tFactual Region: No Data'

    try: 
    	print '\tFactual Postal Code: ' + FactualMap['postcode']
    except:
    	print '\tFactual Postal Code: No Data'

    try: 
    	print '\tFactual Latitude: ' + FactualMap['latitude']
    except:
    	print '\tFactual Latitude: No Data'

    try: 
    	print '\tFactual Longitude: ' + FactualMap['longitude']
    except:
    	print '\tFactual Longitude: No Data'

    try: 
    	print '\tFactual Telephone: ' + FactualMap['tel']
    except:
    	print '\tFactual Telephone: No Data'

    try: 
    	print '\tFactual Chain ID: ' + FactualMap['chain_id']
    except:
    	print '\tFactual Chain ID: No Data'

    try: 
    	print '\tFactual Chain Name: ' + FactualMap['chain_name']
    except:
    	print '\tFactual Chain Name: No Data'

	try:
		print '\tFactual Category IDs: ' + str(FactualMap['category_ids'])
	except:
		print '\tFactual Category IDs: No Data'

	try:
		print '\tFactual Labels: ' + str(FactualMap['category_labels'])
	except:
		print '\tFactual Labels: No Data'

	try:
		print '\tFactual Website: ' + FactualMap['website']
	except:
		print '\tFactual Website: No Data'

	try:
		print '\tFactual Email: ' + FactualMap['email']
	except:
		print '\tFactual Email: No Data'

	try:
		print '\tFactual Cuisines: ' + str(FactualMap['cuisine'])
	except:
		print '\tFactual Cuisines: No Data'

	try:
		print '\tFactual Price: ' + FactualMap['price']
	except:
		print '\tFactual Price: No Data'

	try:
		print '\tFactual Rating: ' + FactualMap['rating']
	except:
		print '\tFactual Rating: No Data'

	try:
		print '\tFactual Cash Only: ' + FactualMap['payment_cashonly']
	except:
		print '\tFactual Cash Only: No Data'

	try:
		print '\tFactual Reservations: ' + FactualMap['reservations']
	except:
		print '\tFactual Reservations: No Data'

	try:
		print '\tFactual Hours: ' + FactualMap['hours_display']
	except:
		print '\tFactual Hours: No Data'

	try:
		print '\tFactual 24 Hours: ' + FactualMap['open_24hrs']
	except:
		print '\tFactual 24 Hours: No Data'

	try:
		print '\tFactual Attire: ' + FactualMap['attire']
	except:
		print '\tFactual Attire: No Data'

	try:
		print '\tFactual Parking: ' + FactualMap['parking']
	except:
		print '\tFactual Parking: No Data'

	try:
		print '\tFactual Smoking: ' + FactualMap['smoking']
	except:
		print '\tFactual Smoking: No Data'

	try:
		print '\tFactual Breakfast: ' + FactualMap['meal_breakfast']
	except:
		print '\tFactual Breakfast: No Data'

	try:
		print '\tFactual Lunch: ' + FactualMap['meal_lunch']
	except:
		print '\tFactual Lunch: No Data'

	try:
		print '\tFactual Dinner: ' + FactualMap['meal_dinner']
	except:
		print '\tFactual Dinner: No Data'

	try:
		print '\tFactual Deliver: ' + FactualMap['meal_deliver']
	except:
		print '\tFactual Deliver: No Data'

	try:
		print '\tFactual Takeout: ' + FactualMap['meal_takeout']
	except:
		print '\tFactual Takeout: No Data'

	try:
		print '\tFactual Cater: ' + FactualMap['meal_cater']
	except:
		print '\tFactual Cater: No Data'

	try:
		print '\tFactual Alcohol: ' + FactualMap['alcohol']
	except:
		print '\tFactual Alcohol: No Data'

	try:
		print '\tFactual GoodForKids: ' + FactualMap['kids_goodfor']
	except:
		print '\tFactual GoodForKids: No Data'

	try:
		print '\tFactual WiFi: ' + FactualMap['wifi']
	except:
		print '\tFactual WiFi: No Data'

	try:
		print '\tFactual Vegetarian: ' + FactualMap['options_vegetarian']
	except:
		print '\tFactual Vegetarian: No Data'

	try:
		print '\tFactual Vegan: ' + FactualMap['options_vegan']
	except:
		print '\tFactual Vegan: No Data'

	try:
		print '\tFactual Gluten Free: ' + FactualMap['options_glutenfree']
	except:
		print '\tFactual Gluten Free: No Data'

	try:
		print '\tFactual Low Fat: ' + FactualMap['options_lowfat']
	except:
		print '\tFactual Low Fat: No Data'

	try:
		print '\tFactual Organic: ' + FactualMap['options_organic']
	except:
		print '\tFactual Organic: No Data'

	try:
		print '\tFactual Healthy: ' + FactualMap['options_healthy']
	except:
		print '\tFactual Healthy: No Data'

	try:
		print '\tFactual ID: ' + FactualMap['factual_id']
	except:
		print '\tFactual ID: No Data'

	try:
		print '\tFactual URL: ' + q1.get_url()
	except:
		print '\tFactual URL: No Data'

if __name__ == '__main__':
	getFactualData("(434) 872-0212")