# MBind GUI

MBind is a Streamlit-based GUI for metalloprotein and standard docking that integrates AutoDock Vina, AutoGrid4, AutoDock4, and optional GNINA-based ML docking in one interface.

Hosted app: https://mbindgui.streamlit.app/

## What This Version Reflects (Manuscript v18)
- Unified workflow for metalloprotein docking (Zn, Cu, Fe, Mg) and non-metalloprotein docking.
- Optional GNINA ML docking inside the same GUI for pose scoring/refinement workflows.
- Benchmark framing from the updated manuscript:
  - 8 metalloproteins and 8 non-metalloproteins.
  - Comparison against 8 ML methods (GNINA, EquiBind, Boltz-2, TankBind, GAABind, StructureNet, GNNSeq, PLAIG).
  - Comparison against 5 non-ML docking tools (SwissDock, CB-Dock2, Webina, 1-ClickDock, MolModa).
- Reported benchmark snapshot from manuscript abstract:
  - Mean RMSD: 0.49 A (metalloproteins), 0.62 A (non-metalloproteins).

## Quick Start
1. Open the hosted app or run locally with Streamlit.
2. Select a workflow tab:
   - `Demo`
   - `Standard AutoDock`
   - `Zn²⁺ Metalloprotein Docking`
   - `Fe²⁺/Mg²⁺/Cu²⁺ Metalloprotein Docking`
   - `GNINA ML Docking`
3. Upload receptor and ligand files.
4. Configure grid parameters and run docking.
5. Export PDBQT/log/CSV/ZIP outputs.

## Run Locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Launch:
   ```bash
   streamlit run MBind.py
   ```
   Windows users can also run `run_docking.bat`.
3. Open `http://localhost:8501`.

## Requirements
- Python 3.8+ recommended.
- Dependencies from `requirements.txt`.
- Docking executables in `Files_for_GUI/`:
  - `vina(.exe)`
  - `autogrid4(.exe)`
  - `autodock4(.exe)`
  - `gnina(.exe)` or `smina(.exe)` for local GNINA workflows (optional)

## Supported Inputs
- Receptors: PDBQT (AD4 workflows), PDB/PDBQT (GNINA workflow)
- Ligands: PDBQT, PDB, MOL2, SDF

## Workflow Coverage
- **Zn²⁺ Metalloprotein Docking tab**: AD4/AutoGrid workflow for Zn metalloproteins.
- **Fe²⁺/Mg²⁺/Cu²⁺ Metalloprotein Docking tab**: AD4/AutoGrid workflow for Fe, Mg, or Cu metalloproteins.
- **Standard AutoDock tab**: classical Vina workflow for standard docking.
- **GNINA ML Docking tab**: optional ML-assisted docking/scoring workflow that can be used for metalloprotein and standard targets.

## Demo Assets
- The bundled demo receptor panel is currently Zn-focused.
- You can still run Cu/Fe/Mg metalloprotein projects by uploading your own receptor/ligand files in the corresponding metalloprotein tabs (and GNINA tab when desired).

## Project Structure
```
New GUi/
├── MBind.py
├── README.md
├── SETUP_INSTRUCTIONS.md
├── requirements.txt
├── run_docking.bat
└── Files_for_GUI/
    ├── vina(.exe), autogrid4(.exe), autodock4(.exe)
    ├── gnina(.exe) / smina(.exe)  # optional
    ├── zinc_pseudo.py, iron_pseudo.py, copper_pseudo.py, magnesium_pseudo.py
    ├── AD4_parameters.dat, AD4Zn.dat, AD4Fe.dat, AD4Cu.dat, AD4Mg.dat
    └── ad4_maps/AD4_parameters_plus_*.dat
```

## Notes on Validation Scope
- The manuscript reports the most extensive benchmarking on Zn metalloproteins.
- Cu/Fe/Mg metalloprotein workflows are included in the GUI and documented as available metalloprotein pathways.
- GNINA is integrated as an optional ML workflow within the same interface.

## Contact
Questions, issues, or collaboration requests: **Dr. Sivanesan Dakshanamurthy** — sd233@georgetown.edu














