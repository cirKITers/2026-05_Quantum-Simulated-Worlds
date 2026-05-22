import template.output as output
import template.questions as questions


def setup_erfolg():
    output.correct("Pakete, Daten und Funktionen erfolgreich geladen.")


def prompt_2a():
    """Fragt die Schüler nach ihren Beobachtungen zum GHZ-Zustand."""
    questions.prompt_answer(
        "AB2-1a",
        input_prompt="Deine Beobachtungen",
        input_description="Deine Beobachtungen zum GHZ-Zustand:",
    )
