import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- PAGE SETTINGS ---
st.set_page_config(page_title="United Stats Lab", page_icon="⚽", layout="centered")

# Custom Premium CSS to style the background and remove white containers
st.markdown("""
    <style>
    .stApp { background-color: #0c100e; color: #ffffff; }
    div[data-testid="stSidebar"] { background-color: #060907; }
    h1, h2, h3 { color: #ffffff; font-family: 'Helvetica Neue', sans-serif; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🚀 Data Science Lab")
project_choice = st.sidebar.radio("Select a Project Dashboard:", ["⚽ United Player Analytics", "🏡 California Housing ML"])
st.sidebar.write("---")

# ==========================================
# PROJECT: UNITED PLAYER ANALYTICS
# ==========================================
if project_choice == "⚽ United Player Analytics":
    st.title("🛡️ Premier League Player Profiles")
    
    # Complete Roster Data Dictionary
    players_data = {
        "Bruno Fernandes": {"Pos": "Attacking midfielder", "Age": 31, "Mat": 35, "G": 9, "A": 18, "Skills": [85, 92, 45, 55, 80, 95, 88, 94], "Nation": "🇵🇹 PORTUGAL"},
        "Bryan Mbeumo": {"Pos": "Forward/Winger", "Age": 26, "Mat": 33, "G": 11, "A": 3, "Skills": [88, 75, 40, 35, 85, 78, 80, 72], "Nation": "🇨🇲 CAMEROON"},
        "Benjamin Šeško": {"Pos": "Striker", "Age": 23, "Mat": 30, "G": 11, "A": 1, "Skills": [92, 65, 30, 25, 82, 68, 85, 60], "Nation": "🇸🇮 SLOVENIA"},
        "Matheus Cunha": {"Pos": "Forward", "Age": 27, "Mat": 33, "G": 10, "A": 2, "Skills": [84, 80, 52, 48, 86, 82, 81, 78], "Nation": "🇧🇷 BRAZIL"},
        "Casemiro": {"Pos": "Defensive Midfielder", "Age": 34, "Mat": 34, "G": 9, "A": 2, "Skills": [65, 82, 88, 90, 70, 84, 76, 75], "Nation": "🇧🇷 BRAZIL"},
        "Kobbie Mainoo": {"Pos": "Midfielder", "Age": 21, "Mat": 28, "G": 1, "A": 2, "Skills": [55, 88, 78, 82, 88, 90, 84, 85], "Nation": "🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENGLAND"}
    }
    
    selected_player = st.selectbox("👤 Select Player to Generate Card:", list(players_data.keys()))
    p = players_data[selected_player]
    
    st.write("")
    
    # --- DESIGNING THE CARD HTML WRAPPER ---
    card_html = f"""
    <div style="background-color: #111613; border-radius: 20px; padding: 25px; border: 1px solid #1a221e; max-width: 480px; margin: auto; box-shadow: 0px 10px 30px rgba(0,0,0,0.5);">
        <!-- Top Metadata Label -->
        <div style="color: #ff2a3a; font-size: 11px; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 5px;">❤️ HEARTBEAT</div>
        
        <!-- Header Info Layout -->
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <div style="background-color: #ff2a3a; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: bold; margin-right: 15px; color: white;">
                {selected_player[0]}
            </div>
            <div>
                <div style="font-size: 22px; font-weight: bold; color: white; line-height: 1.2;">{selected_player}</div>
                <div style="color: #8a9990; font-size: 13px; margin-top: 2px;">{p['Pos']}</div>
                <div style="color: #55635a; font-size: 12px;">Manchester United · English Premier League · {p['Age']}y</div>
                <div style="color: white; font-size: 12px; margin-top: 4px; font-weight: bold;">{p['Nation']}</div>
            </div>
        </div>
        
        <!-- Main Stats Blocks Row -->
        <div style="color: #55635a; font-size: 11px; font-weight: bold; margin-bottom: 4px;">English Premier League 25/26</div>
        <div style="display: flex; gap: 30px; margin-bottom: 20px;">
            <div>
                <div style="font-size: 24px; font-weight: bold; color: white; line-height: 1;">{p['Mat']}</div>
                <div style="color: #55635a; font-size: 10px; font-weight: bold; text-transform: uppercase; margin-top: 3px;">Matches</div>
            </div>
            <div>
                <div style="font-size: 24px; font-weight: bold; color: #ff2a3a; line-height: 1;">{p['G']}</div>
                <div style="color: #55635a; font-size: 10px; font-weight: bold; text-transform: uppercase; margin-top: 3px;">Goals</div>
            </div>
            <div>
                <div style="font-size: 24px; font-weight: bold; color: #ff2a3a; line-height: 1;">{p['A']}</div>
                <div style="color: #55635a; font-size: 10px; font-weight: bold; text-transform: uppercase; margin-top: 3px;">Assists</div>
            </div>
        </div>
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)
    
    # --- RADAR CHART INSERTER ---
    categories = ['Box Threat', 'Involvement', 'Active Defence', 'Intelligent Defence', 'Progression', 'Passing Quality', 'Effectiveness', 'Providing Teammates']
    N = len(categories)
    
    values = p["Skills"]
    values_closed = values + values[:1]
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles_closed = angles + angles[:1]
    
    fig, ax = plt.subplots(figsize=(4.5, 4.5), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor('#111613') # Match Card Background Hex precisely
    ax.set_facecolor('#151c18')
    
    plt.xticks(angles, categories, color='#8a9990', size=8)
    
    ax.plot(angles_closed, values_closed, color='#ff2a3a', linewidth=2, linestyle='solid')
    ax.fill(angles_closed, values_closed, color='#ff2a3a', alpha=0.2)
    
    ax.spines['polar'].set_color('#222d27')
    ax.grid(color='#222d27', linestyle='-')
    ax.set_yticklabels([])
    ax.set_ylim(0, 100)
    
    # Anchor chart directly underneath card UI
    st.pyplot(fig)

# ==========================================
# PROJECT: CALIFORNIA HOUSING ML
# ==========================================
elif project_choice == "🏡 California Housing ML":
    st.title("🏡 California Housing Price Prediction")
    st.write("Your original housing model workspace.")

