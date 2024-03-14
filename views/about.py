"""about.py"""

from flask import render_template


def about_route(app):
    """About."""
    @app.route('/about')
    def about():
        """About."""
        return render_template('about.html')
