import template.output as output
import template.questions as questions
import template.table_widget as table


def setup_erfolg():
    output.correct("Pakete, Daten und Funktionen erfolgreich geladen.")


def prompt_1a():
    """Fragt die Schüler nach ihrer Beobachtung zu den Pauli Gates."""
    questions.prompt_answer(
        "AB2-1a",
        input_prompt="Deine Beobachtungen",
        input_description="Deine Beobachtungen zu den Pauli-Gattern:",
    )


def prompt_1b():
    """Fragt die Schüler nach ihrer Hypothese zur Messung von H."""
    questions.prompt_answer(
        "AB2-1b",
        input_prompt="Deine Hypothese",
        input_description="Deine Hypothese zur Messung des Hadamard-Gatters:",
    )


def show_truth_table():
    table_content = [
        [
            table.Header("Input 1. Qubit"),
            table.Header("Input 2. Qubit"),
            table.Header("Output 1. Qubit"),
            table.Header("Output 2. Qubit"),
        ],
        [table.TextInput(), table.TextInput(), table.TextInput(), table.TextInput()],
        [table.TextInput(), table.TextInput(), table.TextInput(), table.TextInput()],
        [table.TextInput(), table.TextInput(), table.TextInput(), table.TextInput()],
        [table.TextInput(), table.TextInput(), table.TextInput(), table.TextInput()],
    ]
    column_widths = [120, 120, 120, 120]

    def check_table(text_cells):
        correct = set()

        for row in text_cells:
            if row[0] == "0" and row[1] == "0" and row[2] == "0" and row[3] == "0":
                correct.add("00")
            elif row[0] == "0" and row[1] == "1" and row[2] == "0" and row[3] == "1":
                correct.add("01")
            elif row[0] == "1" and row[1] == "0" and row[2] == "1" and row[3] == "1":
                correct.add("10")
            elif row[0] == "1" and row[1] == "1" and row[2] == "1" and row[3] == "0":
                correct.add("11")
        if len(correct) == 4:
            return table.CORRECT, "Korrekt."
        else:
            return (
                table.WRONG,
                f"Falsch. Bitte überprüfe, ob du alle möglichen Eingaben berücksichtigt hast und die richtigen Ausgaben zugeordnet hast. {correct}",
            )

    table.show_table("AB2-2a", table_content, column_widths, check_func=check_table)


def check_2b(halbaddierer):
    """Überprüft die Implementierung des Halbaddierers."""
    correct = True
    for a in [0, 1]:
        for b in [0, 1]:
            sum_out, carry_out = halbaddierer(a, b)
            expected_sum = a ^ b  # XOR für Summe
            expected_carry = a & b  # AND für Carry
            if sum_out != expected_sum or carry_out != expected_carry:
                correct = False
                break
    if correct:
        output.correct("Der Halbaddierer ist korrekt implementiert.")
    else:
        output.wrong(
            "Der Halbaddierer ist nicht korrekt implementiert. Bitte überprüfe deine Logik."
        )


def check_3a(volladdierer):
    """Überprüft die Implementierung des Volladdierers."""
    correct = True
    for a in [0, 1]:
        for b in [0, 1]:
            for carry_in in [0, 1]:
                sum_out, carry_out = volladdierer(a, b, carry_in)
                expected_sum = a ^ b ^ carry_in  # XOR für Summe
                expected_carry = (a & b) | (carry_in & (a ^ b))  # Carry-Logik
                if sum_out != expected_sum or carry_out != expected_carry:
                    correct = False
                    break
    if correct:
        output.correct("Der Volladdierer ist korrekt implementiert.")
    else:
        output.wrong(
            "Der Volladdierer ist nicht korrekt implementiert. Bitte überprüfe deine Logik."
        )


def prompt_3b():
    """Fragt die Schüler nach ihren Beobachtungen zur Kommutativität von X und H."""
    questions.prompt_answer(
        "AB2-3b",
        input_prompt="Deine Beobachtungen",
        input_description="Deine Beobachtungen zur Messung Kommutativität und anderen Experimenten:",
    )
