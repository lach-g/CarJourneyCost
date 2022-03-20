class Address:
    def __init__(self, street_num, street_name, suburb, postcode):
        self.street_num = street_num
        self.street_name = street_name
        self.suburb = suburb
        self.postcode = postcode

    def __repr__(self):
        return self.street_num + " " + self.street_name + ", " + self.suburb + ", " + self.postcode

def main():
    origin = address_input("Origin")
    destination = address_input("Destination")
    print("Origin: " + str(origin))
    print("Destination: " + str(destination))
    

def address_input(point_of_journey: str) -> Address:
    print(f"{point_of_journey} Address\n---")
    street_num = input("Street Number: ")
    street_name = input("Street Name: ")
    suburb = input("Suburb: ")
    post_code = input("Post Code: ")
    print("\n")
    return Address(street_num, street_name, suburb, post_code)




if __name__ == "__main__":
    main()
