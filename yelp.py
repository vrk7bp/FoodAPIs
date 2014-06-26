from yelpapi import YelpAPI

yelp_api = YelpAPI("mcoArGtHYkvFHdFWUPaXXA", "DVjJ16rX-i2fk7dxFCaHQSeKX9Y", "8UOAcJeTBsXGxsqVFAXuixp3T9nMaGcl", "wqoFRuG_ywRrPs36IH96hnetGZM")

"""
    Example search by location text and term. Take a look at http://www.yelp.com/developers/documentation/v2/search_api for
    the various options available.
"""
#print('***** 5 best rated ice cream places in Austin, TX *****\n%s\n' % "yelp_api.search_query(term='ice cream', location='austin, tx', sort=2, limit=5)")


response = yelp_api.search_query(term="buffet", ll="38.030821,-78.486058", sort=0, limit=20, category_filter="restaurants") # term='food', location='charlottesville, va',
print('region center (lat,long): %f,%f\n' % (response['region']['center']['latitude'], response['region']['center']['longitude']))
for business in response['businesses']:
    print('%s\n\tYelp ID: %s\n\trating: %g (%d reviews)\n\taddress: %s' % (business['name'], business['id'], business['rating'],
                                                                           business['review_count'], ', '.join(business['location']['display_address'])))
    print "\tAddress: " + str(business['location']['address'])
    print "\tPostal Code: " + str(business['location']['postal_code'])
    print '\tBusiness Categories:' + str(business['categories'])
    print '\tMobile URL:' + str(business['mobile_url'])
    try:
    	print '\tPhone Number:' + str(business['display_phone'])
    except:
    	print'\tPhone Number: No Number'
    try:
    	print '\tPhone Number(2):' + str(business['phone'])
    except:
    	print'\tPhone Number(2): No Number'
    try:
    	print "\tLatitude, Longitude: " + business['location']['coordinate']['latitude'] + ", " + business['location']['coordinate']['longitude']
    except:
    	print "\tLatitude, Longitude: No Data"
print('\n-------------------------------------------------------------------------\n')

#print

#print response['businesses'][0]