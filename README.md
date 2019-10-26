DashProject

Flask setup:
https://opensource.com/article/18/4/flask

Put this in the .bash_rc file in order to locate the module

```
# in your activate script, probably at the bottom (but anywhere will do)

export FLASK_APP=$VIRTUAL_ENV/../todo/app.py
export DEBUG='True'
```

Run server locally:

```
FLASK_APP=main.py flask run
```

Starter:
https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/

Forms:
https://www.blog.pythonlibrary.org/2017/12/13/flask-101-how-to-add-a-search-form/
http://www.blog.pythonlibrary.org/2017/12/14/flask-101-adding-editing-and-displaying-data/

EasyPost for estimating shipping rates:
https://www.easypost.com/docs/api
