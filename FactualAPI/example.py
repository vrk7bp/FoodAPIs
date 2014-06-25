#!/usr/bin/python

from factual import Factual

KEY = "YOUR_KEY"
SECRET = "YOUR_SECRET"

def main():
    factual = Factual(KEY, SECRET)
    
    table = factual.table('places')
    
    q1 = table.search("sushi Santa Monica")
    print q1.data()[1]
    print q1.get_url()
    
    q2 = table.filters({'category_ids':{'$includes':338}, 'region': "CA"}).limit(1)
    print q2.data()
  
if __name__ == '__main__':
  main()
