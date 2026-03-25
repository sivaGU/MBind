# MBind GUI

MBind is a Streamlit-based interface that wraps AutoDock Vina and AutoDock4 (AD4) so metalloprotein docking runs are easy to configure, execute, and review.

Hosted app: https://g8sfrb59jfx7ohqfzr5fko.streamlit.app/

## Contents
- [Quick Start (Cloud)](#quick-start-cloud)
- [Run Locally](#run-locally)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Key Features](#key-features)
- [Documentation Overview](#documentation-overview)
- [Demo Tab Assets](#demo-tab-assets)
- [Tab-by-Tab Summary](#tab-by-tab-summary)
- [Usage Workflow](#usage-workflow)
- [Supported Formats](#supported-formats)
- [Configuration Files](#configuration-files)
- [Contact](#contact)

## Quick Start (Cloud)
1. Open the hosted Streamlit app.
2. Select the desired navigation tab (Demo, Standard AutoDock, Zn²⁺ Metalloprotein Docking, or Fe²⁺/Mg²⁺/Cu²⁺ Metalloprotein Docking).
3. Follow the on-screen prompts to upload receptors, ligands, and configure grid parameters.
4. Use the *Documentation* tab for a detailed walkthrough of each step.

## Run Locally
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd MetalBind-main
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Launch the app**
   ```bash
   streamlit run MBind.py
   ```
   *Windows:* double-click `run_docking.bat` to launch Streamlit.
4. Visit `http://localhost:8501` in your browser.

## Requirements
- Python 3.7+ (tested with 3.8–3.11)
- Streamlit, pandas (installed via `requirements.txt`)
- Windows-ready executables in `Files_for_GUI/`:
  - `vina.exe`
  - `autogrid4.exe`
  - `autodock4.exe`

*Linux/Mac:* compile or install equivalent binaries (without `.exe` extensions) and drop them inside `Files_for_GUI/` (same names without `.exe`).

## Project Structure
```
MetalBind-main/
├── MBind.py                # Main MBind Streamlit application
├── Files_for_GUI/          # Executables, parameters, sample ligands
│   ├── vina.exe / vina
│   ├── autogrid4.exe / autogrid4
│   ├── autodock4.exe / autodock4
│   ├── zinc_pseudo.py
│   ├── iron_pseudo.py, copper_pseudo.py, magnesium_pseudo.py
│   ├── AD4_parameters.dat, AD4Zn.dat, AD4Fe.dat, AD4Cu.dat, AD4Mg.dat
│   ├── ad4_maps/           # Pre-merged AD4 parameter files (ZnTZ, FeTF, CuTQ, MgTM)
│   └── Ligands/
├── run_docking.bat         # Windows launcher
├── requirements.txt        # Python dependencies
└── README.md               # This document
```

## Key Features
- Unified Vina and AD4 workflows with **Zn²⁺** pseudoatom support and **Fe²⁺ / Cu²⁺ / Mg²⁺** metalloprotein maps (TF / TQ / TM)
- Automatic executable discovery and parameter setup
- Grid box calculators, AD4 map generation, and progress tracking
- Downloads for per-ligand PDBQT/logs, CSV summaries, and ZIP archives
- Dedicated documentation tab mirroring the personalized vaccine pipeline

## Demo Tab Assets
The *Demo* tab is preconfigured for 8 Zinc Metal Proteins. To use it:
1. **Download the demo assets** from the `Zinc Metal Protein Receptors` and `8 Endogenous Ligands` folders in the repository.
2. Place these folders alongside `MBind.py` (locally) or upload their contents to the Streamlit Cloud workspace under the same folder names.
3. In the app, choose from the 8 Zn²⁺ metalloproteins: hACE, HDAC2, HDAC8 with Hydroxamic Acid, HDAC8 with SAHA, HDAC10, Human Neutral Endopeptidase, Leukotriene, or ADAMTS-5. Grid centers, sizes, spacing (0.375 Å), and docking parameters lock automatically.
4. Upload one of the bundled receptors (PDBQT) and select ligands from the endogenous ligand set before running AD4 map building or docking.

Without these folders, the Demo tab cannot find receptors/ligands and will show missing-file warnings.

## Tab-by-Tab Summary
- **Home**: High-level overview and quick tips.
- **Documentation**: Full step-by-step instructions (see above) covering CSV ingestion, module selection, epitope features, VaxiJen workflow, aggregated file processing, and population coverage.
- **Demo**: AD4-only workflow with one-click presets for 8 Zinc Metal Proteins. Requires the demo receptor/ligand folders.
- **Standard AutoDock**: Vina-focused workflow with user-defined grid boxes.
- **Zn²⁺ Metalloprotein Docking**: AD4 workflow with full control over grid/map settings (Zn²⁺-style merged parameters).
- **Fe²⁺/Mg²⁺/Cu²⁺ Metalloprotein Docking**: Same AD4 map + Vina(AD4) flow as Zn²⁺, using bundled `AD4_parameters_plus_FeTF.dat`, `...CuTQ.dat`, or `...MgTM.dat` and the matching pseudo-atom script.

## Usage Workflow
1. **Upload receptor** (PDBQT) via file uploader or path.
2. **Prepare ligands** from a source folder or upload ready-made PDBQT files.
3. **Configure grid box** manually or via preset (Demo) / autodetect (Vina).
4. **Generate AD4 maps** when using the AD4 pipeline.
5. **Run docking**; monitor progress through the status table.
6. **Download results** (per-ligand logs/PDBQT, CSV summary, ZIP bundle).

## Supported Formats
- Receptors: PDBQT only
- Ligands: PDBQT, PDB, MOL2, SDF (converted to PDBQT during preparation)

## Case Studies

- Case Study 1: MBind Metalloprotein and Standard Docking. To demonstrate usability, MBind was tested by a user with no prior command-line experience in molecular docking. The user can perform Zn²⁺ metalloprotein docking by uploading prepared receptor and ligand PDBQT files and executing AutoDock4Zn-based docking entirely through the GUI. No manual parameter file preparation, metal atom typing, or grid map scripting was required, as all preprocessing steps were handled automatically by the platform. The same user could also perform non-metalloprotein docking using AutoDock Vina within the same interface by selecting the standard docking workflow. Grid box definition, docking parameter selection, execution, and output retrieval were all completed through the GUI without switching tools or environments. This case demonstrates MBind’s ability to support both metalloprotein and non-metalloprotein docking workflows within a single interface.

- Case Study 2: MBind Integration of ML docking through the GUI. In a second use case, MBind was used by a user seeking to apply ML based docking methods without command-line interaction. The user selected the GNINA workflow directly from the GUI and executed ML pose and energy prediction using the same prepared ligand and receptor inputs used for standard docking. MBind handled input formatting and output organization automatically to allow the user to obtain ML-based docking results within the same interface. This case demonstrates MBind’s ability to integrate ML docking methods into a unified, accessible workflow.

- Case Study 3: MBind Classroom Use. As a third scenario, MBind was used in a teaching setting to demonstrate metalloprotein docking concepts. Students were able to complete Zn²⁺ docking runs within minutes using the web based interface. This allowed instruction to focus on interpretation of binding poses rather than software setup. This illustrates MBind’s applicability for educational and exploratory applications where traditional command-line workflows may hinder learning due to the unfamiliarity for many individuals.


## Configuration Files
Executables and parameters are auto-detected from `Files_for_GUI/` next to `MBind.py` (falls back to `Working directory/Files_for_GUI` if needed). Ensure permissions are set (`chmod +x` on Linux). Scripts and data:
- `zinc_pseudo.py` — tetrahedral Zn²⁺ pseudoatoms (TZ)
- `iron_pseudo.py`, `copper_pseudo.py`, `magnesium_pseudo.py` — TF, TQ, TM pseudoatoms
- `AD4_parameters.dat` / `AD4Zn.dat` — Zn²⁺ AD4 merge (Demo / general tab)
- `ad4_maps/AD4_parameters_plus_*.dat` — pre-merged maps for ZnTZ, FeTF, CuTQ, MgTM

## Contact
Questions, bug reports, or collaboration requests: **Dr. Sivanesan Dakshanamurthy** — sd233@georgetown.edu
---














