"""
Utility functions for loading GPCR receptor data and metadata.
"""
from pathlib import Path
import json
import pandas as pd
import os


def _resolve_data_dir() -> Path:
    """Resolve the directory that contains all receptor folders."""
    env_path = os.getenv("GPCR_DATA_DIR")
    if env_path:
        candidate = Path(env_path).expanduser()
        if candidate.exists():
            return candidate

    app_root = Path(__file__).resolve().parent

    # Prefer a dedicated "GPCR Structures" subfolder if present
    preferred = app_root / "GPCR Structures"
    if preferred.exists():
        return preferred

    # Some deployments keep receptor folders directly beside the app files
    # Detect this by checking for subdirectories that match the receptor naming pattern
    has_receptor_dirs = any(
        path.is_dir() and len(path.name) == 4 and path.name[0].isdigit()
        for path in app_root.iterdir()
    )
    if has_receptor_dirs:
        return app_root

    # As a final fallback, allow using a sibling "GPCR Structures" directory one level up
    parent_preferred = app_root.parent / "GPCR Structures"
    if parent_preferred.exists():
        return parent_preferred

    return app_root


DATA_DIR = _resolve_data_dir()

def collect_receptors():
    """
    Collect all receptor folders and their associated files.
    Returns a dictionary keyed by receptor folder name with paths & metadata.
    """
    receptors = {}
    
    if not DATA_DIR.exists():
        print(f"Warning: Data directory not found: {DATA_DIR}")
        return receptors
    
    for folder in DATA_DIR.iterdir():
        if folder.is_dir():
            receptor_id = folder.name
            
            # Find all relevant files in the folder
            files = {
                "folder_path": folder,
                "pdb_receptor": None,
                "pdb_ligand": None,
                "pocket_csv": None,
                "pocket_cons_csv": None,
                "pocket_json": None,
                "cons_json": None,
                "feature_vector_csv": None,
                "pocket_analysis_png": None
            }
            
            # Search for files with the receptor ID prefix
            for file_path in folder.glob(f"{receptor_id}_*"):
                filename = file_path.name
                
                if filename.endswith("_receptor_only.pdb"):
                    files["pdb_receptor"] = file_path
                elif filename.endswith("_ligand_only.pdb"):
                    files["pdb_ligand"] = file_path
                elif filename.endswith("_pocket_residues.csv") and not filename.endswith("_with_conservation.csv"):
                    files["pocket_csv"] = file_path
                elif filename.endswith("_pocket_residues_with_conservation.csv"):
                    files["pocket_cons_csv"] = file_path
                elif filename.endswith("_pocket_analysis.json"):
                    files["pocket_json"] = file_path
                elif filename.endswith("_conservation_summary.json"):
                    files["cons_json"] = file_path
                elif filename.endswith("_pocket_feature_vector.csv"):
                    files["feature_vector_csv"] = file_path
                elif filename.endswith("_pocket_analysis.png"):
                    files["pocket_analysis_png"] = file_path
            
            # Only include receptors that have at least some analysis files
            if any([files["pocket_csv"], files["pocket_cons_csv"], files["pocket_json"]]):
                receptors[receptor_id] = files
    
    print(f"Found {len(receptors)} receptors with analysis data")
    return receptors

def load_pocket_data(receptor_files):
    """
    Load pocket residue data for a receptor.
    """
    if receptor_files["pocket_cons_csv"] and receptor_files["pocket_cons_csv"].exists():
        return pd.read_csv(receptor_files["pocket_cons_csv"])
    elif receptor_files["pocket_csv"] and receptor_files["pocket_csv"].exists():
        return pd.read_csv(receptor_files["pocket_csv"])
    else:
        return None

def load_pocket_analysis(receptor_files):
    """
    Load pocket analysis JSON for a receptor.
    """
    if receptor_files["pocket_json"] and receptor_files["pocket_json"].exists():
        with open(receptor_files["pocket_json"], 'r') as f:
            return json.load(f)
    else:
        return None

def load_conservation_summary(receptor_files):
    """
    Load conservation summary JSON for a receptor.
    """
    if receptor_files["cons_json"] and receptor_files["cons_json"].exists():
        with open(receptor_files["cons_json"], 'r') as f:
            return json.load(f)
    else:
        return None

def load_feature_vector(receptor_files):
    """
    Load pocket feature vector CSV for a receptor.
    """
    if receptor_files["feature_vector_csv"] and receptor_files["feature_vector_csv"].exists():
        return pd.read_csv(receptor_files["feature_vector_csv"])
    else:
        return None

def get_receptor_summary_stats(receptor_id, receptor_files):
    """
    Get a summary of key statistics for a receptor.
    """
    summary = {
        "receptor_id": receptor_id,
        "has_receptor_pdb": receptor_files["pdb_receptor"] is not None,
        "has_ligand_pdb": receptor_files["pdb_ligand"] is not None,
        "has_pocket_data": receptor_files["pocket_csv"] is not None,
        "has_conservation_data": receptor_files["pocket_cons_csv"] is not None,
        "has_analysis": receptor_files["pocket_json"] is not None,
        "has_feature_vector": receptor_files["feature_vector_csv"] is not None,
        "pocket_residue_count": 0,
        "conservation_score": 0,
        "hydrophobic_pct": 0,
        "polar_pct": 0
    }
    
    # Load pocket data if available
    pocket_data = load_pocket_data(receptor_files)
    if pocket_data is not None:
        summary["pocket_residue_count"] = len(pocket_data)
    
    # Load analysis data if available
    analysis = load_pocket_analysis(receptor_files)
    if analysis:
        comp_pct = analysis.get("composition_by_type_pct", {})
        summary["hydrophobic_pct"] = comp_pct.get("hydrophobic", 0)
        summary["polar_pct"] = comp_pct.get("polar", 0)
    
    # Load conservation data if available
    conservation = load_conservation_summary(receptor_files)
    if conservation:
        summary["conservation_score"] = conservation.get("average_conservation_score", 0)
    
    return summary 
