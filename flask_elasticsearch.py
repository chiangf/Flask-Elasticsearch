from elasticsearch import Elasticsearch


# Find the stack on which we want to store the database connection.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class FlaskElasticsearch(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('ELASTICSEARCH_HOST', 'localhost:9200')
        app.config.setdefault('ELASTICSEARCH_HTTP_AUTH', None)

        # Use the newstyle teardown_appcontext if it's available,
        # otherwise fall back to the request context
        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    def __getattr__(self, item):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'elasticsearch'):
                ctx.elasticsearch = Elasticsearch(hosts=[ctx.app.config.get('ELASTICSEARCH_HOST')],
                                                  http_auth=ctx.app.config.get('ELASTICSEARCH_HTTP_AUTH'))

            return getattr(ctx.elasticsearch, item)

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'elasticsearch'):
            ctx.elasticsearch = None
