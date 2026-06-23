import streamlit as st

# Page Config
st.set_page_config(
    page_title="Dev Hub | Calculator", 
    page_icon="🧮", 
    layout="centered",
    initial_sidebar_state="collapsed" # Sidebar band rahega
)

# CSS Function
def apply_style():
    st.markdown("""
        <style>
        /* Container width fix */
        .block-container { 
            max-width: 500px !important; 
            padding-top: 1rem !important; 
        }

        /* Input Box */
        .stTextInput > div > div > input {
            font-size: 32px !important;
            text-align: right !important;
            height: 70px !important;
            background-color: #1a1a1a !important;
            border: 2px solid #333 !important;
            border-radius: 10px !important;
            width: 100% !important;
        }

        /* Buttons */
        div.stButton > button {
            height: 60px !important;
            font-size: 20px !important;
            border-radius: 10px !important;
        }
        </style>
    """, unsafe_allow_html=True)

apply_style()

# 3. Branding Header
st.title("🔢 Smart Calculator")
st.caption("Dev Hub | Ecosystem Mode")

# 4. App Logic
if "expr" not in st.session_state: st.session_state.expr = ""

user_typed = st.text_input("Input", value=st.session_state.expr, label_visibility="collapsed")
if user_typed != st.session_state.expr:
    st.session_state.expr = user_typed
    st.rerun()

# 5. Responsive Grid (Buttons)
buttons = [
    ["C", ".", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", "="]
]

for row in buttons:
    # Column layout screen ke hisaab se adjust hoga
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        if cols[i].button(btn, use_container_width=True):
            if btn == "C": st.session_state.expr = ""
            elif btn == "=":
                try: st.session_state.expr = str(round(eval(st.session_state.expr), 4))
                except: st.session_state.expr = "Error"
            else: st.session_state.expr += btn
            st.rerun()

# 6. Professional Footer
st.markdown("""
    <div class="footer">
        Dev Hub Ecosystem | Professional Grade Tool
    </div>
""", unsafe_allow_html=True)