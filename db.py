# import datetime
# import json
#
# from .main import db_db_conn
# from ..classes.Location import Location
# from ..classes.Company import Company
# from ..classes.Inventory import Inventory
# from ..classes.Product import Product
#
# def get_company(company_id):
# 	c = db_conn.cursor()
# 	sql = "SELECT * FROM companies WHERE IDENTITY = ?;"
# 	args = (company_id,)
# 	c.execute(sql, args)
# 	output = c.fetchone()
# 	db_conn.close()
#
# 	if output is None:
# 		return 0
#
# 	companySerialized = json.loads(output[0])
# 	company = Company()
# 	company = company.jsonCompanyToObject(companySerialized)
# 	return company
#
# def get_inventory(inventory_id):
# 	c = db_conn.cursor()
# 	sql = "SELECT JSON FROM inventories WHERE IDENTITY = ?;"
# 	args = (inventory_id,)
# 	c.execute(sql, args)
# 	output = c.fetchone()
# 	db_conn.close()
#
# 	if output is None:
# 		return 0
#
# 	inventorySerialized = json.loads(output[0])
# 	inventory = Inventory()
# 	inventory = inventory.jsonCompanyToObject(inventorySerialized)
# 	return inventory
#
# def get_product(self, product_id):
# 	c = db_conn.cursor()
# 	sql = "SELECT JSON FROM products WHERE IDENTITY = ?;"
# 	args = (product_id,)
# 	c.execute(sql, args)
# 	output = c.fetchone()
# 	db_conn.close()
#
# 	if output is None:
# 		return 0
#
# 	productSerialized = json.loads(output[0])
# 	product = Product()
# 	product = product.jsonCompanyToObject(productSerialized)
# 	return product
#
# def insert_update(obj_type, company_id, obj_id, oldJSON, newJSON):
# 	c = db_conn.cursor()
# 	sql = "SELECT COUNT(*) FROM updates"
# 	c.execute(sql)
# 	if c.fetchone()[0] != 0:
# 		sql = f"SELECT * FROM updates WHERE UPDATE_IDENTITY = " \
# 				f"(SELECT MAX(UPDATE_IDENTITY)  FROM updates);"
# 		c.execute(sql)
# 		output = c.fetchone()
# 		updateIdentity = int(output[3]) + 1
# 	else:
# 		updateIdentity = 1
#
# 	sql = "INSERT INTO updates VALUES(?, ?, ?, ?, ?, ?, ?);"
# 	args = (updateIdentity, obj_type, company_id, obj_id,
# 		oldJSON, newJSON, str(datetime.datetime.now()))
# 	c.execute(sql, args)
# 	db_conn.commit()
#
# 	return updateIdentity
#
# def update_company(self, user_id, target_id, newCompanyJSON):
# 	oldCompanyJSON = self.getCompany(target_id).serialize()
#
# 	c = db_conn.cursor()
# 	sql = "UPDATE companies SET JSON = ? WHERE IDENTITY = ?"
# 	args = (newCompanyJSON, target_id)
# 	c.execute(sql, args)
# 	db_conn.commit()
#
# 	return self.insertUpdate(1, user_id, target_id, oldCompanyJSON, newCompanyJSON)
#
# def update_inventory(self, user_id, target_id, newInventoryJSON):
# 	oldInventoryJSON = self.getInventory(target_id).serialize()
#
# 	c = db_conn.cursor()
# 	sql = "UPDATE inventories SET JSON = ? WHERE IDENTITY = ?"
# 	args = (newInventoryJSON, target_id)
# 	c.execute(sql, args)
# 	db_conn.commit()
#
# 	return self.insertUpdate(2, user_id, target_id, oldInventoryJSON, newInventoryJSON)
#
# def update_product(self, user_id, target_id, newProductJSON):
# 	oldProductJSON = self.getProduct(target_id).serialize()
#
# 	db_conn = sqlite3.db_connect(DB_FILE)
# 	c = db_conn.cursor()
# 	sql = "UPDATE products SET JSON = ? WHERE IDENTITY = ?"
# 	args = (newProductJSON, target_id)
# 	c.execute(sql, args)
# 	db_conn.commit()
#
# 	return self.insertUpdate(3, user_id, target_id, oldProductJSON, newProductJSON)
# 
# def get_inventories(self, modelNumber):
# 	c = db_conn.cursor()
# 	sql = "SELECT DICT FROM productsIDS WHERE MODEL_NUMBER = ?;"
# 	args = (modelNumber,)
# 	c.execute(sql, args)
# 	db_conn.commit()
#
# 	return json.loads(output[0])
