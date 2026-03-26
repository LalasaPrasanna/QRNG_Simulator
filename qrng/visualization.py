import matplotlib.pyplot as plt


def plot_distribution(bits):
    data = ''.join(bits)
    values = [int(b) for b in data]

    plt.figure()
    plt.hist(values, bins=2)
    plt.title("QRNG Bit Distribution")
    plt.xlabel("Bit Value (0 or 1)")
    plt.ylabel("Frequency")
    plt.show()


def plot_bit_sequence(bits, length=50):
    data = ''.join(bits[:length])
    values = [int(b) for b in data]

    plt.figure()
    plt.plot(values)
    plt.title(f"Random Bit Sequence (First {length} bits)")
    plt.xlabel("Index")
    plt.ylabel("Bit")
    plt.show()