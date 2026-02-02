# import streamlit as st
#
# st.title("Noah Nzeki William - Researcher Profile")
# st.header("About Me")
# st.write("Hi, I'm William. I do research in Theoretical Physics and Quantum Computing.")
#
# st.header("Research Interests")
# st.write("- Theoretical and Computational Physics\n- Quantum Computing\n- Data Science")
#
# st.header("Contact")
# st.write("Email: noahnzeki@yandex.com")
# st.write("GitHub: [Noah William](https://github.com/nnw)")


import streamlit as st

# Page config
st.set_page_config(
    page_title="Noah Nzeki William",
    page_icon="🧑‍🔬",
    layout="wide",
)

# Custom CSS (ONLY FIX ADDED: text color inside .card)
st.markdown(
    """
    <style>
    .big-font {
        font-size:40px !important;
        font-weight:700;
    }
    .sub-font {
        font-size:18px !important;
        color: #666;
    }
    .card {
        padding: 1.2rem;
        border-radius: 12px;
        background-color: #f5f5f5;
        margin-bottom: 1rem;
        color: #111 !important;   /* <-- FIX */
    }
    .card h4 {
        color: #000 !important;  /* <-- FIX */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar
with st.sidebar:
    st.image("nnw2.png", width=200)
    st.markdown("### Noah Nzeki William")
    st.write("Theoretical Physics & Quantum Computing")
    st.markdown("---")
    st.markdown("📧 noahnzeki@yandex.com")
    st.markdown("🐙 [GitHub](https://github.com/nnw)")

# Main layout
col1, col2 = st.columns([1, 2])

with col1:
    st.image("nnw2.png", use_container_width=True)

with col2:
    st.markdown('<p class="big-font">Noah Nzeki William</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-font">Researcher in Theoretical Physics & Quantum Computing</p>',
        unsafe_allow_html=True,
    )

    st.write(
        """
        Hi, I'm William. I work at the intersection of **theoretical physics,
        quantum computing**, and **data science**, with a focus on building
        computational tools for modern research.
        """
    )

st.markdown("---")

# About section
st.markdown("## 🧠 About Me")
st.markdown(
    """
    <div class="card">
    Passionate about mathematical modeling, quantum algorithms, and applying
    data-driven techniques to physical systems.
    </div>
    """,
    unsafe_allow_html=True,
)

# Research Interests
st.markdown("## 🔬 Research Interests")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div class="card">
        <h4>🧮 Theoretical Physics</h4>
        Mathematical modeling, simulations, and fundamental theory.
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div class="card">
        <h4>⚛️ Quantum Computing</h4>
        Quantum algorithms, circuits, and computation.
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        """
        <div class="card">
        <h4>📊 Data Science</h4>
        Machine learning and scientific data analysis.
        </div>
        """,
        unsafe_allow_html=True,
    )

# Contact
st.markdown("---")
st.markdown("## 📫 Contact")

st.write("📧 Email: noahnzeki@yandex.com")
st.write("🐙 GitHub: https://github.com/nnw")

st.markdown("---")
st.caption("Built with Streamlit 🚀")

