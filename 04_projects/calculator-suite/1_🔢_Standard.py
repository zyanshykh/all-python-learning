import streamlit as st
from modules.ui_components import add_footer

# 1. Config
st.set_page_config(page_title="Dev Hub | Calculator", page_icon="🧮", layout="centered", initial_sidebar_state="collapsed")

# 2. Styling
st.markdown("""
    <style>
    .block-container { max-width: 500px !important; padding: 1rem !important; }
    div.stButton > button { width: 100% !important; height: 50px !important; margin: 2px !important; }
    .stTextInput > div > div > input { text-align: right !important; font-size: 28px !important; font-weight: bold !important; }
    </style>
""", unsafe_allow_html=True)

st.title("🔢 Standard Calculator")

# 3. State Management
if "expr" not in st.session_state: st.session_state.expr = ""
if "history" not in st.session_state: st.session_state.history = []

# 4. Callback Functions (Yeh buttons ko functional banayega)
def update_expr(val):
    if val == "C":
        st.session_state.expr = ""
    elif val == "=":
        try:
            result = str(eval(st.session_state.expr))
            st.session_state.history.append(f"{st.session_state.expr} = {result}")
            st.session_state.expr = result
        except:
            st.session_state.expr = "Error"
    else:
        st.session_state.expr += str(val)

# 5. UI Display
# Input ko 'key' ke zariye control kar rahe hain
st.text_input("Input", value=st.session_state.expr, label_visibility="collapsed", disabled=True)

# 6. Grid Generation
btn_rows = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

for row in btn_rows:
    cols = st.columns(len(row))
    for i, label in enumerate(row):
        # Callback ka use kar rahe hain taake logic sahi chale
        cols[i].button(label, use_container_width=True, on_click=update_expr, args=(label,))

# 7. History Sidebar
if st.sidebar.button("Clear History"):
    st.session_state.history = []
    st.rerun()

st.sidebar.subheader("History")
for item in reversed(st.session_state.history):
    st.sidebar.text(item)

add_footer()