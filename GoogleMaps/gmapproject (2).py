import googlemaps # print(os.path.dirname(sys.executable)) / pip install googlemaps
import requests, json


# Open the file and get the Google Key
f=open("mykey.txt",'r')
api_key = f.readline()


# url variable store url
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# Requires API key
gmaps = googlemaps.Client(key=api_key)

source = input("enter the source area name : ")
destination = input("enter the destination area name : ")

# Requires cities name
my_dist = gmaps.distance_matrix(source,destination)['rows'][0]['elements'][0]

# Printing the result
print(my_dist)

def destinations(query, api_key):
    # get method of requests module return response object
    r = requests.get(url + 'query=' + query + '&key=' + api_key)                                                                  
    # json method of response object convert json format data into python format data
    x = r.json()
    # print (x)
    # now x contains list of nested dictionaries
    # we know dictionary contain key value pair
    # store the value of result key in variable y
    y = x['results']
    print("------------" + query + "----------")          
    for i in range(len(y)):     
    # Print value corresponding to the 'name' key at the ith index of y
        print(y[i]['name'])
    
# The text string on which to search query = input('Hotels in Velachery: ')
placehotel="Hotels in"
query = placehotel + source
destinations(query, api_key)

# The text string on which to search query = input('Hospital in AnnaNagar: ')
placehospital="Hospitals in "
query = placehospital + source
destinations(query, api_key)

# The text string on which to search query = input('Hospital in AnnaNagar: ')
query = placehospital + destination
destinations(query, api_key)

# The text string on which to search query = input('Hotels in Velachery: ')
query = placehotel + destination
destinations(query, api_key)
