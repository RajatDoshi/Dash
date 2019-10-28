from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db_creator import User, Product, Item

import pandas as pd
import numpy as np

engine = create_engine('sqlite:///data.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # Base.metadata.create_all(bind=engine)

    # users = [('albert', '408 Lakeshore Lane', 'Chapel Hill', 'NC', '27514', 'US', 'Buyer'),
    #             ('john', '1 some street', 'New Haven', 'CT', '00000', 'US', 'Seller'),
    #             ('paul', '2 some street', 'Cupertino', 'CA', '11111', 'US', 'Seller')]
    # products = [('chair', 'furniture', 10, 10, 10, 10),
    #             ('desk', 'furniture', 20, 20, 20, 20)]
    # items = [('chair', 'paul', 10),
    #             ('chair', 'john', 20),
    #             ('desk', 'paul', 30)]

    users = np.array(pd.read_csv('data/users.csv'))[:, 1:]
    products = np.array(pd.read_csv('data/products.csv'))[:, 1:]
    items = np.array(pd.read_csv('data/items.csv'))[:, 1:]

    for instance in users:
        db_session.add(User(name=instance[0].lower(), street=instance[1],
            city=instance[2], state=instance[3], zip=instance[4],
            country=instance[5], user_type=instance[6]))

    for instance in products:
        db_session.add(Product(name=instance[0].lower(), category=instance[1],
            width=instance[2], height=instance[3], length=instance[4],
            weight=instance[5]))

    db_session.commit()

    for instance in items:
        item = Item(product=instance[0].lower(), seller=instance[1].lower(),
            price=instance[2], quantity=True)
        db_session.add(item)

        product = db_session.query(Product).filter(
            Product.name==instance[0].lower()).first()

        seller = db_session.query(User).\
            filter(User.name==instance[1].lower()).\
            filter(User.user_type=='Seller').first()

        if product and seller:
            # Add child to Product parent models
            product.items.append(item)
            seller.items.append(item)

    db_session.commit()
