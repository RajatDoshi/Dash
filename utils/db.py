import sqlite3
import datetime
import json
from os.path import join, dirname, abspath
DB_FILE = join(dirname(dirname(abspath(__file__))), 'data.db')

from Location import Location
from Company import Company
from Inventory import Inventory
from Product import Product

class sqlMethods:
	def getCompany(self, company_id):
		conn = sqlite3.connect(DB_FILE)
		c = conn.cursor()
		sql = "SELECT * FROM companies WHERE IDENTITY = ?;"
		args = (company_id,)
		c.execute(sql, args)
		output = c.fetchone()
		conn.close()

		if output is None:
			return 0

		else:
			companySerialized = json.loads(output[0])
			company = Company()
			company = company.jsonCompanyToObject(companySerialized)
			return company

	def getInventory(self, inventory_id):
		conn = sqlite3.connect(DB_FILE)
		c = conn.cursor()
		sql = "SELECT JSON FROM inventories WHERE IDENTITY = ?;"
		args = (inventory_id,)
		c.execute(sql, args)
		output = c.fetchone()
		conn.close()

		if output is None:
			return 0

		else:
			inventorySerialized = json.loads(output[0])
			inventory = Inventory()
			inventory = inventory.jsonCompanyToObject(inventorySerialized)
			return inventory

	def getProduct(self, product_id):
		conn = sqlite3.connect(DB_FILE)
		c = conn.cursor()
		sql = "SELECT JSON FROM products WHERE IDENTITY = ?;"
		args = (product_id,)
		c.execute(sql, args)
		output = c.fetchone()
		conn.close()

		if output is None:
			return 0

		else:
			productSerialized = json.loads(output[0])
			product = Product()
			product = product.jsonCompanyToObject(productSerialized)
			return product

	def insertUpdate(obj_type, company_id, obj_id, oldJSON, newJSON):
		conn = sqlite3.connect(DB_FILE)
		c = conn.cursor()

		sql = "SELECT COUNT(*) FROM updates"
		c.execute(sql)
		if c.fetchone()[0] != 0:
			sql = "SELECT * FROM updates WHERE UPDATE_IDENTITY = (SELECT MAX(UPDATE_IDENTITY)  FROM updates);"
			c.execute(sql)
			output = c.fetchone()
			updateIdentity = int(output[3]) + 1
		else:
			updateIdentity = 1

		sql = "INSERT INTO updates VALUES(?, ?, ?, ?, ?, ?, ?);"
		args = (updateIdentity, obj_type, company_id, obj_id, oldJSON, newJSON, str(datetime.datetime.now()))
		c.execute(sql, args)
		conn.commit()
		conn.close()

		return updateIdentity


	def updateCompany(self, user_id, target_id, newCompanyJSON):
		oldCompanyJSON = self.getCompany(target_id).serialize()

		conn = sqlite3.connect(DB_FILE)
		c = conn.cursor()
		sql = "UPDATE companies SET JSON = ? WHERE IDENTITY = ?"
		args = (newCompanyJSON, target_id)
		c.execute(sql, args)
		conn.commit()
		conn.close()

		return self.insertUpdate(1, user_id, target_id, oldCompanyJSON, newCompanyJSON)

	def updateInventory(self, user_id, target_id, newInventoryJSON):
		oldInventoryJSON = self.getInventory(target_id).serialize()

		conn = sqlite3.connect(DB_FILE)
		c = conn.cursor()
		sql = "UPDATE inventories SET JSON = ? WHERE IDENTITY = ?"
		args = (newInventoryJSON, target_id)
		c.execute(sql, args)
		conn.commit()
		conn.close()

		return self.insertUpdate(2, user_id, target_id, oldInventoryJSON, newInventoryJSON)

	def updateProduct(self, user_id, target_id, newProductJSON):
		oldProductJSON = self.getProduct(target_id).serialize()

		conn = sqlite3.connect(DB_FILE)
		c = conn.cursor()
		sql = "UPDATE products SET JSON = ? WHERE IDENTITY = ?"
		args = (newProductJSON, target_id)
		c.execute(sql, args)
		conn.commit()
		conn.close()

		return self.insertUpdate(3, user_id, target_id, oldProductJSON, newProductJSON)

	def getInventories(self, modelNumber):
		conn = sqlite3.connect(DB_FILE)
		c = conn.cursor()
		sql = "SELECT DICT FROM productsIDS WHERE MODEL_NUMBER = ?;"
		args = (modelNumber,)
		c.execute(sql, args)
		conn.commit()
		conn.close()

		return json.loads(output[0])