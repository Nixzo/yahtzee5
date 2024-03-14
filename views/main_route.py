"""
main_route.py
"""

from flask import session, request, render_template
from src.hand import Hand
from src.scoreboard import Scoreboard


def initialize_game() -> None:
    """Initiera spelet i sessionen."""
    initial_hand = Hand()
    session['hand'] = [die.get_value() for die in initial_hand.dice]
    session['rerolls'] = 0
    session['scoreboard_points'] = {}
    session['used_rules'] = []
    session['total_points'] = 0
    session['already_scored'] = {}


def get_current_hand_and_scoreboard():
    """Hämta nuvarande hand och poängtavla """
    current_hand = Hand(session['hand'])
    scoreboard = Scoreboard()
    scoreboard.points = session['scoreboard_points']
    scoreboard.used_rules = set(session['used_rules'])
    return current_hand, scoreboard


def handle_rule_selection(rule_name, rules, scoreboard):
    """
    Hantera reger och avslutning.

    Args:
        rule_name (str): Namnet på den valda regeln.
        rules (list): Listan över tillgängliga regler.
        scoreboard (Scoreboard): Den nuvarande poängtavlan.

    Returns:
        tuple: En tuple som innehåller en boolean som indikerar om spelet är slut,
               och poängen för den valda regeln.
    """
    game_finished = False
    rule_points = next((rule['points']
                       for rule in rules if rule['name'] == rule_name), None)
    if rule_points is not None:
        session['total_points'] += rule_points
        session['already_scored'][rule_name] = rule_points
        session['scoreboard_points'][rule_name] = rule_points
        scoreboard.used_rules.add(rule_name)
        session['used_rules'].append(rule_name)
        session['rerolls'] = -1
        game_finished = scoreboard.finished()
    return game_finished, rule_points


def dice_reroll(dice_to_reroll, current_hand):
    """
    Hantera omkastning av tärningar.

    Args:
        dice_to_reroll (list): Indexen för tärningarna att kasta om.
        current_hand (Hand): Den nuvarande handen av tärningar.
    """
    if session.get('rerolls', 0) < 2:
        current_hand.roll(dice_to_reroll)
        session['hand'] = [die.get_value() for die in current_hand.dice]
        session['rerolls'] = session.get('rerolls', 0) + 1


def main_route(app):
    """main_route..."""
    @app.route('/', methods=['GET', 'POST'])
    def main():
        """main..."""
        error_message = None
        game_finished = False
        if 'hand' not in session:
            initialize_game()
        current_hand, scoreboard = get_current_hand_and_scoreboard()
        game_over_message = None
        if request.method == 'POST':
            rules = [{'name': rule.name, 'points': rule.points(
                current_hand)} for rule in scoreboard.rules]
            rule_name = request.form.get('rule')
            if rule_name:
                game_finished, _ = handle_rule_selection(
                    rule_name, rules, scoreboard)
                if game_finished:
                    game_over_message = f'Spelet är slut! Din totala poäng är: ' \
                        f'{session["total_points"]}'
            dice_to_keep = [int(i) for i in request.form.getlist('dice')]
            dice_to_reroll = [i for i in range(5) if i not in dice_to_keep]
            if dice_to_reroll and session.get('rerolls', 0) >= 2:
                error_message = 'Du har redan kastat om tärningarna två gånger!, välj en regel!'
            else:
                dice_reroll(dice_to_reroll, current_hand)
        rules = [{'name': rule.name, 'points': rule.points(
            current_hand)} for rule in scoreboard.rules]
        return render_template(
            'index.html',
            hand=current_hand,
            top_score=scoreboard.get_highest_score(current_hand),
            rules=rules,
            total_points=session['total_points'],
            already_scored=session['already_scored'],
            game_over_message=game_over_message,
            error_message=error_message
        )
