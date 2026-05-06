import template.output as output
import template.questions as questions
import template.text_order_widget as text_order_widget
import template.text_selection_widget as text_selection_widget
import template.text_multiple_choice_widget as multiple_choice_widget


def setup_erfolg():
    output.correct("Pakete, Daten und Funktionen erfolgreich geladen.")


def check_1a(name, age, city):
    """Überprüft die Antworten zur ersten Aufgabe."""
    # Erwartete Werte
    expected_name = "Max Mustermann"
    expected_age = 25
    expected_city = "Karlsruhe"

    all_correct = True

    # Prüfe name
    if name is None or (isinstance(name, str) and name.strip() == ""):
        output.wrong("Bitte gib den Namen 'Max Mustermann' ein.")
        all_correct = False
    elif not isinstance(name, str):
        output.wrong("Der Name sollte ein String sein, keine Zahl.")
        all_correct = False
    elif name.strip() == expected_name:
        output.correct("Der Name ist korrekt!")
    else:
        output.wrong("Der Name ist nicht ganz richtig. Versuche es nochmal.")
        all_correct = False

    # Prüfe age
    if age is None:
        output.wrong("Bitte gib das Alter '25' ein.")
        all_correct = False
    elif age == expected_age:
        output.correct("Das Alter ist korrekt!")
    else:
        output.wrong("Das Alter ist nicht korrekt.")
        all_correct = False

    # Prüfe city
    if city is None or (isinstance(city, str) and city.strip() == ""):
        output.wrong("Bitte gib die Stadt 'Karlsruhe' ein.")
        all_correct = False
    elif not isinstance(city, str):
        output.wrong("Die Stadt sollte ein String sein, keine Zahl.")
        all_correct = False
    elif city.strip() == expected_city:
        output.correct("Die Stadt ist korrekt!")
    else:
        output.wrong("Die Stadt ist nicht korrekt.")
        all_correct = False

    if all_correct:
        output.correct(
            "Alle Antworten sind korrekt! Du hast die erste Aufgabe gemeistert."
        )


def check_3a(answer):
    """Überprüft die Antwort zur Frage über Jupyter Notebooks."""
    answer_lower = answer.lower().strip()

    if "code" in answer_lower and "markdown" in answer_lower:
        return True
    return False


def prompt_2a():
    questions.prompt_answer(
        "AB0-2a",
        input_prompt="Deine Antwort",
        input_description="Beispiel: Was hast du heute gelernt?",
    )


def show_text_order_2b():  # Beispiel: Texte sortieren
    richtige_reihenfolge = ["Erst denken", "Dann codieren", "Ergebnis prüfen"]
    text_order_widget.show_text_order(richtige_reihenfolge, option_width="75%")


def show_selection_2c():  # Beispiel: Radio-Buttons
    # Beispiel: Radio-Buttons
    optionen = [
        ("Die Antwort A", False, "Das ist nicht korrekt."),
        ("Die Antwort B", True, "Richtig! Das ist die korrekte Antwort."),
        ("Die Antwort C", False, "Leider falsch."),
    ]
    text_selection_widget.show_text_selection(optionen, height="35px")


def prompt_3a():
    # Gib hier deine Antwort ein
    questions.prompt_answer_with_check(
        "AB0-3a",
        input_prompt="Deine Antwort",
        input_description="Antwort zu Frage 3a:",
        check_func=check_3a,
        success_message="Korrekt! Jupyter Notebooks bestehen aus Markdown- und Code-Zellen.",  # noqa: E501
        error_message="Denk nochmal darüber nach, zwischen welchen Zellen wir unterscheiden.",  # noqa: E501
    )


def show_multi_selection_3b():
    # Wie kann eine Markdown-Zelle neu gerendert werden?
    multiple_choice_widget.show_multiple_choice_with_feedback(
        [
            ("Ich scrolle einfach weiter", False),  # Liste der möglichen Einträge
            ("Shift + Enter oder Strg + Enter", True),
            ("Ich klicke auf das Häkchen im Bearbeiten-Menü der Zelle", True),
            ("Ich lade das Notebook neu", False),
            ("Ich frage Gabriel oder Eileen", True),
        ],
        feedback_messages={
            "success": "Korrekt! Gut gemacht.",
            "wrong": (
                "Da hast du leider mindestens eine falsche Option ausgewählt. Nichts tun ist meist keine Lösung ;)"  # noqa: E501
            ),
            "missing": (
                "Du hast schon einiges korrekt, aber es gibt noch weitere Möglichkeiten, die du in Betracht ziehen kannst."  # noqa: E501
            ),
            "nothing_selected": "Bitte wähle mindestens eine Option aus.",
        },
    )
