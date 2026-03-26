from scipy.stats import entropy


def frequency_test(bits):
    data = ''.join(bits)

    zeros = data.count('0')
    ones = data.count('1')

    print("\n--- Frequency Test ---")
    print("Total bits:", len(data))
    print("Zeros:", zeros)
    print("Ones :", ones)


def entropy_test(bits):
    data = ''.join(bits)

    p0 = data.count('0') / len(data)
    p1 = data.count('1') / len(data)

    ent = entropy([p0, p1], base=2)

    print("\n--- Entropy Test ---")
    print("Entropy:", ent)


def mean_test(bits):
    data = ''.join(bits)

    values = [int(b) for b in data]
    mean = sum(values) / len(values)

    print("\n--- Mean Test ---")
    print("Mean:", mean)


def run_all_tests(bits):
    frequency_test(bits)
    entropy_test(bits)
    mean_test(bits)