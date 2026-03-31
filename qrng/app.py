import streamlit as st
import matplotlib.pyplot as plt

from qrng import create_qrng_circuit, run_qrng, extract_random_bits, bits_to_numbers

# Page config
st.set_page_config(page_title="QRNG Simulator", page_icon="🔐", layout="wide")

# Title
st.title("🔐 Quantum Random Number Generator (QRNG)")
st.markdown("Generate **true random numbers** using quantum simulation.")

# Sidebar
st.sidebar.header("⚙️ Settings")
n_qubits = st.sidebar.slider("Number of Qubits", 1, 8, 4)
shots = st.sidebar.slider("Number of Shots", 100, 5000, 1000)

# Button
if st.sidebar.button("🚀 Generate Random Numbers"):

    # Create circuit
    qc = create_qrng_circuit(n_qubits)

    # Layout: Circuit + Results side by side
    col1, col2 = st.columns([1, 2])

    # 🔹 Circuit (SMALL SIZE FIXED)
    with col1:
        st.subheader("⚛️ Quantum Circuit")
        try:
            fig = qc.draw(output='mpl')
            fig.set_size_inches(6, 2)  # 👈 FIXED SIZE
            st.pyplot(fig, use_container_width=False)
        except:
            st.warning("⚠️ Install 'pylatexenc' for better visualization")
            st.text(qc)

    # Run simulation
    counts = run_qrng(qc, shots)

    # Extract bits & numbers
    random_bits = extract_random_bits(counts)
    numbers = bits_to_numbers(random_bits)

    # 🔹 Results
    with col2:
        st.subheader("📊 Measurement Results")
        st.write(counts)

        st.subheader("🎲 Sample Random Numbers")
        st.write(numbers[:20])

    # 🔹 Graph
    st.subheader("📈 Bit Distribution")

    data = ''.join(random_bits)
    values = [int(b) for b in data]

    fig2, ax = plt.subplots()
    ax.hist(values, bins=2)
    ax.set_title("Distribution of 0s and 1s")

    st.pyplot(fig2)

    # 🔹 Download
    st.subheader("💾 Download Output")

    file_data = "\n".join(map(str, numbers))
    st.download_button(
        label="⬇️ Download Random Numbers",
        data=file_data,
        file_name="random_numbers.txt",
        mime="text/plain"
    )

    st.success("✅ Random numbers generated successfully!")