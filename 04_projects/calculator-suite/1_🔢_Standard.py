import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Dev Hub | Calculator", page_icon="🧮", layout="centered")

# 2. Modern Styling (CSS)
def apply_style():
    st.markdown("""
        <style>
        .block-container { max-width: 450px !important; }
        div.stButton > button { height: 60px !important; font-size: 20px !important; border-radius: 12px !important; border: 1px solid #444 !important; }
        .stTextInput>div>div>input { font-size: 32px !important; text-align: right !important; font-family: monospace !important; background: #1a1a1a !important; }
        footer {visibility: hidden;} /* Streamlit default footer hide */
        .footer { position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; padding: 10px; background-color: transparent; color: #888; font-size: 12px; }
        </style>
    """, unsafe_allow_html=True)

apply_style()

# 3. Branding Header
st.title("🔢 Smart Calculator")
st.caption("Dev Hub | Ecosystem Mode v1.1")

# 4. Calculator Logic
if "expr" not in st.session_state: st.session_state.expr = ""

user_typed = st.text_input("Input", value=st.session_state.expr, placeholder="0", label_visibility="collapsed")
if user_typed != st.session_state.expr:
    st.session_state.expr = user_typed
    st.rerun()

# Responsive Grid
buttons = [
    ["C", ".", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", "="]
]

for row in buttons:
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        if cols[i].button(btn, use_container_width=True):
            if btn == "C": st.session_state.expr = ""
            elif btn == "=":
                try: st.session_state.expr = str(round(eval(st.session_state.expr), 4))
                except: st.session_state.expr = "Error"
            else: st.session_state.expr += btn
            st.rerun()

# 5. Modern Footer (Branding)
st.markdown("""
    <div class="footer">
        <hr>
        Dev Hub | © 2026 Ecosystem Analytics<br>
        Powered by Zayyan Studio
    </div>
""", unsafe_allow_html=True)