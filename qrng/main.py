from qrng import create_qrng_circuit, run_qrng, extract_random_bits, bits_to_numbers
from analysis import run_all_tests
from visualization import plot_distribution, plot_bit_sequence


def main():
    print(".... Quantum Random Number Generator (QRNG) Simulator ....")

    try:
        n_qubits = int(input("Enter number of qubits: "))
        shots = int(input("Enter number of shots: "))
    except ValueError:
        print("Invalid input")
        return

    # Step 1: Create circuit
    qc = create_qrng_circuit(n_qubits)

    print("\nQuantum Circuit:")
    print(qc)

    # Step 2: Run simulation
    counts = run_qrng(qc, shots)

    print("\nMeasurement Results:")
    print(counts)

    # Step 3: Generate random bits
    random_bits = extract_random_bits(counts)

    # Step 4: Convert to numbers
    numbers = bits_to_numbers(random_bits)

    print("\nSample Random Numbers:")
    print(numbers[:10])

    # Step 5: Save to file (IMPORTANT FEATURE)
    with open("random_numbers.txt", "w") as f:
        for num in numbers:
            f.write(str(num) + "\n")

    print("\nRandom numbers saved to random_numbers.txt")

    # Step 6: Analysis
    run_all_tests(random_bits)

    # Step 7: Visualization
    plot_distribution(random_bits)
    plot_bit_sequence(random_bits)


if __name__ == "__main__":
    main()