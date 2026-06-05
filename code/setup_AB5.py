import template.output as output
import template.questions as questions
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import IntSlider, Dropdown, fixed, Output
from IPython.display import display
import matplotlib


def setup_erfolg():
    output.correct("Pakete, Daten und Funktionen erfolgreich geladen.")


def berechne_grover_amplituden(n_qubits, ziel_index, iterationen):
    """
    Berechnet die Amplituden nach einer bestimmten Anzahl von Grover-Iterationen
    """
    N = 2**n_qubits

    # Anfangsamplitude: alle gleich (1/√N)
    alpha = 1 / np.sqrt(N)  # Amplitude des gesuchten Zustands
    beta = 1 / np.sqrt(N)  # Amplitude jedes nicht-gesuchten Zustands

    for _ in range(iterationen):
        # Orakel: Spiegelt die Amplitude des gesuchten Zustands
        alpha = -alpha

        # Diffusion: Spiegelung um den Durchschnitt aller Amplituden
        mean = (alpha + (N - 1) * beta) / N
        alpha = 2 * mean - alpha
        beta = 2 * mean - beta

    return alpha, beta


def plot_grover_geometrie(n_qubits, iterationen, ziel_name):
    """
    Zeigt die geometrische Interpretation einer Grover-Iteration
    """
    N = 2**n_qubits

    # Berechne Amplituden
    alpha, beta = berechne_grover_amplituden(n_qubits, 0, iterationen)

    # Vektor im 2D-Raum: x = nicht-gesucht, y = gesucht
    x = beta * np.sqrt(N - 1)  # Skaliert für Visualisierung
    y = alpha * np.sqrt(1)

    # Erstelle Figure
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))

    # Koordinatensystem
    ax.axhline(y=0, color="gray", linestyle="-", linewidth=0.5)
    ax.axvline(x=0, color="gray", linestyle="-", linewidth=0.5)

    # Achsen beschriften
    ax.annotate(
        "|r⟩ (nicht gesucht)", xy=(1.05, 0), fontsize=12, ha="left", color="#E74C3C"
    )
    ax.annotate(
        "|w⟩ (gesucht)", xy=(0, 1.05), fontsize=12, ha="center", color="#3498DB"
    )

    # Einheitsvektoren (gestrichelt)
    ax.plot([0, 1], [0, 0], "r--", alpha=0.3, linewidth=2)
    ax.plot([0, 0], [0, 1], "b--", alpha=0.3, linewidth=2)

    # Vektor zeichnen
    vector_scale = 0.8
    ax.arrow(
        0,
        0,
        x * vector_scale,
        y * vector_scale,
        head_width=0.05,
        head_length=0.03,
        fc="#2ECC71",
        ec="#27AE60",
        linewidth=3,
    )

    # Winkel einzeichnen
    if x > 0.01 or y > 0.01:
        angle = np.arctan2(y, x)
        theta_arc = np.linspace(0, angle, 50)
        ax.plot(0.15 * np.cos(theta_arc), 0.15 * np.sin(theta_arc), "g-", linewidth=2)
        ax.text(0.2, 0.05, f"θ={angle*180/np.pi:.1f}°", fontsize=11, color="green")

    # Wahrscheinlichkeiten
    prob_gesucht = alpha**2
    prob_nicht_gesucht = beta**2 * (N - 1)

    # Text-Box mit Informationen
    info_text = f"Iteration: {iterationen}\n"
    info_text += f"Amplitude |w⟩: {alpha:.3f}\n"
    info_text += f"Amplitude |r⟩: {beta:.3f}\n"
    info_text += f"\nP(|w⟩) = {prob_gesucht:.1%}\n"
    info_text += f"P(|r⟩) = {prob_nicht_gesucht:.1%}"

    ax.text(
        0.02,
        0.98,
        info_text,
        transform=ax.transAxes,
        fontsize=11,
        verticalalignment="top",
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8),
    )

    # Titel
    ax.set_title(
        f'Geometrie von Grover: {ziel_name}\n({n_qubits} Qubits, {iterationen} Iteration{"en" if iterationen != 1 else ""})',
        fontsize=14,
        fontweight="bold",
    )

    # Achsen gleich lang
    max_val = max(abs(x), abs(y), 1) * 1.3
    ax.set_xlim(-max_val, max_val)
    ax.set_ylim(-max_val, max_val)
    ax.set_aspect("equal")

    ax.axis("off")
    plt.tight_layout()
    return fig


