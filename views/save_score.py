"""save_score.py"""

from flask import session, redirect, request, url_for
from src.leaderboard import Leaderboard


def save_score_route(app):
    """Topplista"""
    @app.route('/save_score', methods=['POST'])
    def save_score():
        """
        Topllista
        """
        player_name = request.form.get('player_name')
        score = session['total_points']
        leaderboard = Leaderboard.load('src/leaderboard.txt')
        leaderboard.add_entry(player_name, score)
        leaderboard.save('src/leaderboard.txt')

        # rensar session automatiskt när du har seplat färfig
        session.clear()
        return redirect(url_for('toplist'))
