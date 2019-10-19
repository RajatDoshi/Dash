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
python main.py
```