def show_interactive_grover():
    print("🔍 Interaktive Grover-Geometrie:")
    print("Verwende die Regler, um die Anzahl der Iterationen zu ändern!")

    iteration_slider = IntSlider(
        min=0, max=5, step=1, value=0, description="Iterationen:"
    )
    out_grover = Output()

    def update_grover_geometrie(change=None):
        with out_grover:
            out_grover.clear_output(wait=True)
            plt.close("all")
            fig = plot_grover_geometrie(3, iteration_slider.value, "|101⟩")
            plt.close(fig)
            display(fig)

    iteration_slider.observe(update_grover_geometrie, names="value")
    display(iteration_slider, out_grover)

    update_grover_geometrie()


def plot_spiegelungen_erklaerung():
    """
    Zeigt die zwei Spiegelungen einer Grover-Iteration und wie sie zu einer Drehung führen
    """
    fig, axes = plt.subplots(1, 4, figsize=(18, 5))

    # Für 3 Qubits mit 1 Suchzustand
    n_qubits = 3
    N = 2**n_qubits
    # Korrekte Anfangswinkel für Grover: arcsin(1/√N)
    init_angle = np.arcsin(1 / np.sqrt(N))  # ≈ 20.7° für 3 Qubits
    scale = 0.8

    # Teil 1: Start
    ax = axes[0]
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")

    ax.axhline(y=0, color="gray", linestyle="-", linewidth=0.3, alpha=0.5)
    ax.axvline(x=0, color="gray", linestyle="-", linewidth=0.3, alpha=0.5)
    ax.annotate("|r⟩", xy=(1.3, 0), fontsize=11, color="#E74C3C", fontweight="bold")
    ax.annotate("|w⟩", xy=(0, 1.3), fontsize=11, color="#3498DB", fontweight="bold")

    # Vektor (Superposition: korrekte Amplitude)
    ax.arrow(
        0,
        0,
        scale * np.cos(init_angle),
        scale * np.sin(init_angle),
        head_width=0.08,
        head_length=0.05,
        fc="#2ECC71",
        ec="#27AE60",
        linewidth=3,
    )

    # Winkel zeigen
    theta_arc = np.linspace(0, init_angle, 20)
    ax.plot(0.15 * np.cos(theta_arc), 0.15 * np.sin(theta_arc), "g-", linewidth=2)
    ax.text(
        0.25,
        0.1,
        f"θ₀={init_angle*180/np.pi:.1f}°",
        fontsize=10,
        color="green",
        fontweight="bold",
    )

    ax.set_title("1. Start\n(Superposition)", fontsize=12, fontweight="bold")

    # Teil 2: Nach Orakel (Spiegelung an |r⟩-Achse / x-Achse)
    ax = axes[1]
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")

    ax.axhline(y=0, color="gray", linestyle="-", linewidth=0.3, alpha=0.5)
    ax.axvline(x=0, color="gray", linestyle="-", linewidth=0.3, alpha=0.5)
    ax.annotate("|r⟩", xy=(1.3, 0), fontsize=11, color="#E74C3C", fontweight="bold")
    ax.annotate("|w⟩", xy=(0, 1.3), fontsize=11, color="#3498DB", fontweight="bold")

    # MIRROR 1: Spiegelungsachse (|r⟩-Achse) prominent zeigen
    ax.plot([-1.2, 1.2], [0, 0], "r-", linewidth=3, alpha=0.7, label="Spiegelungsachse")
    ax.text(
        1.0,
        0.25,
        "Orakel-Achse\n(an |r⟩)",
        fontsize=10,
        color="#E74C3C",
        fontweight="bold",
        bbox=dict(boxstyle="round", facecolor="yellow", alpha=0.3),
    )

    # Vektor nach Orakel (gespiegelt)
    oracle_angle = -init_angle
    ax.arrow(
        0,
        0,
        scale * np.cos(oracle_angle),
        scale * np.sin(oracle_angle),
        head_width=0.08,
        head_length=0.05,
        fc="#2ECC71",
        ec="#27AE60",
        linewidth=3,
    )

    # Winkel zeigen
    theta_arc = np.linspace(oracle_angle, 0, 20)
    ax.plot(
        0.15 * np.cos(theta_arc),
        0.15 * np.sin(theta_arc),
        "r--",
        linewidth=2,
        alpha=0.6,
    )

    ax.set_title(
        "2. Nach Orakel\nSpiegelung an |r⟩-Achse", fontsize=12, fontweight="bold"
    )

    # Teil 3: Die zweite Spiegelungsachse (Diffusion-Achse)
    ax = axes[2]
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")

    ax.axhline(y=0, color="gray", linestyle="-", linewidth=0.3, alpha=0.5)
    ax.axvline(x=0, color="gray", linestyle="-", linewidth=0.3, alpha=0.5)
    ax.annotate("|r⟩", xy=(1.3, 0), fontsize=11, color="#E74C3C", fontweight="bold")
    ax.annotate("|w⟩", xy=(0, 1.3), fontsize=11, color="#3498DB", fontweight="bold")

    # Vektor vor zweiter Spiegelung (vom Orakel)
    ax.arrow(
        0,
        0,
        scale * np.cos(oracle_angle),
        scale * np.sin(oracle_angle),
        head_width=0.08,
        head_length=0.05,
        fc="#2ECC71",
        ec="#27AE60",
        linewidth=3,
        alpha=0.7,
    )

    # MIRROR 2: Diffusions-Achse (Spiegelung an der Richtung der Superposition)
    # Die Diffusion spiegelt an der Richtung des Superpositionszustands (bei init_angle)
    bisector_angle = init_angle

    ax.plot(
        [-1.2 * np.cos(bisector_angle), 1.2 * np.cos(bisector_angle)],
        [-1.2 * np.sin(bisector_angle), 1.2 * np.sin(bisector_angle)],
        "b-",
        linewidth=3,
        alpha=0.7,
    )
    ax.text(
        0.6,
        0.8,
        "Diffusion-Achse\n(Superposition-Richtung)",
        fontsize=10,
        color="#3498DB",
        fontweight="bold",
        bbox=dict(boxstyle="round", facecolor="lightblue", alpha=0.3),
    )

    ax.set_title(
        "3. Diffusion-Achse\n(Zweite Spiegelungsachse)", fontsize=12, fontweight="bold"
    )

    # Teil 4: Nach beiden Spiegelungen = Drehung
    ax = axes[3]
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")

    ax.axhline(y=0, color="gray", linestyle="-", linewidth=0.3, alpha=0.5)
    ax.axvline(x=0, color="gray", linestyle="-", linewidth=0.3, alpha=0.5)
    ax.annotate("|r⟩", xy=(1.3, 0), fontsize=11, color="#E74C3C", fontweight="bold")
    ax.annotate("|w⟩", xy=(0, 1.3), fontsize=11, color="#3498DB", fontweight="bold")

    # Vektor nach beiden Spiegelungen: gedreht um 2θ₀
    # Die Drehung ist um 2*init_angle (Eigenschaften von zwei Spiegelungen)
    final_angle = init_angle + 2 * init_angle  # = 3*init_angle
    ax.arrow(
        0,
        0,
        scale * np.cos(final_angle),
        scale * np.sin(final_angle),
        head_width=0.08,
        head_length=0.05,
        fc="#2ECC71",
        ec="#27AE60",
        linewidth=3,
    )

    # Gesamtdrehungswinkel
    theta_arc = np.linspace(init_angle, final_angle, 30)
    ax.plot(0.2 * np.cos(theta_arc), 0.2 * np.sin(theta_arc), "g-", linewidth=2)
    ax.text(
        0.05,
        0.25,
        f"Drehung\num 2θ₀\n≈{2*init_angle*180/np.pi:.1f}°",
        fontsize=10,
        color="green",
        fontweight="bold",
    )

    ax.set_title(
        "4. Nach Diffusion\nZwei Spiegelungen = Drehung", fontsize=12, fontweight="bold"
    )

    plt.suptitle(
        f"Grover-Iteration (3 Qubits): Zwei Spiegelungen führen zu einer Drehung um 2θ₀",
        fontsize=14,
        fontweight="bold",
        y=1.00,
    )
    plt.tight_layout()
    plt.close("all")
    return fig


