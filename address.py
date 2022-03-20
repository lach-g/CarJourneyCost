class Address:
    def __init__(self, street_num, street_name, suburb, postcode):
        self.street_num = street_num
        self.street_name = street_name
        self.suburb = suburb
        self.postcode = postcode

    def __repr__(self):
        return self.street_num + " " + self.street_name + ", " + self.suburb + ", " + self.postcode
