"""error_handlers.py"""

import traceback
from flask import render_template


def hander_404(app):
    """404-fel."""
    @app.errorhandler(404)
    def page_not_found(e):
        """404"""
        print(e)
        return render_template('404.html'), 404


def handler_500(app):
    """500-fel."""
    @app.errorhandler(500)
    def internal_server_error():
        """500-fel."""
        return '<p>Flask 500<pre>' + traceback.format_exc()
