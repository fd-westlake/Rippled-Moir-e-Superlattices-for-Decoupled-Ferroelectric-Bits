# Rippled-Moir-e-Superlattices-for-Decoupled-Ferroelectric-Bits

## Folder Structure

###  database/
Raw data for training and testing.
- **`force_model/`**: Data for the force field model, including `input.json` (input parameters) and `database.zip` (database file).

###  model/
Trained machine learning model files.
- **`BNC_frozen_model_compressed.pb`**: Force field prediction model.

###  DFT/
Files and scripts for first-principles (DFT) calculations.
- **`INCAR_scf`**: Input file for DFT calculations.
- **`INCAR_bec`**:  Input file for BEC calculations.

###  LAMMPS/
Files for LAMMPS molecular dynamics simulations.
- **`01-eq_npt.lammps`**: Script for NPT simulation.
- **`02-eq_nvt.lammps`**: Script for NPT simulation.
- **`03-apply_E.lammps`**: Script for applying electric field.
- **`04-apply_bub.lammps`**: Script for applying bubble.

###  DFT/
Files and scripts for first-principles (DFT) calculations.
- **`INCAR_scf`**: Input file for DFT calculations.
- **`INCAR_bec`**:  Input file for BEC calculations.

###  figure/
High-resolution figures from the manuscript.