def show_grover_spiegelung_visualisierung():
    # Zeige die Erklärung
    print("📐 Die zwei Spiegelungen des Grover-Algorithmus:")
    fig_spiegelungen = plot_spiegelungen_erklaerung()
    display(fig_spiegelungen)


def show_grover_spiegelung_barplot(n_qubits=3, ziel_index=0):
    """Zeigt Balkendiagramme der Amplituden vor/nach Orakel und Diffusion

    Fügt die Spiegelungsachsen hinzu: für das Orakel die x-Achse (horizontale
    Spiegelachse bei y=0) und für die Diffusion eine horizontale Linie bei dem
    Mittelwert (Spiegelungsachse). Fügt eine Legende hinzu, die das rote Element
    als gesuchten Zustand kennzeichnet.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from IPython.display import display

    N = 2**n_qubits

    # Anfangsamplituden
    alpha = 1 / np.sqrt(N)
    beta = 1 / np.sqrt(N)
    amps_init = np.full(N, beta)
    amps_init[ziel_index] = alpha

    # Nach Orakel (Phase des Zielzustands invertiert)
    amps_oracle = amps_init.copy()
    amps_oracle[ziel_index] *= -1

    # Diffusion: Spiegelung um den Durchschnitt aller Amplituden
    mean = amps_oracle.mean()
    amps_diff = 2 * mean - amps_oracle

    # Plot
    fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharey=True)
    titles = [
        "1) Start (Superposition)",
        "2) Nach Orakel\n(Spiegelung am Ziel)",
        "3) Nach Diffusion\n(Spiegelung am Mittelwert)",
    ]
    data = [amps_init, amps_oracle, amps_diff]

    ymin = min(amps_init.min(), amps_oracle.min(), amps_diff.min())
    ymax = max(amps_init.max(), amps_oracle.max(), amps_diff.max())
    pad = max(abs(ymin), abs(ymax)) * 0.15
    ylim = (ymin - pad, ymax + pad)

    for ax, title, amps in zip(axes, titles, data):
        colors = ["#AAAAAA"] * N
        colors[ziel_index] = "#E74C3C"  # Zielzustand hervorheben
        ax.bar(range(N), amps, color=colors)
        ax.set_title(title, fontsize=11)
        ax.set_xlabel("Basiszustand (Index)")
        ax.set_xticks(range(N))
        ax.set_ylim(ylim)
        # kleine Mittellinie (Hilfsachse)
        ax.axhline(0, color="k", linewidth=0.4)

    # Orakel-Achse: Die Spiegelung des Orakels ist eine Spiegelung der Ziel-Amplitude
    # an der x-Achse (y=0). Zeichne diese hervorgehoben in der zweiten Spalte.
    axes[1].axhline(0, color="#E74C3C", linestyle="--", linewidth=2, alpha=0.9)
    axes[1].text(
        N - 0.5,
        0.02 * (ylim[1] - ylim[0]),
        "Orakel-Achse\n(|r⟩-Achse)",
        color="#E74C3C",
        fontsize=9,
        ha="right",
        va="bottom",
        fontweight="bold",
    )

    # Diffusion-Achse: horizontale Linie bei mean (Spiegelungsachse)
    axes[2].axhline(mean, color="#3498DB", linestyle="--", linewidth=2, alpha=0.8)
    axes[2].text(
        0.5,
        mean + (ymax - ymin) * 0.05,
        "Diffusion-Achse\n(Mittelwert)",
        color="#3498DB",
        fontsize=9,
        bbox=dict(boxstyle="round", facecolor="lightblue", alpha=0.3),
    )

    # Legende: rotes Element = gesuchter Zustand
    red_patch = mpatches.Patch(color="#E74C3C", label="Gesuchter Zustand (Ziel)")
    gray_patch = mpatches.Patch(color="#AAAAAA", label="Andere Zustände")
    # Platziere Legende in der ersten Achse oben rechts
    axes[0].legend(handles=[red_patch, gray_patch], loc="upper right", fontsize=9)

    plt.tight_layout()
    display(fig)
    plt.close(fig)
