from qiskit import QuantumCircuit, transpile, assemble
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector
from qiskit_ibm_provider import IBMProvider
import matplotlib.pyplot as plt
import numpy as np


# -------------------------------------------------
# 1. Initializare: superpozitie uniforma pe 3 qubiti (starea initiala)
# -------------------------------------------------
init_circ = QuantumCircuit(3)
init_circ.h([0, 1, 2])
sv_initial = Statevector.from_instruction(init_circ)

print("\nStatevector initial:")
for i, amplitude in enumerate(sv_initial.data):
    print(f"Stare {format(i, '03b')}: {np.round(amplitude, 2)}")

# -------------------------------------------------
# 2. Oracle pentru starea |101⟩ (inversarea fazei pentru numarul cautat(oracle))
# -------------------------------------------------
oracle = QuantumCircuit(3, name='oracle')
oracle.x(1)          # inversam qubitul 1 (deoarece e 0 in tinta noastra)
oracle.h(2)
oracle.ccx(0, 1, 2)
oracle.h(2)
oracle.x(1)          # readucem qubitul 1 la starea initiala

oracle_gate = oracle.to_gate()

print("Oracle (marcheaza starea |101⟩):")
print(oracle.draw())


# -----------------------------------------------------
# 3. Operatorul de difuzie (inversia in jurul mediei) 
# -----------------------------------------------------
diffusion = QuantumCircuit(3, name='diffusion')
diffusion.h([0, 1, 2])
diffusion.x([0, 1, 2])
diffusion.h(2)
diffusion.ccx(0, 1, 2)
diffusion.h(2)
diffusion.x([0, 1, 2])
diffusion.h([0, 1, 2])
diffusion_gate = diffusion.to_gate()

print("\nOperatorul de difuzie:")
print(diffusion.draw())

# --------------------------------------
# 4. Circuitul complet Grover(cresterea progresiva a amplitudinii)
# --------------------------------------
grover = QuantumCircuit(3)
grover.h([0, 1, 2])
grover.append(oracle_gate, [0, 1, 2])
grover.append(diffusion_gate, [0, 1, 2])
grover.measure_all()

print("\nCircuitul complet Grover:")
print(grover.draw())

# -----------------------------------------------------
# 5. Simularea circuitului pe simulator (probabilitati finale)
# -----------------------------------------------------
from qiskit_aer import Aer
simulator = Aer.get_backend('qasm_simulator')
job_sim = simulator.run(transpile(grover, simulator), shots=1024)
result_sim = job_sim.result()
counts_sim = result_sim.get_counts()

print("\nRezultatele masuratorii pe simulator:")
print(counts_sim)
plot_histogram(counts_sim, title="Rezultatul Grover (Simulator)")
plt.show()

# -----------------------------------------------------
# 6. Rularea circuitului pe hardware real IBM Q
# -----------------------------------------------------
provider = IBMProvider()

# Selectam un backend real disponibil (ex: ibmq_manila sau ibm_oslo)
backend = provider.get_backend('ibmq_manila')

# Transpilam circuitul pentru backend-ul ales
transpiled_circuit = transpile(grover, backend=backend, optimization_level=3)

# Ruleazam circuitul pe hardware
job_hw = backend.run(transpiled_circuit, shots=1024)
print("\nJob-ul a fost trimis catre hardware. Asteptam rezultatele...")

# Așteptam rezultatul
result_hw = job_hw.result()
counts_hw = result_hw.get_counts()

print("\nRezultatele masuratorii pe hardware IBM Q:")
print(counts_hw)
plot_histogram(counts_hw, title="Rezultatul Grover (IBM Q Hardware)")
plt.show()
