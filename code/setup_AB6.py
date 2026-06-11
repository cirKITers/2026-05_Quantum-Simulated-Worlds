import template.output as output
import template.text_multiple_choice_widget as multiple_choice_widget
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
import random
import numpy as np


def setup_erfolg():
    output.correct("Pakete, Daten und Funktionen erfolgreich geladen.")


def show_multi_selection_1a():
    # Wie kann eine Markdown-Zelle neu gerendert werden?
    multiple_choice_widget.show_multiple_choice_with_feedback(
        [
            ("Man braucht mindestens N Klicks, um das Spiel zu gewinnen", False),
            (
                "Man braucht jeden Knopf nur maximal einmal zu drücken",
                True,
            ),  # Liste der möglichen Einträge
            ("Die Reihenfolge der Klicks ist egal", True),
            ("Es macht keinen Sinn eine ausgeschaltete Lampe zu schalten", False),
        ],
        feedback_messages={
            "success": "Korrekt! Gut gemacht.",
            "wrong": "Da hast du leider mindestens eine falsche Option ausgewählt.",
            "missing": (
                "Du hast schon einiges korrekt, aber es gibt noch weitere Möglichkeiten, die du in Betracht ziehen kannst."  # noqa: E501
            ),
            "nothing_selected": "Bitte wähle mindestens eine Option aus.",
        },
    )


# Spiel-Klasse für Lights-out
class LightsOutGame:
    def __init__(self, size=3):
        self.size = size
        self.field = [[0] * size for _ in range(size)]
        self.clicked_cells = []  # Liste der geklickten Felder
        self.buttons = []
        self.output = widgets.Output()
        self.status_label = widgets.HTML()
        self.history_label = widgets.HTML()  # Anzeige der Klick-Historie
        self.new_game_button = widgets.Button(
            description="🔄 Neues Spiel",
            button_style="success",
            layout=widgets.Layout(width="150px", height="40px"),
        )
        self.new_game_button.on_click(self.new_game)

        self.create_buttons()
        self.display_game()

    def create_buttons(self):
        """Erstellt die 9 Buttons für das Spielfeld"""
        self.buttons = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                btn = widgets.Button(
                    description="💡", layout=widgets.Layout(width="60px", height="60px")
                )
                btn.style.button_color = "#FFD700"
                btn.on_click(lambda x, row=i, col=j: self.on_click(row, col))
                row.append(btn)
            self.buttons.append(row)

    def toggle(self, row, col):
        """Toggle das Feld und seine Nachbarn"""
        # Toggle das Feld selbst
        self.field[row][col] = 1 - self.field[row][col]

        # Toggle Nachbarn (oben, unten, links, rechts)
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

        for r, c in neighbors:
            if 0 <= r < self.size and 0 <= c < self.size:
                self.field[r][c] = 1 - self.field[r][c]

    def on_click(self, row, col):
        """Wird aufgerufen, wenn ein Button geklickt wird"""
        # Toggle das Feld
        self.toggle(row, col)

        # Füge das geklickte Feld zur Historie hinzu
        self.clicked_cells.append((row, col))

        self.update_display()
        self.check_win()
        self.update_history()

    def check_win(self):
        """Prüft, ob alle Lichter aus sind"""
        won = all(
            self.field[r][c] == 0 for r in range(self.size) for c in range(self.size)
        )
        if won:
            self.status_label.value = '<h2 style="color: green; text-align: center;">🎉 Glückwunsch! Alle Lichter aus!</h2>'
        else:
            moves = sum(sum(row) for row in self.field)
            self.status_label.value = f'<p style="text-align: center;">Anzahl eingeschaltete Lichter: <b>{moves}</b></p>'

    def update_display(self):
        """Aktualisiert die Anzeige der Buttons"""
        for i in range(self.size):
            for j in range(self.size):
                btn = self.buttons[i][j]
                if self.field[i][j] == 1:  # An
                    btn.description = "💡"
                    btn.style.button_color = "#FFD700"
                    btn.style.font_weight = "bold"
                else:  # Aus
                    btn.description = "⚫"
                    btn.style.button_color = "#606060"
                    btn.style.font_weight = "normal"

    def update_history(self):
        """Aktualisiert die Anzeige der Klick-Historie"""
        if not self.clicked_cells:
            self.history_label.value = '<p style="text-align: center; color: #888;">Noch keine Felder geklickt</p>'
            return

        # Erstelle eine lesbare Darstellung
        history_text = '<div style="text-align: center; margin: 10px 0;">'
        history_text += "<b>Geklickte Felder:</b><br>"

        # Zeige die Felder als Grid
        history_text += '<div style="display: inline-block; background: #f0f0f0; padding: 10px; border-radius: 8px;">'
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) in self.clicked_cells:
                    history_text += '<span style="display: inline-block; width: 30px; height: 30px; background: #FFD700; border-radius: 4px; margin: 2px; text-align: center; line-height: 30px;"></span>'
                else:
                    history_text += '<span style="display: inline-block; width: 30px; height: 30px; background: #ddd; border-radius: 4px; margin: 2px;"></span>'
            history_text += "<br>"
        history_text += "</div>"

        # Zeige die Reihenfolge der Klicks
        history_text += "<br><b>Reihenfolge:</b> "
        history_text += " → ".join([f"({r+1},{c+1})" for r, c in self.clicked_cells])
        history_text += f"<br><b>Anzahl Klicks:</b> {len(self.clicked_cells)}"
        history_text += "</div>"

        self.history_label.value = history_text

    def new_game(self, b=None):
        """Startet ein neues Spiel mit zufälliger Konfiguration"""
        # Zufällige Konfiguration (mindestens 3 Lichter an)
        while True:
            self.field = [
                [random.randint(0, 1) for _ in range(self.size)]
                for _ in range(self.size)
            ]
            # Mindestens 3 Lichter einschalten
            if sum(sum(row) for row in self.field) >= 3:
                break

        # Historie zurücksetzen
        self.clicked_cells = []

        self.update_display()
        self.check_win()
        self.update_history()

    def display_game(self):
        """Zeigt das Spiel an"""
        # Erstelle das Grid
        grid = widgets.GridBox(
            [btn for row in self.buttons for btn in row],
            layout=widgets.Layout(
                grid_template_columns="repeat(3, 70px)",
                grid_gap="5px",
                justify_content="center",
                margin="20px 0",
            ),
        )

        # Layout zusammenbauen
        title = widgets.HTML(
            '<h1 style="text-align: center; color: #333;">🎮 Lights-out</h1>'
        )
        instructions = widgets.HTML(
            '<p style="text-align: center; color: #666;">Klicke auf ein Licht, um es und seine Nachbarn umzuschalten!</p>'
        )

        display(
            widgets.VBox(
                [
                    title,
                    instructions,
                    grid,
                    self.status_label,
                    self.history_label,
                    widgets.HTML('<div style="text-align: center; margin-top: 20px;">'),
                    self.new_game_button,
                    widgets.HTML("</div>"),
                ]
            )
        )

        # Starte ein neues Spiel
        self.new_game()
