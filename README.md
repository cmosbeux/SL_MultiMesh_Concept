# Mesh Concept and Source Explanation

## Overview
This project explores the concept of particle advection and damage modeling using high and low-resolution meshes. The main idea is to understand how damage evolves over time under the influence of a velocity field and a source term with levels of mesh. There is two simple examples, a simple advection of a step function `2_Mesh_Concept.py` and an advection of damage based on a simple source term `2_Mesh_Source.py`.

## Principle of the method

### Limitation:
The velocity field remains the same across both high and low-resolution meshes, and the pathing does not improve with higher resolution. This reproduces the effect of solving for velocities with Stokes solver in Elmer on the low resolution mesh and then interpolating the result on the higher resolution mesh.

Similarly, the stress is only calculated at low resolution (based on the solution of the Stokes solver) it is then interpolated to the higher resolution.


### Detail of the method (and advantages)

Particle advection involves two main components:

1. **Advection of Existing Damage**: At the end of a timestep, the existing damage can be saved on the high-resolution mesh (e.g. damage at the end of the previous timestep). Back-trackingat the next timestep benefits from the higher resolution, using more particles to interpolate the same shape. This is similar to the effect of a higher resolution mesh when advecting any shape (e.g the discs or donut in our simulation with Elmer)

2. **Source Term**: This term is a function of stress and damage. The stress is defined at a low resolution (from Stokes solution) and re-interpolated to a higher resolution without improving accuracy. The damage (from previous timestep), however, is defined at a higher resolution. If the source term depends on the damage then there is an increased accuracy.

### Conservation Issues
There might be conservation issues since the calculated stress is also a function of damage, which is re-interpolated from the high resolution to the low resolution.

## Python Scripts
The provided Python scripts (`2_Mesh_Concept.py` and `2_Mesh_Source.py`) demonstrate these concepts. The scripts simulate the advection of damage fields and the application of a source term over time.

### `2_Mesh_Concept.py`
This script focuses on the concept of using high and low-resolution meshes for damage advection. It initializes damage fields, advects them over time, and plots the results.

### `2_Mesh_Source.py`
This script extends the concept by including a source term that depends on stress and damage. It demonstrates how the source term and damage advection interact over time.

## GitHub Repository
For a better understanding, you can run the provided Python scripts available in the GitHub repository: [SL_MultiMesh_Concept](https://github.com/cmosbeux/SL_MultiMesh_Concept). The repository includes examples of carrying existing damage with back and forth interpolations between two meshes and a simple source term case.

Feel free to explore the repository and run the scripts to see the concepts in action.