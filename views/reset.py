"""reset.py"""

from flask import session, redirect, url_for


def reset_route(app):
    """återställa spelet."""
    @app.route('/reset')
    def reset():
        """återställa spelet."""
        session.clear()
        return redirect(url_for('main'))
