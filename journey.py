class Journey:
    def __init__(self, origin, destination, meters, seconds):
        self.origin = origin
        self.destination = destination
        self.meters = meters
        self.seconds = seconds
        self.kms = self.meters_to_kms(meters)
        self.minutes = self.seconds_to_minutes(seconds)

    def meters_to_kms(self, meters):
        kms = round(float(meters) / 1000.0, 2)
        return kms

    def seconds_to_minutes(self, seconds):
        minutes = round(float(seconds) / 60, 2)
        return minutes

    def __repr__(self):
        return ("\nJourney\n---\nOrigin: " + self.origin +
                "\nDestination: " + self.destination +
                "\nDistance: " + str(self.kms) +
                "\nDuration: " + str(self.minutes) + "\n")
