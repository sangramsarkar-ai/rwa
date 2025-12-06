import streamlit as st
import pandas as pd
import plotly.express as px

# 👉 Import all static data from separate file
from rwa_data import (
    TOTAL_SQFT,
    EXEC_MEMBERS,
    SUPPORT_STAFF,
    MANPOWER_NOV,
    MANPOWER_DEC,
    RUNNING_COST,
    TOTAL_RUNNING,
    PROVISIONS,
    TOTAL_PROVISIONS,
)

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Candeur Sunshine RWA – GBM Overview",
    page_icon="🏙️",
    layout="wide",
)

# ---------- CUSTOM STYLING (MODERN / GLASS) ----------
st.markdown(
    """
    <style>
    /* Overall background */
    .stApp {
        background: radial-gradient(circle at top left, #e9e4ff 0, #ffffff 45%, #f5f7fb 100%);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    /* Main block container padding */
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #313866, #504099);
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span {
        color: #f5f5ff !important;
    }

    /* Glass card */
    .glass-card {
        background: rgba(255, 255, 255, 0.86);
        border-radius: 18px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(12px);
    }

    .glass-card h2, .glass-card h3 {
        margin-top: 0;
        font-weight: 600;
        letter-spacing: 0.02em;
        color: #1f2933;
    }

    .glass-card p {
        margin-bottom: 0.4rem;
        color: #4b5563;
    }

    /* Headings */
    h1 {
        font-weight: 700;
        letter-spacing: 0.03em;
        color: #1f2933;
    }
    h2, h3 {
        font-weight: 600;
        color: #111827;
    }

    /* Metric label tweak */
    [data-testid="stMetricValue"] {
        font-size: 1.4rem;
    }
    [data-testid="stMetricLabel"] {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #6b7280;
    }

    /* Tables */
    .dataframe {
        border-radius: 12px;
        overflow: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- PAGE HEADER ----------
st.markdown(
    """
    <div class="glass-card" style="margin-bottom: 1.5rem;">
        <h1>🏙️ Candeur Sunshine Residents Welfare Association</h1>
        <p style="font-size:0.95rem; color:#6b7280; margin-bottom:0.4rem;">
            Introductory General Body Meeting • Maintenance & Cost Overview Dashboard
        </p>
        <p style="font-size:0.9rem; color:#4b5563;">
            Track manpower, running costs, provisions, and <strong>per sq ft monthly maintenance</strong> with a clear, modern view.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- COMMON CALCULATIONS ----------
def compute_common(additional_provision: int):
    running_per_sqft_local = TOTAL_RUNNING / TOTAL_SQFT
    effective_total_provisions_local = TOTAL_PROVISIONS + additional_provision
    per_month_provision_local = effective_total_provisions_local / 9
    provision_per_sqft_per_month_local = (
        per_month_provision_local / TOTAL_SQFT
    )
    total_maintenance_local = (
        running_per_sqft_local + provision_per_sqft_per_month_local
    )
    return (
        running_per_sqft_local,
        effective_total_provisions_local,
        per_month_provision_local,
        provision_per_sqft_per_month_local,
        total_maintenance_local,
    )

# ---------- HELPERS ----------
def glass_container(title: str = None):
    if title:
        st.markdown(f'<div class="glass-card"><h2>{title}</h2>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)

def glass_container_end():
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- SIDEBAR (INPUTS) ----------
st.sidebar.title("⚙️ Controls")

additional_provision = st.sidebar.number_input(
    "Additional Provision (₹)",
    min_value=0,
    step=1_000,
    value=0,
    help="Add any extra provision amount you want to simulate (e.g., new projects/buffers).",
)

st.sidebar.markdown(
    f"""
    <small>
    <strong>Total Built-up Area</strong><br/>
    {TOTAL_SQFT:,} sq ft
    </small>
    """,
    unsafe_allow_html=True,
)

# Recompute with current additional_provision
(
    running_per_sqft,
    effective_total_provisions,
    per_month_provision,
    provision_per_sqft_per_month,
    total_maintenance_per_sqft_per_month,
) = compute_common(additional_provision)

# ---------- TABS NAVIGATION (TOP) ----------
tab_titles = [
    "📋 Agenda",
    "👥 Executive Committee",
    "🛠️ Maintenance Overview",
    "🏗️ Facility Management & Staff",
    "👨‍🔧 Manpower (Nov vs Dec)",
    "💰 Running Cost",
    "📦 Provisions / Capex",
    "📊 Maintenance Revision",  # last
]

(
    tab_agenda,
    tab_exec,
    tab_maint_overview,
    tab_fm_staff,
    tab_manpower,
    tab_running,
    tab_provisions,
    tab_revision,
) = st.tabs(tab_titles)

# ---------- TAB: AGENDA ----------
with tab_agenda:
    glass_container("📋 Agenda for the Meeting")

    st.markdown(
        """
1. **Welcome & Introduction to the Residents Welfare Association**  
2. **Overview of the Ongoing Maintenance Processes**  
3. **Clarification of Inclusions and Exclusions under Maintenance**  
4. **Discussion on Current Resident Issues and Proposed Resolutions**  
5. **Open Forum for Questions, Feedback, and Suggestions**  
        """
    )

    st.info(
        "This meeting sets the foundation for transparency, clarity in processes, "
        "and collaborative improvement of the community."
    )

    glass_container_end()

# ---------- TAB: EXECUTIVE COMMITTEE ----------
with tab_exec:
    glass_container("👥 Executive Committee")

    col1, col2 = st.columns(2)
    half = len(EXEC_MEMBERS) // 2

    with col1:
        for name in EXEC_MEMBERS[:half]:
            st.markdown(f"• **{name}**")
    with col2:
        for name in EXEC_MEMBERS[half:]:
            st.markdown(f"• **{name}**")

    st.success(
        "This team is responsible for governance, decision-making, and representing "
        "resident interests in all key matters."
    )

    glass_container_end()

# ---------- TAB: MAINTENANCE OVERVIEW ----------
with tab_maint_overview:
    glass_container("🛠️ Overview of the Ongoing Maintenance Processes")

    st.markdown(
        """
- Maintenance operations were **officially handed over on 1st November**.  
- Evaluation of the current system is still in progress, including:
  - Reviewing existing processes  
  - Identifying areas for improvement  
  - Implementing necessary process changes  
- Partnered with **Idencies Facility Management Services** for day-to-day operations.  
- Facility Manager role was restructured after initial transition challenges.
        """
    )

    st.info(
        "Goal: Build a predictable, efficient, and resident-centric maintenance system."
    )

    glass_container_end()

# ---------- TAB: FACILITY MANAGEMENT & STAFF ----------
with tab_fm_staff:
    glass_container("🏗️ Facility Management & Support Staff")

    st.subheader("Facility Manager")
    st.markdown(
        "**Hemanth** – Responsible for overseeing all maintenance operations "
        "and coordination with Idencies FM."
    )

    st.subheader("Key Support Staff")
    df_staff = pd.DataFrame(SUPPORT_STAFF)
    st.dataframe(df_staff, use_container_width=True)

    st.caption(
        "This structure ensures quicker response, accountability, and smoother daily operations."
    )

    glass_container_end()

# ---------- TAB: MANPOWER ----------
with tab_manpower:
    glass_container("👨‍🔧 Manpower Deployment – November vs December")

    comp_rows = []
    for role in MANPOWER_NOV:
        nov_val = MANPOWER_NOV[role]
        dec_val = MANPOWER_DEC.get(role, nov_val)
        change = dec_val - nov_val
        if change > 0:
            indicator = "⬆️ +" + str(change)
        elif change < 0:
            indicator = "⬇️ " + str(change)
        else:
            indicator = "➖ 0"
        comp_rows.append(
            {
                "Role": role,
                "November": nov_val,
                "December": dec_val,
                "Change": change,
                "Change Indicator": indicator,
            }
        )
    df_comp = pd.DataFrame(comp_rows)

    st.subheader("Combined Manpower View")
    st.dataframe(df_comp, use_container_width=True)

    st.info(
        "- **Housekeeping Staff** increased from 8 → 10 (**+2**) – better cleanliness and coverage.\n"
        "- **Gardeners** increased from 1 → 2 (**+1**) – improved landscaping and green maintenance.\n"
        "- All other roles remain stable to ensure continuity."
    )

    glass_container_end()

# ---------- TAB: RUNNING COST ----------
with tab_running:
    glass_container("💰 Monthly Running Cost")

    df_cost = pd.DataFrame(
        [{"Head": k, "Amount (₹)": v} for k, v in RUNNING_COST.items()]
    )

    st.subheader("Cost Breakdown")
    st.table(df_cost)

    # 👇 Chart removed – only metrics now
    st.metric("Total Monthly Running Cost (₹)", f"{TOTAL_RUNNING:,.0f}")
    st.metric("Monthly Running Cost / sq ft (₹)", f"{running_per_sqft:.2f}")

    st.caption(
        "These costs cover essential services like water, power, facility management, "
        "waste management, and basic upkeep."
    )

    glass_container_end()




# ---------- TAB: PROVISIONS / CAPEX ----------
with tab_provisions:
    glass_container("📦 Provisions & Capital Expenditure")

    df_prov = pd.DataFrame(
        [{"Item": k, "Amount (₹)": v} for k, v in PROVISIONS.items()]
    ).sort_values("Amount (₹)", ascending=False)

    col1, col2 = st.columns(2)

    # --- LEFT SIDE: TABLE ---
    with col1:
        st.subheader("Major Provisions / Capex Items")
        st.table(df_prov)

        # Estimate table height dynamically
        table_height = 40 * len(df_prov) + 120  # row height * rows + header padding

    # --- RIGHT SIDE: MATCHING-HEIGHT CHART ---
    with col2:
        st.subheader("Chart View")

        fig = px.bar(
            df_prov,
            x="Amount (₹)",
            y="Item",
            orientation="h",
            title="",
        )
        fig.update_layout(
            height=table_height,     # 👈 MATCH HEIGHT TO TABLE
            margin=dict(l=10, r=10, t=10, b=10),
        )
        st.plotly_chart(fig, use_container_width=True)

    col3, col4, col5 = st.columns(3)
    with col3:
        st.metric("Base Provisions / Capex (₹)", f"{TOTAL_PROVISIONS:,.0f}")
    with col4:
        st.metric("Additional Provision (₹)", f"{additional_provision:,.0f}")
    with col5:
        st.metric(
            "Effective Provisions (₹)",
            f"{effective_total_provisions:,.0f}",
        )

    st.markdown("### Normalized view (over 9 months)")
    st.metric("Per Month Provision (₹)", f"{per_month_provision:,.0f}")
    st.metric("Provisions / sq ft / month (₹)", f"{provision_per_sqft_per_month:.2f}")

    st.info(
        "Provisions are distributed over 9 months and normalized by total built-up area "
        f"({TOTAL_SQFT:,} sq ft) to estimate the per sq ft per month impact."
    )

    glass_container_end()


# ---------- TAB: MAINTENANCE REVISION (Per Sq Ft Summary) ----------
with tab_revision:
    glass_container("📊 Maintenance Revision – Per Sq Ft Summary")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Built-up Area (sq ft)", f"{TOTAL_SQFT:,.0f}")
        st.metric("Monthly Running Cost (₹)", f"{TOTAL_RUNNING:,.0f}")
    with col2:
        st.metric("Base Provisions (₹)", f"{TOTAL_PROVISIONS:,.0f}")
        st.metric("Additional Provision (₹)", f"{additional_provision:,.0f}")
    with col3:
        st.metric(
            "Running Cost / sq ft / month (₹)",
            f"{running_per_sqft:.2f}",
        )
        st.metric(
            "Provisions / sq ft / month (₹)",
            f"{provision_per_sqft_per_month:.2f}",
        )

    st.markdown("---")
    st.subheader("💡 Total Maintenance per sq ft per month")

    st.metric(
        "Total Maintenance / sq ft / month (₹)",
        f"{total_maintenance_per_sqft_per_month:.2f}",
        help=(
            "This is: (Monthly Running Cost / sq ft) "
            "+ (Provisions / sq ft per month over 9 months, including additional provisions)."
        ),
    )

    st.markdown(
        """
        <p style="font-size:0.9rem; color:#4b5563; margin-top:0.8rem;">
        Adjust <strong>Additional Provision</strong> in the sidebar to instantly see
        the impact on per sq ft monthly maintenance.
        </p>
        """,
        unsafe_allow_html=True,
    )

    glass_container_end()
