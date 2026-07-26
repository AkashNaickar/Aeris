import time
from pathlib import Path
import streamlit as st
from streamlit_folium import st_folium

from aeris.config import settings
from aeris.pipeline.orchestrator import run_pipeline, format_result
from aeris.geo.heatmap import build_heatmap
from aeris.alerts.vernacular import generate_alert

st.set_page_config(page_title="Aeris", layout="wide")
st.title("🌾 Aeris — Field Health Dashboard")

if "results" not in st.session_state:
    st.session_state.results = []
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

with st.sidebar:
    st.header("Controls")
    uploaded_file = st.file_uploader("Upload drone image", type=["jpg", "jpeg", "png"])
    if uploaded_file and st.button("Run Pipeline"):
        tmp = Path("data/ingested") / uploaded_file.name
        tmp.parent.mkdir(parents=True, exist_ok=True)
        tmp.write_bytes(uploaded_file.getvalue())
        with st.spinner("Running 3-stage pipeline..."):
            result = run_pipeline(tmp)
            st.session_state.results.append(result)
        st.success("Pipeline complete!")
        st.text(format_result(result))

    if st.button("Clear All"):
        st.session_state.results = []

    st.divider()
    lang = st.selectbox("Alert Language", ["hindi", "english"], index=0)
    st.session_state.lang = lang

col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("Field Health Map")
    if st.session_state.results:
        m = build_heatmap(st.session_state.results)
        st_folium(m, width=700, height=500)
    else:
        st.info("No data yet. Upload an image to begin.")

with col2:
    st.subheader("Latest Diagnosis")
    if st.session_state.results:
        latest = st.session_state.results[-1]
        s1 = latest["stage1"]
        s2 = latest["stage2"]
        s3 = latest["stage3"]

        stress_icon = "🔴" if s1["stressed"] else "🟢"
        st.metric("Stress Detected", f"{stress_icon} {'Yes' if s1['stressed'] else 'No'}")
        st.metric("Disease", s2["disease"])
        st.metric("Confidence", f"{s2['confidence']:.1%}")
        st.metric("Risk Level", s3["risk_level"])
        st.metric("Risk Score", f"{s3['risk_score']:.2f}")

        st.subheader("Alert")
        alert = generate_alert(
            s3["risk_level"], s2["disease"],
            language=st.session_state.get("lang", "hindi"),
        )
        st.info(alert)

        if latest.get("gps"):
            st.caption(f"Location: {latest['gps'][0]:.6f}, {latest['gps'][1]:.6f}")
    else:
        st.info("Awaiting first capture...")
