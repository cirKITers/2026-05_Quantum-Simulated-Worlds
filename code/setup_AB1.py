import IPython
import numpy as np
import pandas as pd
from IPython.display import HTML, display, clear_output

import template.output as output
import template.questions as questions
import template.text_order_widget as text_order_widget
import template.table_widget as table


def setup_erfolg():
    output.correct("Pakete, Daten und Funktionen erfolgreich geladen.")


def prompt_3b():
    """Fragt die Schüler nach ihrer Hypothese zur Messung von |+⟩."""
    questions.prompt_answer(
        "AB1-3b",
        input_prompt="Deine Hypothese",
        input_description="Deine Hypothese zur Messung von |+⟩:",
    )


def prompt_4a():
    """Fragt die Schüler nach ihren Beobachtungen zu eigenen Messungen"""
    questions.prompt_answer(
        "AB1-4a",
        input_prompt="Deine Beobachtungen",
        input_description="Deine Beobachtungen zu deinen eigenen Messungen:",
    )


def check_1a(ket_0, ket_1, ket_plus):
    """Überprüft, ob ket_0, ket_1 und ket_plus korrekt gesetzt wurden."""
    # Erwartete Werte
    expected_ket_0 = np.array([1, 0])
    expected_ket_1 = np.array([0, 1])
    expected_ket_plus = np.array([1 / np.sqrt(2), 1 / np.sqrt(2)])

    # Prüfe ket_0
    if ket_0 is None:
        output.wrong("Bitte denke daran, ket_0 zu definieren.")
    elif np.allclose(ket_0, expected_ket_0):
        output.correct("ket_0 ist korrekt!")
    else:
        output.wrong("ket_0 ist nicht korrekt. Bitte überleg nochmal.")

    # Prüfe ket_1
    if ket_1 is None:
        output.wrong("Bitte denke daran, ket_1 zu definieren.")
    elif np.allclose(ket_1, expected_ket_1):
        output.correct("ket_1 ist korrekt!")
    else:
        output.wrong("ket_1 ist nicht korrekt. Bitte überleg nochmal.")

    # Prüfe ket_plus
    if ket_plus is None:
        output.wrong("Bitte denke daran, ket_plus zu definieren.")
    elif np.allclose(ket_plus, expected_ket_plus):
        output.correct("ket_plus ist korrekt! Superposition korrekt definiert.")
    else:
        output.wrong("ket_plus ist nicht korrekt.")


def check_1b(norm, prob_0, prob_1):
    """Überprüft, ob norm, prob_0 und prob_1 korrekt berechnet wurden."""
    # Erwartete Werte für ket_plus = [1/√2, 1/√2]
    expected_norm = 1.0
    expected_prob_0 = 0.5
    expected_prob_1 = 0.5

    # Prüfe norm
    if norm is None:
        output.wrong("Bitte denke daran, die Norm zu berechnen.")
    elif np.isclose(norm, expected_norm):
        output.correct("Die Norm ist korrekt!")
    else:
        output.wrong(f"Die Norm ist nicht korrekt.")

    # Prüfe prob_0
    if prob_0 is None:
        output.wrong("Bitte denke daran, die Wahrscheinlichkeit für |0⟩ zu berechnen.")
    elif np.isclose(prob_0, expected_prob_0):
        output.correct("Die Wahrscheinlichkeit für |0⟩ ist korrekt!")
    else:
        output.wrong(
            f"Die Wahrscheinlichkeit für |0⟩ ist nicht korrekt. P(|0⟩) = |Amplitude|²."
        )

    # Prüfe prob_1
    if prob_1 is None:
        output.wrong("Bitte denke daran, die Wahrscheinlichkeit für |1⟩ zu berechnen.")
    elif np.isclose(prob_1, expected_prob_1):
        output.correct("Die Wahrscheinlichkeit für |1⟩ ist korrekt!")
    else:
        output.wrong(
            f"Die Wahrscheinlichkeit für |1⟩ ist nicht korrekt. P(|1⟩) = |Amplitude|²."
        )


# ---------------------------------------------------------------------------------------------------------------------------------------------------


def show_bloch():
    """Interaktives Bloch-Sphere-Widget mit Slidern für θ und φ."""
    import matplotlib.pyplot as plt
    from qiskit.quantum_info import Statevector
    import ipywidgets as widgets

    def bloch_from_angles(theta, phi):
        """Return a Statevector corresponding to Bloch‑Koordinaten (θ, φ)."""
        a = np.cos(theta / 2)
        b = np.exp(1j * phi) * np.sin(theta / 2)
        return Statevector([a, b])

    theta_slider = widgets.FloatSlider(
        min=0,
        max=2 * np.pi,
        step=0.01,
        value=np.pi / 2,
        description="θ",
        continuous_update=True,
    )
    phi_slider = widgets.FloatSlider(
        min=0,
        max=2 * np.pi,
        step=0.01,
        value=0,
        description="φ",
        continuous_update=True,
    )

    output = widgets.Output()

    def update_plot(change=None):
        with output:
            clear_output(wait=True)
            sv = bloch_from_angles(theta_slider.value, phi_slider.value)
            sv.draw("bloch")
            plt.show()

    theta_slider.observe(update_plot, names="value")
    phi_slider.observe(update_plot, names="value")

    display(theta_slider, phi_slider, output)
    update_plot()  # initial plot
