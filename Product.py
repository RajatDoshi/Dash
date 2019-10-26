class Product:
	def __init__(self, inIdentity = -1, inWeight = 0, inPrice = 0, inInventoryIdentity = -1, inQuantity = 0, inModelNumber = "", inSerialNumber = [], inInTransit = False, inTransitData = []):
		self.identity = inIdentity
		self.weight = inWeight
		self.price = inPrice
		self.inventoryIdentity = inInventoryIdentity
		self.quantity = inQuantity
		self.modelNumber = inModelNumber
		self.serialNumber = inSerialNumber
		self.inTransit = inInTransit
		self.transitData = inTransitData

	def jsonProductToObject(self, product):
		identity = product["identity"]
		weight = product["weight"]
		price = product["price"]
		inventoryIdentity = product["inventoryIdentity"]
		quantity = product["quantity"]
		modelNumber = product["modelNumber"]
		serialNumber = product["serialNumber"]
		inTransit = product["inTransit"]
		transitData = product["transitData"]

		return Product(identity, weight, price, inventoryIdentity, quantity, modelNumber, serialNumber, inTransit, transitData)

	def serialize(self):
		return {"identity": self.identity, "weight": self.weight, "price": self.price, "inventoryIdentity": self.inventoryIdentity, "quantity": self.quantity, "modelNumber": self.modelNumber, "serialNumber": self.serialNumber}