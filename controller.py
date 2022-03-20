import requests

import config
from address import Address
from journey import Journey

def address_input(point_of_journey: str) -> Address:
    print(f"{point_of_journey} Address\n---")
    street_num = input("Street Number: ")
    street_name = input("Street Name: ")
    suburb = input("Suburb: ")
    post_code = input("Post Code: ")
    print("\n")
    return Address(street_num, street_name, suburb, post_code)

def query_maps(origin: Address, destination: Address):
    url = ("https://maps.googleapis.com/maps/api/distancematrix/json?origins="
            + origin.street_num + "%20"
            + origin.street_name + "%20"
            + origin.suburb + "%20"
            + origin.postcode + "%20"
            + "&destinations="
            + destination.street_num + "%20"
            + destination.street_name + "%20"
            + destination.suburb + "%20"
            + destination.postcode + "%20"
            + "&units=metric&key="
            + config.google_maps_api_key)
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response

def maps_query_success(data) -> bool:
    success = False
    response_status = data["status"]
    journey_status = data["rows"][0]["elements"][0]["status"]
    if response_status == "OK" and journey_status == "OK":
        success = True
    if not success:
        print("ERROR: Google Maps query failed")
        print("Response status: " + response_status)
        print("Journey status: " + journey_status)
    return success

def create_journey(data) -> Journey:
    origin = data["origin_addresses"][0]
    destination = data["destination_addresses"][0]
    meters = data["rows"][0]["elements"][0]["distance"]["value"]
    seconds = data["rows"][0]["elements"][0]["duration"]["value"]
    journey = Journey(origin, destination, meters, seconds)
    return journey
