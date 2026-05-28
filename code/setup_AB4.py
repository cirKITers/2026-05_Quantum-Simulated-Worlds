import template.output as output
import template.questions as questions


def setup_erfolg():
    output.correct("Pakete, Daten und Funktionen erfolgreich geladen.")


def check_oracle(oracle, typ):
    """
    Prüft ob ein Orakel dem angegebenen Typ entspricht.

    Args:
        oracle: Eine Funktion, die eine Zahl als Eingabe nimmt und 0 oder 1 zurückgibt
        typ: Entweder "constant" oder "balanced"
    """
    # Teste mit mehreren Eingaben (0-19 = 20 verschiedene Eingaben)
    results = [oracle(x) for x in range(20)]

    if typ == "constant":
        # Constant: Alle Ergebnisse müssen gleich sein (alle 0 oder alle 1)
        if len(set(results)) == 1 and results[0] in (0, 1):
            output.correct(
                "Das Orakel (constant) ist korrekt, da alle Ausgaben gleich sind."
            )
            return

    elif typ == "balanced":
        # Balanced: Etwa die Hälfte 0, Hälfte 1
        count_0 = results.count(0)
        count_1 = results.count(1)
        # Erlaube etwas Spielraum
        if count_0 >= 7 and count_1 >= 7:
            output.correct(
                "Das Orakel (balanced) ist korrekt, da es ungefähr zur Hälfte 0 als auch 1 zurückgibt."
            )
            return
    else:
        output.wrong(
            f"Ungültiger Orakeltyp: '{typ}'. Erwarte 'constant' oder 'balanced'."
        )
        return
    output.wrong(f"Das Orakel entspricht nicht dem Typ '{typ}'. Ergebnisse: {results}")


def prompt_1a():
    """Fragt die Schüler nach der Komplexität für DJ-Orakel im Klassischen Modell."""
    questions.prompt_answer_with_check(
        "AB4-1a",
        input_prompt="Anzahl notwendiger Fragen",
        input_description="Deine Antwort zur Anzahl notwendiger Fragen im Klassischen Modell:",
        check_func=lambda x: x.replace(" ", "") == "N/2+1",
        success_message="Richtig! Im klassischen Modell benötigt man im schlimmsten Fall N/2 + 1 Fragen, um sicher zu sein, ob die Funktion konstant oder balanciert ist.",
        error_message="Das ist leider nicht korrekt. Überlege, wie viele mögliche Eingaben es gibt und wie viele davon konstant oder balanciert sein können. Im schlimmsten Fall sind die Antworten sortiert...",
    )
