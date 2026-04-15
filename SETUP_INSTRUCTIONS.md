# MBind Setup Instructions

## Overview
MBind is a Streamlit-based GUI for AutoDock Vina, AutoGrid4, AutoDock4, and optional GNINA workflows. It supports metalloprotein docking across Zn²⁺, Cu²⁺, Fe²⁺, and Mg²⁺ targets, plus standard docking.

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup Demo Files (Optional)
For the Demo tab to work, you need to populate two folders:

- **`(DEMO) Zinc Metal Protein Receptors/`**: Place 8 receptor PDBQT files (bundled demo panel):
  - hACE.pdbqt
  - HDAC2.pdbqt
  - HDAC8_with_Hydroxamic_Acid.pdbqt
  - HDAC8_with_SAHA.pdbqt
  - HDAC10.pdbqt
  - Human_Neutral_Endopeptidase.pdbqt
  - Leukotriene.pdbqt
  - ADAMTS-5.pdbqt

- **`(DEMO) Ligands/`**: Place 8 endogenous ligand PDBQT files corresponding to each receptor.

### 3. Run the Application

**Windows:**
Double-click `run_docking.bat` or run:
```bash
streamlit run MBind.py
```

**Linux/Mac:**
```bash
streamlit run MBind.py
```

The application will open in your browser at `http://localhost:8501`

## Project Structure

```
MBind/
├── MBind.py                        # Main MBind Streamlit application
├── README.md                       # Full documentation
├── requirements.txt                # Python dependencies
├── run_docking.bat                 # Windows launcher script
├── setup_executables.py            # Executable setup script
├── .gitignore                      # Git ignore file
├── Files_for_GUI/                  # Executables and parameters
│   ├── vina                        # AutoDock Vina executable
│   ├── autogrid4                   # AutoGrid4 executable
│   ├── autodock4                   # AutoDock4 executable
│   ├── AD4_parameters.dat          # AD4 parameters
│   ├── AD4Zn.dat                   # AD4 extra block (merge for Zn²⁺/TZ)
│   ├── AD4Fe.dat, AD4Cu.dat, AD4Mg.dat  # Extra blocks for Fe/Cu/Mg
│   ├── ad4_maps/                   # Pre-merged: ZnTZ, FeTF, CuTQ, MgTM
│   ├── zinc_pseudo.py              # Zn²⁺ pseudoatom (TZ)
│   ├── iron_pseudo.py, copper_pseudo.py, magnesium_pseudo.py  # TF, TQ, TM
│   └── Ligands/                    # Sample ligands
├── (DEMO) Zinc Metal Protein Receptors/  # Demo receptors (populate with 8 PDBQT files)
└── (DEMO) Ligands/                 # Demo ligands (populate with 8 PDBQT files)
```

## Features

- **Demo Tab**: Pre-configured Zn-focused benchmark panel with locked grid box parameters
- **Standard AutoDock Tab**: Vina-focused workflow with user-defined grid boxes
- **Zn²⁺ Metalloprotein Docking tab**: AD4 workflow with full control over Zn map settings
- **Fe²⁺/Mg²⁺/Cu²⁺ Metalloprotein Docking tab**: AD4 maps for Fe²⁺, Mg²⁺, or Cu²⁺ using bundled pseudo scripts and merged `.dat` files
- **GNINA ML Docking tab**: Optional ML-assisted docking workflow for metalloprotein and standard targets

## Notes

- The Demo tab requires the demo receptor and ligand folders to be populated
- Grid box coordinates are automatically set when selecting a demo receptor in the Demo tab
- The demo receptor set is Zn-focused, while Cu/Fe/Mg runs use the dedicated metalloprotein tabs with user-provided receptors
- All executables are included in `Files_for_GUI/` for Windows (Linux/Mac users need to compile or install equivalent binaries)

## Contact

Questions or issues: See README.md for contact information.
