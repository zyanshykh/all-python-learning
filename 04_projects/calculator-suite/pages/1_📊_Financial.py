import streamlit as st

st.set_page_config(page_title="Financial Analytics", page_icon="📊", layout="centered")

st.sidebar.markdown("# ⚙️ Main Menu")
st.sidebar.markdown("---")

st.title("📊 Financial Calculator")
st.markdown("---")

tab1, tab2 = st.tabs(["💰 Loan EMI Calculator", "📈 Compound Interest"])

with tab1:
    st.subheader("Calculate Monthly Loan EMI")
    principal = st.number_input("Principal Amount ($/Rs)", min_value=1000, value=50000, step=1000)
    tenure_years = st.slider("Loan Tenure (Years)", min_value=1, max_value=30, value=5)
    interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.5, max_value=25.0, value=7.5, step=0.1)

    if st.button("Calculate EMI", key="emi_btn"):
        r = (interest_rate / 12) / 100
        n = tenure_years * 12
        emi = (principal * r * (1 + r)**n) / ((1 + r)**n - 1)
        total_payment = emi * n
        total_interest = total_payment - principal
        
        st.success(f"Monthly EMI: **${emi:,.2f}**")
        c1, c2 = st.columns(2)
        c1.metric("Total Interest", f"${total_interest:,.2f}")
        c2.metric("Total Payable Amount", f"${total_payment:,.2f}")

with tab2:
    st.subheader("Compound Interest Calculator")
    p_ci = st.number_input("Initial Investment ($/Rs)", min_value=100, value=10000, step=500)
    rate_ci = st.number_input("Annual Interest Rate (CI %)", min_value=0.1, max_value=50.0, value=8.0, step=0.5)
    time_ci = st.slider("Time Period (Years)", min_value=1, max_value=40, value=10)
    
    future_value = p_ci * ((1 + (rate_ci / 100)) ** time_ci)
    net_interest = future_value - p_ci
    
    st.info(f"Future Wealth Value: **${future_value:,.2f}**")
    st.metric("Total Interest Earned", f"${net_interest:,.2f}")