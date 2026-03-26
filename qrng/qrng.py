from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer


def create_qrng_circuit(n_qubits):
    qc = QuantumCircuit(n_qubits, n_qubits)

    # Apply Hadamard (superposition)
    for i in range(n_qubits):
        qc.h(i)

    # Measure
    qc.measure(range(n_qubits), range(n_qubits))

    return qc


def run_qrng(qc, shots=1024):
    simulator = Aer.get_backend('aer_simulator')

    compiled_circuit = transpile(qc, simulator)

    job = simulator.run(compiled_circuit, shots=shots)
    result = job.result()

    return result.get_counts()


def extract_random_bits(counts):
    random_bits = []

    for state, freq in counts.items():
        random_bits.extend([state] * freq)

    return random_bits


def bits_to_numbers(bits):
    return [int(b, 2) for b in bits]