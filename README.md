# Gravitational Lensing Simulations: Mass Distributions & Einstein Rings

## Project Overview
This repository contains three numerical Python simulations modeling strong gravitational lensing. By solving the lens equation across high-resolution 2D coordinate grids, these scripts demonstrate how theoretical physics concepts, specifically varying source galaxy morphologies and complex dark matter mass distributions, translate into observable optical distortions like Einstein rings and arcs. 

This project serves as a practical demonstration of efficient, vectorized data processing and spatial mapping techniques.

## Required Dependencies
*   **NumPy:** Core library for vectorized matrix operations, n-dimensional array manipulation, and deflection vector mathematics.
*   **SciPy (`ndimage.map_coordinates`):** Utilized for fast coordinate mapping and interpolation during the ray-tracing phase.
*   **Matplotlib:** Used for generating high-contrast, publication-quality visualizations of the scalar fields.

## Included Simulations

### 1. Ideal Spherical Distribution
*   **The Physics:** The baseline theoretical model. Simulates a perfectly spherical background source deflected by a single, massive foreground lens.
*   **The Output:** Generates a mathematically ideal, symmetrical Einstein ring as seen below.
<img width="1800" height="800" alt="Spherical" src="https://github.com/user-attachments/assets/66823d16-d4a9-4a0d-8ee7-9ba408033e20" />

### 2. Elliptical Source Morphology
*   **The Physics:** Introduces structural realism by adding an ellipticity parameter ($q$) to the background source galaxy's Gaussian profile. 
*   **The Output:** Demonstrates how elliptical mass distribution of the source galaxy results in elliptical arcs and 'stretched' rings rather than the uniform rings of the previous, as seen below.
<img width="1800" height="800" alt="Elliptical" src="https://github.com/user-attachments/assets/98fd18c0-9020-47ee-8963-1f1951f7ef01" />

### 3. Dark Matter Substructures
*   **The Physics:** Models a highly complex, "clumpy" mass distribution. The foreground lens field consists of a primary massive galaxy ($R_E = 65$) alongside multiple localized dark matter sub-halos and satellite clumps.
*   **The Output:** Conveys how 'clumpy' mass distributions break uniform arcs of the resulting Einstein Rings into fragmented, asymmetric spatial anomalies.
<img width="1800" height="800" alt="SubstructureAndDarkMatterClumps" src="https://github.com/user-attachments/assets/5181b907-1d47-4835-8384-719a5358d01e" />


## Methodology
Each simulation follows a structured, computationally efficient ray-tracing pipeline:
1.  **Source Generation:** Modeling the background galaxy using exponential intensity profiles on a 2D source plane.
2.  **Deflection Field Calculation:** Calculating the spatial deflection angle $\vec{\alpha}$ at every pixel based on the gravitational pull of localized masses.
3.  **Ray-Tracing:** Applying the standard lens equation ($\vec{\beta} = \vec{\theta} - \vec{\alpha}$) to map the observed image coordinates back to the non-lensed source plane.

## Local Execution
To replicate this environment and run the simulations locally:

1. Clone this repository to your local computer.
2. Install the required scientific dependencies:
   ```bash
   pip install numpy scipy matplotlib
3. Execute the desired script:
`test-spherical.py`, `test-elliptical.py`, or `test-clumpy.py`
