import json

from address import Address
from journey import Journey
import controller

def main():
    origin = controller.address_input("Origin")
    destination = controller.address_input("Destination")

    # DEBUG
    # origin = Address("37A", "Farris Street", "Innaloo", "6018")
    #destination = Address("8", "Webb Street", "Cottesloe", "6011")
    #origin = Address("", "", "", "")
    #destination = Address("", "", "", "")

    # Quering Google Maps API
    response = controller.query_maps(origin, destination)

    # Parsing response for distance and time traveling
    data = response.json()
    success = controller.maps_query_success(data)

    if not success:
        return 0

    # Create Journey Model
    journey = controller.create_journey(data)
    print(journey)

if __name__ == "__main__":
    main()
