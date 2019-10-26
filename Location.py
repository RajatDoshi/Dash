class Location:
	def __init__(self, inLatitude = 0.0, inLongitude = 0.0):
		self.latitude = inLatitude
		self.longitude = inLongitude

	def jsonLocationToObject(self, location):
		latitude = location["latitude"]
		longitude = location["longitude"]
		
		return Location(latitude, longitude)

	def serialize(self):
		return {"latitude": self.latitude, "longitude": self.longitude}