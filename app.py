# app.py
import streamlit as st

st.set_page_config(page_title="AdaptInfer Dashboard", layout="wide")
st.title("🧠 AdaptInfer: Hardware-Aware Adaptive Inference Engine")

# Setup the mode tabs
mode = st.sidebar.radio("Select View Mode", ["Simple Mode", "Expert Mode"])

if mode == "Simple Mode":
    st.header("Simple Generation Interface")
    prompt = st.text_input("Enter your prompt:")
    if st.button("Generate"):
        st.write("Inference pipeline will trigger here...")
        
else:
    st.header("Expert Optimization Panel")
    st.write("Hardware graphs and precision metrics will display here.")