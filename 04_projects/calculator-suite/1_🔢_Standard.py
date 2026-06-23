import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Dev Hub | Calculator", page_icon="🧮", layout="centered")

# 2. Modern & Responsive CSS
def apply_style():
    st.markdown("""
        <style>
        /* Mobile aur Desktop ke liye common container */
        .block-container { max-width: 450px !important; padding: 1rem !important; }
                /* Input Box Styling - Fix */
        .stTextInput>div>div>input {
            font-size: 32px !important;
            text-align: right !important;
            height: 80px !important; /* Thodi height badha di taake text saaf dikhe */
            padding-right: 20px !important;
            background-color: #1a1a1a !important;
            color: #ffffff !important;
            border: 2px solid #333 !important;
            border-radius: 12px !important;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.3) !important;
        }

        /* Label ko hide rakho taake UI saaf rahe */
        div[data-testid="stTextInput"] label {
            display: none !important;
        }
        
        /* Input Box Styling */
        .stTextInput>div>div>input {
            font-size: 32px !important;
            text-align: right !important;
            height: 70px !important;
            background-color: #1e1e1e !important;
            border-radius: 10px !important;
        }
                /* Sabhi input boxes ko ek jaisa aur clean banane ke liye */
    div[data-testid="stTextInput"] > div > div > input {
        text-align: right !important;
        background-color: #1a1a1a !important;
        color: white !important;
        border: 1px solid #444 !important;
        border-radius: 8px !important;
    }
    
    /* Plus/Minus buttons ko hatane ka CSS hack */
    div[data-testid="stNumberInput"] button {
        display: none !important;
    }

        /* Buttons responsive design */
        div.stButton > button {
            height: 65px !important;
            font-size: 22px !important;
            border-radius: 12px !important;
            transition: 0.3s !important;
            border: 1px solid #333 !important;
        }
        
        div.stButton > button:hover { border-color: #00ffa3 !important; }
        
        /* Footer Branding */
        .footer { text-align: center; color: #555; margin-top: 30px; font-size: 13px; }
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