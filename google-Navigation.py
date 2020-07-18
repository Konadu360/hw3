#trying something new
"""
Write a function that will provide directions between two locations. Leverage the
Google Directions API to source the navigation information from point A to point B.
The function should accept three input parameters:
origin
destination preferred
travel method 

The function should output the entire trip time in text format and information on each individual leg of
the trip including duration time and duration distance. For each step in the leg, please include duration
time, duration distance, and formatted instructions. Ideally the formatted instructions will not include any
html tags but this is not necessary. You may assume that the parameters given will be valid according
to the API documentation. You may also assume there will be a route from the origin to the destination.
For information on the Google Directions API, please refer to the following documentation:
https://developers.google.com/maps/documentation/directions/intro . Please note that you can
reference additional documentation resources for further information regarding the Google Directions
API . Please note that inputting credit card information is normal and Google gives this $200
credit so the interview process will not cost you any additional dollars.
Here is an example:
origin = Boston, MA destination
= Santa Clara, CA preferred
travel method = driving
These input arguments would go to this URL (use your own API
Key):
https://maps.googleapis.com/maps/api/directions/json?origin=Boston+MA&destination=Santa+Clara+C
A &mode=driving&key=YOURAPIKEY
Below are formatted examples of the first and last steps of the
journey.
Step 1: In 0.1 mi, Head north on Cambridge St toward Sudbury St. This should take
you 1 min.
[Steps 2 – 54 are omitted]
Step 55: In 0.1 mi, Turn right onto Lincoln St. This should take
you 1 min.

"""


# enter location, destination and travel method

# define function map() to privide drirection for location and direction provided
def map(origin,destination,mode):
    # import the request function to scape data from the url with the information entered by the user
    # import json to parse the json-encoded content data into python dict using json.loads() function
    import requests,pprint,json,bs4
    url = ("https://maps.googleapis.com/maps/api/directions/json?origin=${}&destination=${}&mode=${}&key=AIzaSyAznD0Chv5MlSEemH0EKmUzKZI9RYhbmdY".format(origin.replace(' ','+'),destination.replace(' ','+'),mode.replace(' ','+')))
    print(url)
    response= requests.get(url)
    Dir_Data = json.loads(response.text)
    pprint.pprint(Dir_Data)
    print('\n\n')
    
    # get all the values for the key(routes) in the direction data and store in route
    # loop through the data stored in the variable(route),filter all items in each individual leg and
    # print total distance and duration for the journey
     # loop through the steps in legs and parse the html instruction in beautiful soup to format it and
    #  use the getText() function to extract only the text in the html instruction
    # initialize a counter and print each count of steps(distance and instructions)
    
    route=Dir_Data.get('routes',0)
    for legs in route:
        for items in legs['legs']:
            print('Total Distance {} and Duration {}'.format(items['distance'].get('text',False),items['duration'].get('text',False)),'\n' )
            count=0
            for dis_dest_dir in items['steps']:
                soup_data=bs4.BeautifulSoup(dis_dest_dir['html_instructions'],'html.parser')
                count +=1
                print('step {}: In {}, {}. This should take you {}\n' .format(str(count),dis_dest_dir['distance'].get('text',0),soup_data.getText(separator=' '),dis_dest_dir['duration'].get('text',0)))

# keep input data in try and except function to exclude keyboard interrupt
# call the function map() to execute the user input
try:
    print('\nYOU CAN PRESS CTRL-C TO QUIT\n')
    location =input("Please enter your location:(example: Chicago,IL) : ")
    destination =input("Please enter your destination: ")
    txmethod = input("Select your preferred travel method from: driving, bicycling, transit, or walking : ")
    map(location,destination,txmethod)
except KeyboardInterrupt:
    print('\n\n OOPS!!! good bye')
