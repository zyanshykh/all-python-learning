import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Zyan Studio | Calculator Suite",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Initialize Session State values safely
if 'expr' not in st.session_state:
    st.session_state.expr = ""

# Handle direct actions from the custom HTML template buttons
query_params = st.query_transform(st.experimental_get_query_params() if hasattr(st, 'experimental_get_query_params') else {})
# Safe backward-compatible alternative for newer Streamlit query parameter fetches
try:
    current_params = st.query_params
    if "action" in current_params:
        clicked_val = current_params["action"]
        if clicked_val == "C":
            st.session_state.expr = ""
        elif clicked_val == "=":
            if st.session_state.expr:
                try:
                    st.session_state.expr = str(round(eval(st.session_state.expr), 4))
                except ZeroDivisionError:
                    st.session_state.expr = "Cannot divide by 0"
                except Exception:
                    st.session_state.expr = "Error"
        else:
            # Map clean visual signs back to execution variables
            mapped_val = clicked_val.replace("×", "*").replace("÷", "/")
            st.session_state.expr += mapped_val
        
        # Clear query state parameters instantly to prevent endless loop triggers on page reloads
        st.query_params.clear()
        st.rerun()
except Exception:
    pass

# Custom CSS Injection to lock down App View wrapper margins
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"], .main {
        background-color: #0d0f14 !important;
    }
    [data-testid="stHeader"] { background: transparent !important; }
    /* Hide native container paddings so our app sits perfect */
    .block-container { padding-top: 2rem !important; padding-bottom: 0rem !important; }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("# ⚙️ Main Menu")
st.sidebar.markdown("---")

# Display fallback standard tracking representation safely
display_value = st.session_state.expr if st.session_state.expr else "0"

# Pure Native HTML & CSS Architecture Blueprint Grid Layout Matrix
# This bypasses all reactive layouts and guarantees 1:1 scaling everywhere
calculator_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<style>
* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}}
body {{
    background-color: #0d0f14;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10px;
}}
.calc-card-wrapper {{
    width: 100%;
    max-width: 350px;
    background: #151922;
    border-radius: 24px;
    border: 1px solid #222936;
    padding: 20px;
    box-shadow: 0px 15px 40px rgba(0, 0, 0, 0.6);
}}
.header-text {{
    text-align: center;
    color: #ffffff;
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 2px;
}}
.sub-text {{
    text-align: center;
    color: #64748b;
    font-size: 11px;
    margin-bottom: 18px;
    letter-spacing: 0.5px;
}}
.display-screen {{
    width: 100%;
    height: 70px;
    background-color: #090b0f;
    border: 1px solid #222936;
    border-radius: 14px;
    color: #ffffff;
    font-size: 34px;
    text-align: right;
    padding: 12px 16px;
    margin-bottom: 16px;
    overflow-x: auto;
    white-space: nowrap;
    font-family: monospace;
}}
.grid-matrix {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
}}
button {{
    width: 100%;
    height: 54px;
    border-radius: 12px;
    font-size: 20px;
    font-weight: 600;
    background-color: #1e2430;
    color: #e2e8f0;
    border: none;
    cursor: pointer;
    transition: all 0.1s ease;
    display: flex;
    justify-content: center;
    align-items: center;
    -webkit-tap-highlight-color: transparent;
}}
button:active {{
    transform: scale(0.95);
    background-color: #293142;
}}
.btn-operator {{
    background-color: #3b82f6;
    color: #ffffff;
}}
.btn-operator:active {{
    background-color: #2563eb;
}}
.btn-utility {{
    background-color: #2d3748;
    color: #cbd5e1;
}}
.btn-utility:active {{
    background-color: #4a5568;
}}
</style>
</head>
<body>

<div class="calc-card-wrapper">
    <div class="header-text">Smart Calculator</div>
    <div class="sub-text">Zyan Studio Premium Suite</div>
    
    <div class="display-screen">{display_value}</div>
    
    <div class="grid-matrix">
        <button class="btn-utility" onclick="sendAction('C')">C</button>
        <button class="btn-utility" onclick="sendAction('.')">.</button>
        <button class="btn-utility" onclick="sendAction('%')">%</button>
        <button class="btn-operator" onclick="sendAction('÷')">÷</button>
        
        <button onclick="sendAction('7')">7</button>
        <button onclick="sendAction('8')">8</button>
        <button onclick="sendAction('9')">9</button>
        <button class="btn-operator" onclick="sendAction('×')">×</button>
        
        <button onclick="sendAction('4')">4</button>
        <button onclick="sendAction('5')">5</button>
        <button onclick="sendAction('6')">6</button>
        <button class="btn-operator" onclick="sendAction('-')">-</button>
        
        <button onclick="sendAction('1')">1</button>
        <button onclick="sendAction('2')">2</button>
        <button onclick="sendAction('3')">3</button>
        <button class="btn-operator" onclick="sendAction('+')">+</button>
        
        <button style="grid-column: span 2;" onclick="sendAction('0')">0</button>
        <button style="grid-column: span 2;" class="btn-operator" onclick="sendAction('=')">=</button>
    </div>
</div>

<script>
function sendAction(value) {{
    // Inject parameters directly back to parent frame window safely via search queries
    const url = new URL(window.parent.location.href);
    url.searchParams.set('action', value);
    window.parent.location.href = url.toString();
}}
</script>

</body>
</html>
"""

# Inject iframe element into Streamlit dashboard securely with static sizing bounds
components.html(calculator_html, height=440, scrolling=False)