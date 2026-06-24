import streamlit as st
from modules.ui_components import add_footer

# Config
st.set_page_config(page_title="Dev Hub | Calculator", page_icon="🧮", layout="centered", initial_sidebar_state="collapsed")

# Styling (Minimize redundant calls)
st.markdown("""<style>.block-container { max-width: 500px !important; padding: 1rem !important; } div.stButton > button { width: 100% !important; height: 50px !important; font-size: 18px !important; } .stTextInput > div > div > input { text-align: right !important; font-size: 32px !important; font-weight: bold !important; color: #00ffa3 !important; }</style>""", unsafe_allow_html=True)

st.title("🔢 Standard Calculator")

# State
if "expr" not in st.session_state: st.session_state.expr = ""
if "history" not in st.session_state: st.session_state.history = []

# Core Logic
def on_btn_click(btn):
    if btn == "C":
        st.session_state.expr = ""
    elif btn == "=":
        try:
            res = str(eval(st.session_state.expr))
            st.session_state.history.append(f"{st.session_state.expr} = {res}")
            st.session_state.expr = res
        except:
            st.session_state.expr = "Error"
    else:
        st.session_state.expr += btn

# Input Box
st.text_input("Display", value=st.session_state.expr, label_visibility="collapsed", disabled=True)

# Grid
btn_rows = [["C", "(", ")", "/"], ["7", "8", "9", "*"], ["4", "5", "6", "-"], ["1", "2", "3", "+"], ["0", ".", "="]]

for row in btn_rows:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        cols[i].button(btn, use_container_width=True, on_click=on_btn_click, args=(btn,))

# History
if st.sidebar.button("Clear History"): st.session_state.history = []
for item in reversed(st.session_state.history): st.sidebar.text(item)

add_footer()