# HiSim: Quantencomputing simuliert für Schüler:innen

Dieses Projekt gibt eine leichte Einführung in das Thema Quantencomputing für Schülerinnen und Schüler.
Die Arbeitsblätter liegen als Jupyter-Notebooks im Ordner `./worksheets` und behandeln jeweils ein Themenfeld der folgenden Wochen:

- [Einführung in die Arbeit mit Jupyter Notebooks](worksheets/AB0_Einfuehrung.ipynb)
- Woche 1: [Qubits und die Bloch Sphere](worksheets/AB1_Qubits.ipynb)
- Woche 2: [Wichtige Gates und Quantenschaltkreise](worksheets/AB2_Gates.ipynb)
- Woche 3: [Verschränkung und Bell States](worksheets/AB3_Entanglement.ipynb)
- Woche 4: [Der Deutsch-Jozsa Algorithmus](worksheets/AB4_DeutschJozsa.ipynb)
- Woche 5: [Suchen mit dem Grover Algorithmus](worksheets/AB5_Grover.ipynb)
- Woche 6: [Finales Projekt: Lights Out mit dem Quantencomputer](worksheets/AB6_LightsOut.ipynb)

Als Startpunkt dient das Notebook [Start.ipynb](Start.ipynb), in dem alle Arbeitsblätter verlinkt sind.

## Lokale Einrichtung

Damit du die Notebooks auf dem eigenen Rechner ausführen kannst, empfehlen wir dir eine virtuelle Python-Umgebung, damit die Abhängigkeiten dieses Projekts nicht mit anderen Projekten kollidieren.
Zum Einrichten wechselst du zunächst in einem Terminal in den Projektordner und führst dann die folgenden Befehle aus:

1. Virtuelle Umgebung anlegen (Python 3.10):

   ```bash
   python3.10 -m venv venv
   ```

2. Virtuelle Umgebung aktivieren:

   ```bash
   # macOS / Linux
   source venv/bin/activate
   ```
   ```bat
   :: Windows
   venv\Scripts\activate
   ```

3. Abhängigkeiten installieren:

   ```bash
   pip install -r requirements.txt
   ```

4. Jupyter-Kernel registrieren:

   ```bash
   python -m ipykernel install --user --name hisim-quantencomputing
   ```

5. JupyterLab starten:

   ```bash
   jupyter lab
   ```

## Mit den Arbeitsblättern arbeiten

- In JupyterLab öffnest du zunächst [Start.ipynb](Start.ipynb) und kannst dann über die Links zu den Arbeitsblättern der einzelnen Wochen navigieren.
- Beim ersten Öffnen eines Notebooks wählst du oben rechts den Kernel `hisim-quantencomputing` aus.
- Beim Wechsel zwischen Arbeitsblättern solltest du bei Problemen mit den interaktiven Widgets den Kernel neu starten (Menü "Kernel > Restart Kernel").
