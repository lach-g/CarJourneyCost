import json

from address import Address
from journey import Journey
import controller

def main():
    origin = controller.address_input("Origin")
    destination = controller.address_input("Destination")

    # DEBUG
    #origin = Address("37A", "Farris Street", "Innaloo", "6018")
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

    # Create Fuel Usage Model
    fuel_usage = controller.create_fuel_usage(journey.kms)
    print("Type: " + fuel_usage.fuel_type)
    print("Mileage: " + str(fuel_usage.mileage))
    print("Total Fuel Usage: " + str(fuel_usage.total_fuel_usage))

    # Without API access necessary to input fuel cost
    print("\n\nVisit https://informedsources.com/ for live petrol prices.")
    current_fuel_cost = float(input("Current fuel cost:\n"))
    journey_cost = round(current_fuel_cost * fuel_usage.total_fuel_usage, 2)
    print("\nCost Estimation\n---\nOne way journey cost: $" + str(journey_cost))
    print("Return journey cost: $" + str(journey_cost * 2))




if __name__ == "__main__":
    main()
