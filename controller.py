import requests

import config
from address import Address
from journey import Journey
from fuel_usage import Fuel_Usage

def address_input(point_of_journey: str) -> Address:
    print(f"{point_of_journey} Address\n---")
    street_num = input("Street Number:\n")
    street_name = input("Street Name:\n")
    suburb = input("Suburb:\n")
    post_code = input("Post Code:\n")
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

def create_fuel_usage(distance) -> Fuel_Usage:
    fuelType = input("Fuel Type (91, 95, 98, Diesel):\n")
    litresPerHundredKmsStr = input("Litres per 100 km of car (Press Enter if unknown):\n")
    if litresPerHundredKmsStr != "":
        litresPerHundredKms = float(litresPerHundredKmsStr)
        totalFuelUsage = round(distance * (litresPerHundredKms / 100), 2)
        print("Total Fuel Usage (l): " + str(totalFuelUsage))
    else:
        litresPerHundredKms = 13.4
        totalFuelUsage = round(distance * (litresPerHundredKms / 100), 2)
        print("Fuel Usage\n---\nUsing current average fuel usage (13.4 l/100kms)\nTotal Fuel Usage (l): " + str(totalFuelUsage))
    return Fuel_Usage(fuelType, litresPerHundredKms, totalFuelUsage)
