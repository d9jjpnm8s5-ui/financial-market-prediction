"""Professional CSS styling for Streamlit dashboard"""

# Professional color palette for charts
CHART_COLORS = {
    "primary": "#2563eb",      # Blue
    "success": "#10b981",      # Green
    "danger": "#ef4444",       # Red
    "warning": "#f59e0b",      # Amber
    "secondary": "#8b5cf6",    # Purple
    "info": "#06b6d4",         # Cyan
}

SENTIMENT_COLORS = {
    "positive": "#10b981",     # Green
    "negative": "#ef4444",     # Red
    "neutral": "#6b7280",      # Gray
}

# Plotly template with dark theme and colors
PLOTLY_TEMPLATE = {
    "layout": {
        "paper_bgcolor": "#0b1120",
        "plot_bgcolor": "#111827",
        "font": {"color": "#e2e8f0", "family": "Arial"},
        "colorway": [
            "#2563eb",  # Blue
            "#10b981",  # Green
            "#ef4444",  # Red
            "#f59e0b",  # Amber
            "#8b5cf6",  # Purple
            "#06b6d4",  # Cyan
            "#ec4899",  # Pink
            "#14b8a6",  # Teal
        ],
        "title": {"font": {"size": 18, "color": "#e2e8f0"}},
        "xaxis": {
            "gridcolor": "rgba(148, 163, 184, 0.1)",
            "linecolor": "rgba(148, 163, 184, 0.3)",
        },
        "yaxis": {
            "gridcolor": "rgba(148, 163, 184, 0.1)",
            "linecolor": "rgba(148, 163, 184, 0.3)",
        },
    }
}
<style>
    /* Main container styling */
    .stApp {
        background-color: #0b1120;
        color: #e2e8f0;
    }
    
    /* Professional header styling */
    h1, h2, h3 {
        color: #e2e8f0;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 0.75rem;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #111827;
        border-radius: 0.5rem;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        color: #9ca3af;
    }
    
    .stTabs [aria-selected="true"] [data-baseweb="tab"] {
        background-color: #2563eb;
        color: white;
        box-shadow: 0 2px 8px rgba(37, 99, 235, 0.35);
    }
    
    /* Metric styling */
    [data-testid="metric-container"] {
        background-color: #111827;
        border: 1px solid rgba(148, 163, 184, 0.24);
        border-radius: 0.75rem;
        padding: 1.5rem;
        box-shadow: 0 1px 10px rgba(15, 23, 42, 0.4);
        color: #e2e8f0;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #2563eb;
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 1.5rem;
        box-shadow: 0 1px 6px rgba(37, 99, 235, 0.35);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #1d4ed8;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
    }
    
    /* Input styling */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    .stNumberInput > div > div > input {
        border-radius: 0.75rem;
        border: 1px solid rgba(148, 163, 184, 0.32);
        padding: 0.65rem 1rem;
        font-size: 0.95rem;
        background-color: #111827;
        color: #e2e8f0;
    }
    
    .stTextInput > div > div > input::placeholder,
    .stSelectbox > div > div > select::placeholder,
    .stNumberInput > div > div > input::placeholder {
        color: #94a3b8;
    }
    
    /* Success/Error/Warning styling */
    .stSuccess, .stError, .stWarning, .stInfo {
        border-radius: 0.75rem;
        padding: 1rem 1.5rem;
        border-left: 4px solid;
        background-color: rgba(15, 23, 42, 0.9);
        color: #e2e8f0;
        border: 1px solid rgba(148, 163, 184, 0.18);
    }
    
    .stSuccess {
        border-left-color: #22c55e;
    }
    
    .stError {
        border-left-color: #ef4444;
    }
    
    .stWarning {
        border-left-color: #f59e0b;
    }
    
    .stInfo {
        border-left-color: #3b82f6;
    }
    
    /* Sidebar styling */
    .stSidebar {
        background-color: #0f172a;
        border-right: 1px solid rgba(148, 163, 184, 0.16);
        color: #e2e8f0;
    }
    
    .stSidebar [data-testid="stMarkdownContainer"] {
        padding-left: 1rem;
        color: #e2e8f0;
    }
    
    /* Expander styling */
    .stExpander {
        border: 1px solid rgba(148, 163, 184, 0.16);
        border-radius: 0.75rem;
        background-color: #111827;
    }
    
    .stExpander > div[role="button"] {
        background-color: #111827;
        padding: 1rem;
        font-weight: 600;
        color: #e2e8f0;
    }
    
    /* DataFrame styling */
    [data-testid="dataframe"] {
        border-radius: 0.75rem;
        border: 1px solid rgba(148, 163, 184, 0.16);
        overflow: hidden;
        background-color: #0f172a;
        color: #e2e8f0;
    }
    
    /* Divider styling */
    hr {
        border: none;
        border-top: 1px solid rgba(148, 163, 184, 0.16);
        margin: 2rem 0;
    }
    
    /* Loading spinner */
    .stSpinner > div > div {
        border-color: #2563eb;
    }
    
    /* Caption and small text */
    .stCaption {
        color: #94a3b8;
        font-size: 0.875rem;
    }
    
    /* Link styling */
    a {
        color: #60a5fa;
        text-decoration: none;
        font-weight: 500;
    }
    
    a:hover {
        text-decoration: underline;
    }
</style>
"""

def apply_custom_styling():
    """Apply custom CSS to Streamlit app"""
    import streamlit as st
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

def apply_plotly_theme(fig):
    """Apply professional theme to Plotly figure"""
    fig.update_layout(**PLOTLY_TEMPLATE["layout"])
    return fig


def get_sentiment_color(sentiment: str) -> str:
    """Get color for sentiment label"""
    sentiment_lower = str(sentiment).lower()
    if "positive" in sentiment_lower or "bullish" in sentiment_lower:
        return SENTIMENT_COLORS["positive"]
    elif "negative" in sentiment_lower or "bearish" in sentiment_lower:
        return SENTIMENT_COLORS["negative"]
    else:
        return SENTIMENT_COLORS["neutral"]


def get_chart_color_scale(n_colors: int = 7) -> list:
    """Get a color scale for multi-series charts"""
    return PLOTLY_TEMPLATE["layout"]["colorway"][:n_colors]