from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'Flask-WTF',
    'easypost',
    'sqlite3'
]

setup(
    name='dash',
    version='0.0',
    description='Dash web application using Python Flask',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
