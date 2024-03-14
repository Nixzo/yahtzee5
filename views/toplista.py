"""toplista.py"""

from flask import render_template
from src.leaderboard import Leaderboard
from src.sort import recursive_insertion
from src.unorderedlist import UnorderedList


def topplista_route(app):
    """Topplistan."""
    @app.route('/toplist')
    def toplist():
        """Topplistan."""
        try:
            leaderboard = Leaderboard.load("./src/leaderboard.txt")
            # Kollar om listan är tom!
            if leaderboard.entries.is_empty():
                return render_template('toplist.html', message="Ingen har spelat än!")
            entries = UnorderedList()

            # Fixar till listan eftersom den bara är en simpel .txt fil...
            for entry in leaderboard.entries:
                name, score = entry  # tilldela namn och poäng direkt från entry
                score = int(score)  # omvandla poängen till en integer
                entries.append((name, score))  # lägg till en tupel till listan

            # sorterar listan
            sorted_enteries = recursive_insertion(entries)

            # konvertera till lista (för att kunna klippa av top 10)
            sorted_enteries_list = list(sorted_enteries)
            # ? revers här för att recursive_insertion sorterar den på andra hållet.
            sorted_enteries_list.reverse()

            top_scores = sorted_enteries_list[:10]  # klipp listan till topp 10

            return render_template('toplist.html', top_scores=top_scores)

        # om filen inte skulle finnas av någon anlending.
        except FileNotFoundError:
            return render_template('toplist.html', message="Fil fattas!")
