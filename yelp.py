from yelpapi import YelpAPI

yelp_api = YelpAPI("mcoArGtHYkvFHdFWUPaXXA", "DVjJ16rX-i2fk7dxFCaHQSeKX9Y", "8UOAcJeTBsXGxsqVFAXuixp3T9nMaGcl", "wqoFRuG_ywRrPs36IH96hnetGZM")

"""
    Example search by location text and term. Take a look at http://www.yelp.com/developers/documentation/v2/search_api for
    the various options available.
"""
print('***** 5 best rated ice cream places in Austin, TX *****\n%s\n' % "yelp_api.search_query(term='ice cream', location='austin, tx', sort=2, limit=5)")
response = yelp_api.search_query(term='ice cream', location='austin, tx', sort=2, limit=5)
print('region center (lat,long): %f,%f\n' % (response['region']['center']['latitude'], response['region']['center']['longitude']))
for business in response['businesses']:
    print('%s\n\tYelp ID: %s\n\trating: %g (%d reviews)\n\taddress: %s' % (business['name'], business['id'], business['rating'],
                                                                           business['review_count'], ', '.join(business['location']['display_address'])))

print('\n-------------------------------------------------------------------------\n')