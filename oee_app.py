import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="OEE Calculator", page_icon="🏭")

st.title("🏭 OEE Calculator")
st.subheader("Overall Equipment Effectiveness")

st.write("Enter your machine performance data below:")

availability = st.slider("Availability %", 0, 100, 90)
performance = st.slider("Performance %", 0, 100, 95)
quality = st.slider("Quality %", 0, 100, 99)

oee = (availability * performance * quality) / 10000

st.markdown("---")
st.metric("Your OEE Score", f"{oee:.1f}%")

if oee >= 85:
    st.success("🌟 World Class OEE! Excellent performance!")
elif oee >= 60:
    st.warning("⚠️ Average OEE. Room for improvement.")
else:
    st.error("🚨 Below Average. Immediate action needed!")

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=oee,
    title={'text': "OEE Score"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "#1D9E75"},
        'steps': [
            {'range': [0, 60], 'color': "#FAECE7"},
            {'range': [60, 85], 'color': "#FAEEDA"},
            {'range': [85, 100], 'color': "#E1F5EE"}
        ],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 85
        }
    }
))

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("What does this mean?")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Availability", f"{availability}%")
with col2:
    st.metric("Performance", f"{performance}%")
with col3:
    st.metric("Quality", f"{quality}%")

st.info("World Class OEE benchmark is 85% or above")