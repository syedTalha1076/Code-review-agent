
import streamlit as st

from src.graph import workflow


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Code Review Agent",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       GLOBAL
       ====================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(99, 102, 241, 0.12),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(14, 165, 233, 0.10),
                transparent 25%
            ),
            #080b12;
    }

    .main {
        padding-top: 1rem;
    }

    /* Remove Streamlit header */
    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* ======================================================
       SIDEBAR
       ====================================================== */

    section[data-testid="stSidebar"] {
        background: #0b0f18;
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }

    /* ======================================================
       HERO
       ====================================================== */

    .hero {
        padding: 2.5rem 2rem;
        border-radius: 24px;
        background:
            linear-gradient(
                135deg,
                rgba(30, 41, 59, 0.95),
                rgba(15, 23, 42, 0.90)
            );
        border: 1px solid rgba(148, 163, 184, 0.15);
        box-shadow:
            0 20px 60px rgba(0,0,0,0.30);
        margin-bottom: 2rem;
    }

    .hero-badge {
        display: inline-block;
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        background: rgba(99,102,241,0.14);
        border: 1px solid rgba(99,102,241,0.30);
        color: #a5b4fc;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }

    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        line-height: 1.1;
        margin: 0;
        background:
            linear-gradient(
                90deg,
                #f8fafc,
                #c7d2fe,
                #7dd3fc
            );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 1.05rem;
        line-height: 1.7;
        margin-top: 1rem;
        max-width: 850px;
    }

    /* ======================================================
       CARDS
       ====================================================== */

    .card {
        background: rgba(15, 23, 42, 0.72);
        border: 1px solid rgba(148, 163, 184, 0.12);
        border-radius: 18px;
        padding: 1.25rem;
        height: 100%;
        box-shadow: 0 10px 35px rgba(0,0,0,0.18);
    }

    .card-title {
        color: #f8fafc;
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }

    .card-text {
        color: #94a3b8;
        font-size: 0.88rem;
        line-height: 1.6;
    }

    /* ======================================================
       PIPELINE
       ====================================================== */

    .pipeline {
        background: rgba(15, 23, 42, 0.65);
        border: 1px solid rgba(148,163,184,0.12);
        border-radius: 18px;
        padding: 1.3rem;
        margin: 1.5rem 0;
    }

    .pipeline-title {
        color: #f8fafc;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    .pipeline-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 0.5rem;
        flex-wrap: wrap;
    }

    .pipeline-step {
        flex: 1;
        min-width: 100px;
        text-align: center;
        padding: 0.75rem 0.5rem;
        border-radius: 12px;
        background: #111827;
        border: 1px solid rgba(148,163,184,0.10);
        color: #cbd5e1;
        font-size: 0.78rem;
    }

    .pipeline-step.active {
        border-color: rgba(99,102,241,0.45);
        background: rgba(99,102,241,0.10);
        color: #c7d2fe;
    }

    .arrow {
        color: #475569;
        font-size: 1.2rem;
    }

    /* ======================================================
       SECTION TITLES
       ====================================================== */

    .section-title {
        font-size: 1.35rem;
        font-weight: 750;
        color: #f8fafc;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }

    /* ======================================================
       FOOTER
       ====================================================== */

    .footer {
        margin-top: 4rem;
        padding: 1.5rem;
        text-align: center;
        color: #64748b;
        border-top: 1px solid rgba(148,163,184,0.10);
    }

    .footer-name {
        color: #c7d2fe;
        font-weight: 700;
    }

    /* ======================================================
       INPUT
       ====================================================== */

    div[data-baseweb="input"] {
        background: rgba(15,23,42,0.75);
        border-radius: 12px;
    }

    div[data-baseweb="input"] input {
        color: #f8fafc;
    }

    /* ======================================================
       BUTTON
       ====================================================== */

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: 1px solid rgba(99,102,241,0.35);
        background:
            linear-gradient(
                135deg,
                #4f46e5,
                #2563eb
            );
        color: white;
        font-weight: 700;
        padding: 0.7rem 1rem;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: rgba(165,180,252,0.8);
        transform: translateY(-1px);
        box-shadow:
            0 8px 25px rgba(37,99,235,0.25);
    }

    /* ======================================================
       EXPANDERS
       ====================================================== */

    div[data-testid="stExpander"] {
        background: rgba(15,23,42,0.55);
        border: 1px solid rgba(148,163,184,0.12);
        border-radius: 14px;
        margin-bottom: 0.7rem;
    }

    /* ======================================================
       STATUS
       ====================================================== */

    .status-card {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        padding: 1rem;
        border-radius: 14px;
        background: rgba(16,185,129,0.08);
        border: 1px solid rgba(16,185,129,0.20);
        color: #a7f3d0;
        margin-bottom: 1rem;
    }

    .status-dot {
        width: 9px;
        height: 9px;
        border-radius: 50%;
        background: #34d399;
        box-shadow: 0 0 12px rgba(52,211,153,0.8);
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:0.5rem 0 1.5rem 0;
        ">
            <div style="
                font-size:2.4rem;
                margin-bottom:0.4rem;
            ">
                🔍
            </div>

            <div style="
                font-size:1.15rem;
                font-weight:800;
                color:#f8fafc;
            ">
                AI Code Reviewer
            </div>

            <div style="
                font-size:0.78rem;
                color:#64748b;
                margin-top:0.3rem;
            ">
                Intelligent PR Analysis
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown(
        """
        <div class="card">

            <div class="card-title">
                AI Engine
            </div>

            <div class="card-text">

            <b>Primary</b><br>
            Groq — GPT-OSS 120B

            <br><br>

            <b>Fallback</b><br>
            Cerebras — Llama

            <br><br>

            Automatic fallback protects
            the workflow from temporary
            model failures and rate limits.

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="card">

            <div class="card-title">
                Review Capabilities
            </div>

            <div class="card-text">

            ✓ Bug Detection<br>
            ✓ Security Analysis<br>
            ✓ Code Quality<br>
            ✓ Severity Classification<br>
            ✓ AI Recommendations<br>
            ✓ Consolidated Review

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HERO SECTION
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-badge">
            LangGraph Powered AI
        </div>

        <h1 class="hero-title">
            AI Code Review Agent
        </h1>

        <div class="hero-subtitle">
            An intelligent multi-agent system that analyzes
            GitHub Pull Requests, detects bugs, identifies
            security vulnerabilities, evaluates code quality,
            and generates professional review recommendations.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# CAPABILITY CARDS
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
        <div class="card">

            <div style="font-size:1.7rem;">
                🐛
            </div>

            <div class="card-title">
                Bug Detection
            </div>

            <div class="card-text">
                Detects logic errors, runtime problems,
                edge cases and exception-handling issues.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with col2:

    st.markdown(
        """
        <div class="card">

            <div style="font-size:1.7rem;">
                🛡️
            </div>

            <div class="card-title">
                Security Analysis
            </div>

            <div class="card-text">
                Identifies vulnerabilities such as SQL
                injection, exposed secrets and unsafe
                input handling.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with col3:

    st.markdown(
        """
        <div class="card">

            <div style="font-size:1.7rem;">
                ⚡
            </div>

            <div class="card-title">
                Code Quality
            </div>

            <div class="card-text">
                Evaluates readability, maintainability,
                performance and software engineering
                best practices.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# PIPELINE
# ============================================================

st.markdown(
    """
    <div class="pipeline">

        <div class="pipeline-title">
            Review Pipeline
        </div>

        <div class="pipeline-row">

            <div class="pipeline-step active">
                PR Input
            </div>

            <div class="arrow">→</div>

            <div class="pipeline-step">
                Analyze
            </div>

            <div class="arrow">→</div>

            <div class="pipeline-step">
                Bugs
            </div>

            <div class="arrow">→</div>

            <div class="pipeline-step">
                Security
            </div>

            <div class="arrow">→</div>

            <div class="pipeline-step">
                Quality
            </div>

            <div class="arrow">→</div>

            <div class="pipeline-step">
                Aggregate
            </div>

            <div class="arrow">→</div>

            <div class="pipeline-step">
                Report
            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# INPUT SECTION
# ============================================================

st.markdown(
    '<div class="section-title">Analyze a Pull Request</div>',
    unsafe_allow_html=True,
)

st.write(
    "Enter the GitHub Pull Request URL below to start the AI review."
)

pr_url = st.text_input(
    "GitHub Pull Request URL",
    placeholder="https://github.com/username/repository/pull/123",
    label_visibility="collapsed",
)


# ============================================================
# REVIEW BUTTON
# ============================================================

review_button = st.button(
    "🚀  Start AI Code Review"
)


if review_button:

    if not pr_url.strip():

        st.warning(
            "Please enter a GitHub Pull Request URL."
        )

    else:

        initial_state = {

            "pr_url": pr_url,

            "pr_title": "",

            "pr_description": "",

            "changed_files": [],

            "code_diff": "",

            "code_analysis": "",

            "bugs": "",

            "security_issues": "",

            "quality_issues": "",

            "final_review": "",
        }

        # ====================================================
        # RUN LANGGRAPH
        # ====================================================

        with st.status(
            "Running AI Code Review...",
            expanded=True,
        ) as status:

            try:

                st.write("Fetching Pull Request information...")

                result = workflow.invoke(
                    initial_state
                )

                st.write(
                    "Analyzing code with specialized reviewers..."
                )

                st.write(
                    "Consolidating findings..."
                )

                st.write(
                    "Generating final review..."
                )

                status.update(
                    label="Code review completed",
                    state="complete",
                    expanded=False,
                )

            except Exception as e:

                status.update(
                    label="Code review failed",
                    state="error",
                    expanded=True,
                )

                st.error(
                    f"An error occurred: {str(e)}"
                )

                st.stop()

        # ====================================================
        # SUCCESS STATUS
        # ====================================================

        st.markdown(
            """
            <div class="status-card">

                <div class="status-dot"></div>

                <div>
                    <b>Review Completed</b><br>
                    <span style="color:#6ee7b7;">
                        AI analysis successfully generated.
                    </span>
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


        # ====================================================
        # PR INFORMATION
        # ====================================================

        st.markdown(
            '<div class="section-title">Pull Request</div>',
            unsafe_allow_html=True,
        )

        info1, info2 = st.columns([2, 1])

        with info1:

            st.markdown(
                f"""
                <div class="card">

                    <div class="card-title">
                        {result["pr_title"]}
                    </div>

                    <div class="card-text">
                        {result["pr_description"]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

        with info2:

            st.markdown(
                f"""
                <div class="card">

                    <div class="card-title">
                        Changed Files
                    </div>

                    <div style="
                        font-size:2rem;
                        font-weight:800;
                        color:#c7d2fe;
                    ">
                        {len(result["changed_files"])}
                    </div>

                    <div class="card-text">
                        Files analyzed
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


        # ====================================================
        # FINAL REVIEW
        # ====================================================

        st.markdown(
            '<div class="section-title">Final AI Review</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            result["final_review"]
        )


        # ====================================================
        # DETAILED ANALYSIS
        # ====================================================

        st.markdown(
            '<div class="section-title">Detailed Analysis</div>',
            unsafe_allow_html=True,
        )


        with st.expander(
            "🧠  General Code Analysis"
        ):

            st.markdown(
                result["code_analysis"]
            )


        with st.expander(
            "🐛  Bug Detection"
        ):

            st.markdown(
                result["bugs"]
            )


        with st.expander(
            "🛡️  Security Analysis"
        ):

            st.markdown(
                result["security_issues"]
            )


        with st.expander(
            "⚡  Code Quality Analysis"
        ):

            st.markdown(
                result["quality_issues"]
            )


        # ====================================================
        # CHANGED FILES
        # ====================================================

        with st.expander(
            "📁  Changed Files"
        ):

            for file in result["changed_files"]:

                st.code(
                    file,
                    language="text"
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        <div>
            AI Code Review Agent
        </div>

        <div style="margin-top:0.4rem;">
            Powered by LangGraph • Groq • Cerebras
        </div>

        <div style="margin-top:0.8rem;">
            Developed by
            <span class="footer-name">
                Syed Talha Ali Shah
            </span>
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)
