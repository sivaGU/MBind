# MBind GUI

MBind is a Streamlit-based GUI for metalloprotein and standard docking. It integrates AutoDock Vina, AutoGrid4, and AutoDock4 in one workflow, with optional GNINA (or SMINA) ML docking in the same interface.

**Hosted app:** https://mbindgui.streamlit.app/

**Source repository:** https://github.com/sivaGU/MBind

## What this README reflects (Manuscript v19)

- **Zinc** is the primary validated metalloprotein pathway (AutoDock4Zn-style parameterization via `AD4Zn.dat` and related maps).
- **Magnesium, iron, and copper** workflows use extended AD4 parameter files and pseudoatoms in the GUI; they are **preliminary / exploratory** and are not validated to the same extent as zinc (see manuscript §2.5–2.6 and §3.2.4).
- **Benchmark panel:** eight zinc metalloproteins and eight non-metalloprotein targets; comparisons against **eight ML methods** (GNINA, EquiBind, Boltz-2, TankBind, GAABind, StructureNet, GNNSeq, PLAIG) and **five non-ML tools** (SwissDock, CB-Dock2, Webina, 1-ClickDock, MolModa) under a fixed redocking protocol.
- **Reported pose accuracy (manuscript abstract):** mean ligand RMSD **0.49 Å** (metalloprotein set) and **0.62 Å** (non-metalloprotein set), measured with DockRMSD (symmetry-aware) relative to co-crystallized poses; binding trends compared using IC₅₀-derived ΔG values.

### Usability case studies (manuscript §3.2)

1. **Zinc and standard docking:** A novice user completed both Zn²⁺ metalloprotein docking (AutoDock4Zn-style setup handled in-app) and standard Vina docking in the same interface without switching tools or using the command line.
2. **ML docking in the GUI:** GNINA was run from the GUI with the same prepared inputs as classical workflows, with outputs organized in one place.
3. **Teaching:** Students ran zinc docking runs via the web UI in a short lab-style session, focusing on poses rather than toolchain setup.
4. **Preliminary Mg²⁺ / Fe²⁺ / Cu²⁺ parameters:** Prototype force-field extensions were developed and exposed through the same workflow for exploratory docking; these implementations are experimental (manuscript §3.2.4).

## Quick start

1. Open the hosted app or run locally (below).
2. Choose a workflow tab:
   - `MBind Demo`
   - `Standard AutoDock`
   - `Zn²⁺ Metalloprotein Docking`
   - `Fe²⁺/Mg²⁺/Cu²⁺ Metalloprotein Docking`
   - `GNINA ML Docking`
3. Upload receptor and ligand files (see **Supported inputs**).
4. Configure the grid and run docking.
5. Download PDBQT, log, CSV, or ZIP outputs.

## Run locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Launch:
   ```bash
   streamlit run MBind.py
   ```
   On Windows you can also run `run_docking.bat`.
3. Open http://localhost:8501.

## Requirements

- Python 3.8+ (the manuscript reports development with Python 3.12.3).
- Packages listed in `requirements.txt`.
- Docking executables under `Files_for_GUI/`:
  - `vina` (or `vina.exe`)
  - `autogrid4` (or `autogrid4.exe`)
  - `autodock4` (or `autodock4.exe`)
  - `gnina` / `smina` (optional, for local GNINA workflows)

## Supported inputs

- **Receptors:** PDBQT (AD4 workflows); PDB or PDBQT (GNINA workflow)
- **Ligands:** PDBQT, PDB, MOL2, SDF

## Workflow coverage

- **Zn²⁺ Metalloprotein Docking:** AD4/AutoGrid workflow with AutoDock4Zn-style maps.
- **Fe²⁺/Mg²⁺/Cu²⁺ Metalloprotein Docking:** AD4/AutoGrid with metal-specific merged parameter files and pseudoatoms (preliminary).
- **Standard AutoDock:** Classical AutoDock Vina box docking.
- **GNINA ML Docking:** Optional ML-assisted docking/scoring; can be used for metalloprotein or standard targets when executables or backend access are configured.

## Demo assets

- The bundled Demo panel is **zinc-focused** (eight preset receptors). Populate `(DEMO) Zinc Metal Protein Receptors/` and `(DEMO) Ligands/` as described in `SETUP_INSTRUCTIONS.md` so the Demo tab can resolve paths.
- Cu/Fe/Mg projects use the dedicated metalloprotein tabs with your own prepared PDBQT files.

## Project structure

```
MBind-main/
├── MBind.py
├── README.md
├── SETUP_INSTRUCTIONS.md
├── requirements.txt
├── run_docking.bat
└── Files_for_GUI/
    ├── vina, autogrid4, autodock4  (plus .exe on Windows)
    ├── gnina / smina (optional)
    ├── zinc_pseudo.py, iron_pseudo.py, copper_pseudo.py, magnesium_pseudo.py
    ├── AD4_parameters.dat, AD4Zn.dat, AD4Fe.dat, AD4Cu.dat, AD4Mg.dat
    └── ad4_maps/AD4_parameters_plus_*.dat
```

## Notes on validation scope

- The manuscript’s quantitative benchmarking emphasizes the **eight zinc metalloproteins** and **eight non-metalloprotein** targets; Mg/Fe/Cu case docking in §2.6 is illustrative parameter testing rather than the main benchmark table.
- GNINA is integrated as an optional ML pathway alongside classical AutoDock tools.

## Contact

Questions or collaboration: **Dr. Sivanesan Dakshanamurthy** — sd233@georgetown.edu
