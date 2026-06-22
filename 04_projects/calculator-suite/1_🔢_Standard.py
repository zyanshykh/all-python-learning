import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Dev Hub | Modern Calculator Suite",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Global CSS context override to completely fix the layout container widths
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"], .main {
        background-color: #0b0d12 !important;
    }
    [data-testid="stHeader"] { background: transparent !important; }
    .block-container { 
        padding-top: 1.5rem !important; 
        max-width: 450px !important; 
    }
    iframe { 
        border: none !important; 
        margin: 0 auto !important; 
        display: block !important; 
    }
    </style>
""", unsafe_allow_html=True)

# Sandboxed Pure-HTML/JS Grid Matrix Layout Engine
# Bypasses all reactive column drops completely across device viewports
calculator_canvas = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    user-select: none;
}
body {
    background-color: #0b0d12;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 5px;
}
.calc-container {
    width: 100%;
    max-width: 360px;
    background-color: #121620;
    border: 1px solid #1e2538;
    border-radius: 20px;
    padding: 22px;
    box-shadow: 0px 20px 40px rgba(0, 0, 0, 0.5);
}
.brand-title {
    color: #ffffff;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 0.5px;
    margin-bottom: 2px;
}
.brand-sub {
    color: #4b5563;
    font-size: 11px;
    margin-bottom: 16px;
    text-transform: uppercase;
}
.display-wrapper {
    width: 100%;
    background-color: #07090d;
    border: 1px solid #1e2538;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 20px;
    min-height: 85px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-end;
}
.history-display {
    color: #4b5563;
    font-size: 14px;
    font-family: monospace;
    min-height: 18px;
    word-break: break-all;
}
.main-display {
    color: #ffffff;
    font-size: 34px;
    font-weight: 600;
    font-family: monospace;
    word-break: break-all;
    max-height: 45px;
    overflow: hidden;
}
.keypad-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
}
button {
    width: 100%;
    height: 52px;
    border-radius: 10px;
    font-size: 20px;
    font-weight: 600;
    background-color: #1e2433;
    color: #f3f4f6;
    border: none;
    cursor: pointer;
    transition: background 0.1s, transform 0.05s;
    display: flex;
    justify-content: center;
    align-items: center;
    -webkit-tap-highlight-color: transparent;
}
button:active {
    transform: scale(0.96);
    background-color: #272f42;
}
.btn-operator {
    background-color: #2563eb;
    color: #ffffff;
}
.btn-operator:active {
    background-color: #1d4ed8;
}
.btn-utility {
    background-color: #2e374a;
    color: #cbd5e1;
}
.btn-utility:active {
    background-color: #3d4961;
}
.devhub-footer {
    text-align: center;
    margin-top: 18px;
    color: #4b5563;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 1px;
}
</style>
</head>
<body>

<div class="calc-container">
    <div class="brand-title">Standard Engine</div>
    <div class="brand-sub">Modern Precision System</div>
    
    <div class="display-wrapper">
        <div class="history-display" id="history"></div>
        <div class="main-display" id="output">0</div>
    </div>
    
    <div class="keypad-grid">
        <button class="btn-utility" onclick="action('C')">C</button>
        <button class="btn-utility" onclick="action('back')">⌫</button>
        <button class="btn-utility" onclick="action('%')">%</button>
        <button class="btn-operator" onclick="action('/')">÷</button>
        
        <button onclick="action('7')">7</button>
        <button onclick="action('8')">8</button>
        <button onclick="action('9')">9</button>
        <button class="btn-operator" onclick="action('*')">×</button>
        
        <button onclick="action('4')">4</button>
        <button onclick="action('5')">5</button>
        <button onclick="action('6')">6</button>
        <button class="btn-operator" onclick="action('-')">−</button>
        
        <button onclick="action('1')">1</button>
        <button onclick="action('2')">2</button>
        <button onclick="action('3')">3</button>
        <button class="btn-operator" onclick="action('+')">+</button>
        
        <button onclick="action('.')">.</button>
        <button onclick="action('0')">0</button>
        <button style="grid-column: span 2;" class="btn-operator" onclick="action('=')">=</button>
    </div>
    
    <div class="devhub-footer">CREATED BY DEV HUB</div>
</div>

<script>
let currentInput = "";
let arithmeticExpression = "";

const outputScreen = document.getElementById('output');
const historyScreen = document.getElementById('history');

function formatDisplay(expr) {
    return expr.replace(/\*/g, ' × ').replace(/\//g, ' ÷ ').replace(/\+/g, ' + ').replace(/-/g, ' − ');
}

function action(key) {
    if (key === 'C') {
        currentInput = "";
        arithmeticExpression = "";
        outputScreen.innerText = "0";
        historyScreen.innerText = "";
    } 
    else if (key === 'back') {
        if (arithmeticExpression.length > 0) {
            arithmeticExpression = arithmeticExpression.slice(0, -1);
            outputScreen.innerText = formatDisplay(arithmeticExpression) || "0";
        }
    } 
    else if (key === '=') {
        if (arithmeticExpression) {
            try {
                let cleanExpression = arithmeticExpression;
                let evaluation = eval(cleanExpression);
                
                // Keep clean floating point results without long tail decimals
                let result = Number(evaluation.toFixed(6)).toString();
                
                historyScreen.innerText = formatDisplay(arithmeticExpression) + " =";
                outputScreen.innerText = result;
                arithmeticExpression = result; // preserve state for multi-step math
            } catch (e) {
                outputScreen.innerText = "Error";
                arithmeticExpression = "";
            }
        }
    } 
    else if (key === '%') {
        if (arithmeticExpression) {
            try {
                let evaluation = eval(arithmeticExpression) / 100;
                outputScreen.innerText = Number(evaluation.toFixed(6)).toString();
                arithmeticExpression = evaluation.toString();
            } catch(e) {
                outputScreen.innerText = "Error";
            }
        }
    } 
    else {
        // Prevent duplicate consecutive operation anomalies
        const operators = ['+', '-', '*', '/'];
        if (operators.includes(key) && operators.includes(arithmeticExpression.slice(-1))) {
            arithmeticExpression = arithmeticExpression.slice(0, -1) + key;
        } else {
            arithmeticExpression += key;
        }
        outputScreen.innerText = formatDisplay(arithmeticExpression);
    }
}
</script>

</body>
</html>
"""

# Embed locked canvas into Streamlit ecosystem
components.html(calculator_canvas, height=490, scrolling=False)