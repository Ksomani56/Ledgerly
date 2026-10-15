"""
build_all_experiments.py - Master Orchestrator for Ledgerly WDL Lab Manuals.
Generates all 13 individual, fully-formatted academic experiment documents (.docx).
"""

import sys
from pathlib import Path

# Add current workspace to python path
WORKSPACE = Path(__file__).resolve().parent
if str(WORKSPACE) not in sys.path:
    sys.path.insert(0, str(WORKSPACE))

from generate_lab_docx import OUTPUT_DIR
from lab_experiments.exp_01_04 import (
    generate_exp_01, generate_exp_02, generate_exp_03, generate_exp_04
)
from lab_experiments.exp_05_07 import (
    generate_exp_05, generate_exp_06, generate_exp_07
)
from lab_experiments.exp_08_10 import (
    generate_exp_08, generate_exp_09, generate_exp_10
)
from lab_experiments.exp_11_13 import (
    generate_exp_11, generate_exp_12, generate_exp_13
)

EXPERIMENTS = [
    (1, "Project Selection and Conceptualization", generate_exp_01),
    (2, "Design Static Web Pages Required for the Project (HTML)", generate_exp_02),
    (3, "JavaScript Form Validation", generate_exp_03),
    (4, "Design a Web Page Using CSS (Cascading Style Sheets)", generate_exp_04),
    (5, "Prepare SRS for the Project Topic (IEEE 830)", generate_exp_05),
    (6, "Prepare DFD - Data Flow Diagram (Levels 0, 1, 2)", generate_exp_06),
    (7, "Prepare Use Case Diagram and Specifications", generate_exp_07),
    (8, "Interaction Design and Detailed UML Artifacts", generate_exp_08),
    (9, "WBS, Gantt Chart & Test Case Design", generate_exp_09),
    (10, "Prepare Test Case Plan using Pytest or Unittest", generate_exp_10),
    (11, "Prepare RMMM Document", generate_exp_11),
    (12, "Cost Estimation Using the Basic COCOMO Model", generate_exp_12),
    (13, "Version Control and Deployment Using Git & GitHub Pages", generate_exp_13)
]

def build_all():
    print(f"Starting generation of all {len(EXPERIMENTS)} Professional Lab Experiment Documents...")
    print(f"Target Directory: {OUTPUT_DIR}\n")

    for num, name, gen_fn in EXPERIMENTS:
        print(f"[{num:02d}/13] Building Exp {num:02d}: {name}...")
        gen_fn()

    print("\n" + "="*70)
    print("ALL 13 EXPERIMENT DOCUMENTS SUCCESSFULLY CREATED WITH PROFESSIONAL FORMATTING!")
    print(f"Destination: {OUTPUT_DIR}")
    print("="*70)

if __name__ == '__main__':
    build_all()
