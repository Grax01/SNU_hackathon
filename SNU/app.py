from operator import ge
from flask import Flask, render_template, request, session,redirect,url_for
from googleplaces import GooglePlaces, types, lang
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from urllib.request import urlopen
import json
google_places = GooglePlaces(API_KEY)

app = Flask(__name__)
API_KEY="API"
mongopass="mongo"



class geeks:
    def __init__(self,id, name, rating,img):
        self.id=id
        self.name = name
        self.rating = rating
        self.img=img



@app.route("/", methods=['GET', 'POST'])
def admin():
     if request.method == 'GET':
         return render_template("admin.html")



@app.route("/", methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        query_result = google_places.nearby_search(

    lat_lng ={'lat': 28.6280, 'lng': 77.3649},
	radius = 15000,

	types =[types.TYPE_MOVIE_THEATER])
    print(query_result)
    print(dir(query_result))
    obj=[]
    for place in query_result.places:
        try:
            img=place.photos[0].photo_reference
            img = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference='+ place.photos[0].photo_reference + '&key=AIzaSyCi3Kvx3X6P6s0gPEwEuSRb1cHMBEUGYXY'
            print(place.place_id,place.name, place.rating , place.photos[0].photo_reference)
            obj.append(geeks(place.place_id,place.name,place.rating,img))
        except IndexError:
            pass
       
        # obj.append(geeks(place.name,place.rating,place.photos[0].photo_reference))
        # # obj[count]['name']=place.name
        # obj[count]['rate']=place.rating
        # obj[count]['img']=place.photos[0].photo_reference
        # count=count+1
	    # print("boxie",dir(place)) 
	    # print(place.name)
	    # print("Latitude", place.geo_location['lat'])
	    # print(place.photos[0].photo_reference)
        # print(place.photos[0].photo_reference)
	    # for i in place.photos:
        #      print(i.photo_reference)
    print(obj)
    return render_template("nearby_theatre.html",obj=obj)
      
         
           
           



@app.route("/search")
def seating():
    
    return render_template("seating.html")



@app.route("/cinemaHallRegister", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("hallRegister.html")



@app.route('/seatBooked', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        bookedSeats=request.form.getlist('seat')
        print(bookedSeats)


if __name__ == "__main__":
    app.secret_key = 'super secret key'
app.run( port=9052)