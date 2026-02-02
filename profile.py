import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Page config
st.set_page_config(
    page_title="Noah Nzeki William",
    page_icon="🧑‍🔬",
    layout="wide",
)

# Custom CSS (text color fix and line-height)
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
        color: #111 !important;
        line-height: 1.25;   /* ensures even spacing */
    }
    .card h4 {
        color: #000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar
with st.sidebar:
    st.image("nnw2.png", width=150)
    st.markdown("### Noah Nzeki William")
    st.write("Theoretical Physics & Quantum Computing")
    st.markdown("---")
    st.markdown("## 📫 Contact")
    st.markdown("📧 noahnzeki@yandex.com")
    st.markdown("## 💻 GitHub")
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
 
    url = "https://assets2.lottiefiles.com/packages/lf20_u4yrau.json"  # Quantum circuit example
    response = requests.get(url)
    lottie_json = response.json()

    st_lottie(
        lottie_json,
        speed=1,
        loop=True,
        quality="high",
        height=100
    )
st.markdown("---")

# About section
# ======================
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

st.markdown("---")

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
        <h4>📊 Data Science (Intrested)</h4>
        Machine learning and scientific data analysis.
        </div>
        """,
        unsafe_allow_html=True,
    )

# Contact
# st.markdown("---")
# st.markdown("## 📫 Contact")
#
# st.write("📧 Email: noahnzeki@yandex.com")
# # st.write("🐙 GitHub: https://github.com/nnw")

st.markdown("---")
st.caption("Built with Streamlit 🚀")

url = "https://assets2.lottiefiles.com/packages/lf20_u4yrau.json"  # Quantum circuit example
response = requests.get(url)
lottie_json = response.json()

st_lottie(
    lottie_json,
    speed=1,
    loop=True,
    quality="high",
    height=400
)


