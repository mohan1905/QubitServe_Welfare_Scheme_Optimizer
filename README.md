# QubitServe Welfare Scheme Optimizer

## Quantum-Assisted Welfare Scheme Allocation Optimizer using QAOA and Qiskit

### Project Overview

This project formulates welfare scheme allocation as a combinatorial optimization problem and explores a quantum-assisted approach using the Quantum Approximate Optimization Algorithm (QAOA).

The problem is modeled as a Quadratic Unconstrained Binary Optimization (QUBO) problem. The model considers beneficiary priorities, scheme benefits, eligibility constraints, and scheme capacity constraints.

### Proposed Approach

1. Define beneficiaries, welfare schemes, priorities, benefits, eligibility, and capacities.
2. Formulate the allocation problem as a QUBO.
3. Convert the QUBO into an Ising Hamiltonian.
4. Construct a QAOA circuit using Qiskit.
5. Optimize the QAOA parameters using a classical optimizer.
6. Simulate the quantum circuit using a statevector simulator.
7. Select the highest-probability feasible allocation.
8. Compare the result with a classical baseline.

### Technologies Used

- Python
- Qiskit
- NumPy
- SciPy
- QAOA
- QUBO
- Quantum simulation

### Project Status

This is a small-scale proof-of-concept using synthetic data and quantum simulation.

The current implementation does not claim quantum advantage or execution on quantum hardware.

### Team

**Team:** QubitServe

**Members:**
- K. Mohan Chandra
- I. Geethika Nandini

**Institution:** Rajamahendri Institute of Engineering and Technology, Rajahmundry

**Event:** Qiskit Fall Fest 2026 – Nuzvid

**Track:** Quantum Optimization
