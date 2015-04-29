# Flask-Elasticsearch

This is a Flask extension that provides simple integration with Elasticsearch.

## Usage

In your main app file:
```
from flask import Flask
from flask.ext.elasticsearch import FlaskElasticsearch

app = Flask(__name__)
es = FlaskElasticsearch(app)
```

If you're following the [Application Factories](http://flask.pocoo.org/docs/0.10/patterns/appfactories/) pattern:
```
from flask import Flask
from flask.ext.elasticsearch import FlaskElasticsearch

es = FlaskElasticsearch()

app = Flask(__name__)
es.init_app(app)
```


## Customizing Properties

In order to customize the host, add the following into your app.config (see [Configuration Handling](http://flask.pocoo.org/docs/0.10/config/) for more details):
```
ELASTICSEARCH_HOST = "10.10.10.13:9200"
```

If you need to specify HTTP AUTH for the Elasticsearch connection, add the following into your app.config:
```
ELASTICSEARCH_HTTP_AUTH = "<INSERT AUTH KEY>"
```
