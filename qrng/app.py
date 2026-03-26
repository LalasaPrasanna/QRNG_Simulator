import streamlit as st
from qrng import create_qrng_circuit, run_qrng, extract_random_bits, bits_to_numbers
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="QRNG Simulator", page_icon="🔐", layout="wide")

# Title
st.title("🔐 Quantum Random Number Generator (QRNG)")
st.markdown("Generate **true random numbers** using quantum simulation.")

# Sidebar (better UI)
st.sidebar.header("⚙️ Settings")
n_qubits = st.sidebar.slider("Number of Qubits", 1, 8, 4)
shots = st.sidebar.slider("Number of Shots", 100, 5000, 1000)

# Button
if st.sidebar.button("🚀 Generate"):

    st.subheader("⚛️ Quantum Circuit")
    qc = create_qrng_circuit(n_qubits)
    st.text(qc)

    # Run QRNG
    counts = run_qrng(qc, shots)

    # Layout in columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Measurement Results")
        st.write(counts)

    # Generate bits & numbers
    random_bits = extract_random_bits(counts)
    numbers = bits_to_numbers(random_bits)

    with col2:
        st.subheader("🎲 Random Numbers (Sample)")
        st.write(numbers[:20])

    # Histogram
    st.subheader("📈 Distribution")

    data = ''.join(random_bits)
    values = [int(b) for b in data]

    fig, ax = plt.subplots()
    ax.hist(values, bins=2)
    ax.set_title("Bit Distribution (0 vs 1)")

    st.pyplot(fig)

    # Download button
    st.subheader("💾 Download Data")

    file_data = "\n".join(map(str, numbers))
    st.download_button(
        label="⬇️ Download Random Numbers",
        data=file_data,
        file_name="random_numbers.txt",
        mime="text/plain"
    )

    st.success("✅ Random numbers generated successfully!")