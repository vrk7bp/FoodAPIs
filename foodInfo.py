#!/usr/bin/python

from factual import Factual
import imp
import json
from yelpapi import YelpAPI


FACTUAL_KEY = "4RVd3PBB9wVnoiRTUbGe5bdAXVTCVfClPKKvarLu"
FACTUAL_SECRET = "IK4klSaSGQnWlkYJQIDYLjU5QEhmGIPxZqFdc83L"

yelp_api = YelpAPI("mcoArGtHYkvFHdFWUPaXXA", "DVjJ16rX-i2fk7dxFCaHQSeKX9Y", "8UOAcJeTBsXGxsqVFAXuixp3T9nMaGcl", "wqoFRuG_ywRrPs36IH96hnetGZM")

def getYelpResults(locationLatLong):
	response = yelp_api.search_query(term="buffet", ll=locationLatLong, sort=2, limit=3, category_filter="restaurants") # term='food', location='charlottesville, va',
	
	# print('region center (lat,long): %f,%f\n' % (response['region']['center']['latitude'], response['region']['center']['longitude']))
	
	phoneNumberList = []
	for business in response['businesses']:

		print('%s\n\tYelp ID: %s\n\trating: %g (%d reviews)\n\taddress: %s' % (business['name'], business['id'], business['rating'], business['review_count'], ', '.join(business['location']['display_address'])))
		print "\tAddress: " + str(business['location']['address'])
		print "\tPostal Code: " + str(business['location']['postal_code'])
		print '\tBusiness Categories:' + str(business['categories'])
		print '\tMobile URL:' + str(business['mobile_url'])
		try:
			print '\tPhone Number:' + str(business['display_phone'])
			phoneNumberList.append(business['display_phone'])
		except:
			print'\tPhone Number: No Number'
			phoneNumberList.append("No Number")
		try:
			print '\tPhone Number(2):' + str(business['phone'])
		except:
			print'\tPhone Number(2): No Number'
		try:
			print "\tLatitude, Longitude: " + business['location']['coordinate']['latitude'] + ", " + business['location']['coordinate']['longitude']
		except:
			print "\tLatitude, Longitude: No Data"
	print('\n-------------------------------------------------------------------------\n')

	return phoneNumberList

def formatPhoneNumberForFactual(phoneNumber):
	listOfNums = phoneNumber.split("-")
	stringForFactual = "(" + listOfNums[1] + ")" + " " + listOfNums[2] + "-" + listOfNums[3]
	return stringForFactual


# Phone Number has to be in (XXX) XXX-XXXX format
def getFactualData(phoneNumber):
	factual = Factual(FACTUAL_KEY, FACTUAL_SECRET)
	table = factual.table('restaurants-us')

	filterMap = {}
	filterMap['tel'] = phoneNumber

	q1 = table.filters(filterMap)
	FactualMap = q1.data()[0]
	print "-----------------------------"
	#print json.dumps(q1.data()[0], indent=4, sort_keys=True)
	#print "-----------------------------"
	print 'Factual Data for ' + FactualMap['name'] + ':'

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

if __name__ == '__main__':
	listOfResults = getYelpResults("38.030821,-78.486058")
	getFactualData(formatPhoneNumberForFactual(listOfResults[0]))