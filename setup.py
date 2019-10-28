from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'Flask-WTF',
    'easypost',
    'flask_table',
    'numpy',
    'pandas',
    'googlemaps'
]

setup(
    name='yhack19',
    version='0.0',
    description='yhack19 web application using Python Flask',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    instalsl_requires=requires
)
