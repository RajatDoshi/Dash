class Company:
	def __init(self, inIdentity = -1, inName = "", inInventories = [], inProducts = []):
		self.identity = inIdentity
		self.name = inName
		self.inventories = inInventories
		self.products = inProducts

	def jsonCompanyToObject(self, company):
		identity = company["identity"]
		name = company["name"]
		inventories = company["inventories"]
		products = company["products"]

		return Company(identity, name, inventories, products)

	def serialize(self):
		return {"identity": self.identity, "name": self.name, "inventories": self.inventories, "products": self.products}