"""
Flask-webbapplikationen.
"""

from flask import Flask
from views import (main_route, about_route, topplista_route, reset_route,
                   save_score_route, hander_404, handler_500)


app = Flask(__name__)
app.secret_key = 'tempkey'

main_route(app)
about_route(app)
topplista_route(app)
reset_route(app)
save_score_route(app)
hander_404(app)
handler_500(app)


if __name__ == '__main__':
    app.run(debug=True)
