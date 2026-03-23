# Rippled-Moir-e-Superlattices-for-Decoupled-Ferroelectric-Bits

> This repository contains all calculations, data, and model files related to the study of rippled moiré superlattices for decoupled ferroelectric bits, as described in [ arXiv:2510.13568]. It includes first-principles (DFT) calculations, molecular dynamics simulations, and machine learning models.

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
- **`cal_polar/`**: Directory containing tools to split trajectory frames and calculate the total polarization.
  - **`avg_z.py`**: Python script to compute the average polarization across frames.
  - **`input.lammps`**: Input script for LAMMPS to read trajectories and compute local dipoles.
  - **`runscript`**: Job submission script for cluster execution.
- **`strain.py`**: Python script for applying biaxial strain to the structure.
- **`z_range.py`**: Python script for calculating the Z-coordinate range of atoms (maximum minus minimum value).


###  DFT/
Files and scripts for first-principles (DFT) calculations.
- **`INCAR_scf`**: Input file for DFT calculations.
- **`INCAR_bec`**:  Input file for BEC calculations.

###  figure/
High-resolution figures from the manuscript.

## Wiki
We have also made a public wiki that explains how to implement dynamic BEC simulation in LAMMPS：https://liutheorylab.github.io/Tutorial/LAMMPS_DynamicBEC/
