from Location import Location

class Inventory:
	def __init__(self, inIdentity = -1,
			inLocation = Location(),
			inProducts = [],
			inWarehouse = False,
			inCompanyID = -1):
		self.identity = inIdentity
		self.location = inLocation
		self.products = inProducts
		self.warehouse = inWarehouse
		self.companyID = inCompanyID

	def jsonInventoryToObject(self, inventory):
		identity = inventory["identity"]
		location = inventory["location"]
		products = inventory["products"]
		warehouse = inventory["warehouse"]
		companyID = inventory["companyID"]

		return Inventory(identity, location, products, warehouse, companyID)

	def serialize(self):
		return {"identity": self.identity, "location": self.location,
			"products": self.products, "warehouse", self.warehouse,
			"companyID": self.companyID}
