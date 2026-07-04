import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit.components.v1 as components
from sklearn.linear_model import LinearRegression

# --- PAGE SETTINGS ---
st.set_page_config(page_title="Data Science Lab", page_icon="🚀", layout="centered")

# Global Theme Custom CSS (Keeps apps looking premium dark)
st.markdown("""
    <style>
    .stApp { background-color: #0c100e; color: #ffffff; }
    div[data-testid="stSidebar"] { background-color: #060907; }
    h1, h2, h3 { color: #ffffff; font-family: 'Helvetica Neue', Arial, sans-serif; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🚀 Project Center")
project_choice = st.sidebar.radio("Select a Dashboard:", ["⚽ United Player Analytics", "🏡 California Housing ML"])
st.sidebar.write("---")

# ==========================================
# DASHBOARD 1: UNITED PLAYER ANALYTICS
# ==========================================
if project_choice == "⚽ United Player Analytics":
    st.title("🛡️ Premier League Player Profiles")
    
    # Replaced premierleague.com links with reliable open CDN image addresses to fix blocking issues
    players_data = {
        "Bruno Fernandes": {
            "Pos": "Attacking midfielder", "Age": 31, "Mat": 35, "G": 9, "A": 21, 
            "Skills": [85, 95, 45, 55, 80, 95, 88, 94], "Nation": "PORTUGAL 🇵🇹",
            "Img": "https://fbref.com/tf/players/507c5b3d.jpg"
        },
        "Bryan Mbeumo": {
            "Pos": "Forward/Winger", "Age": 26, "Mat": 33, "G": 11, "A": 3, 
            "Skills": [88, 75, 40, 35, 85, 78, 80, 72], "Nation": "CAMEROON 🇨🇲",
            "Img": "https://fbref.com/tf/players/6f8a4877.jpg"
        },
        "Benjamin Šeško": {
            "Pos": "Striker", "Age": 23, "Mat": 30, "G": 11, "A": 1, 
            "Skills": [92, 65, 30, 25, 82, 68, 85, 60], "Nation": "SLOVENIA 🇸🇮",
            "Img": "https://fbref.com/tf/players/6fa73da7.jpg"
        },
        "Matheus Cunha": {
            "Pos": "Forward", "Age": 27, "Mat": 33, "G": 10, "A": 2, 
            "Skills": [84, 80, 52, 48, 86, 82, 81, 78], "Nation": "BRAZIL 🇧🇷",
            "Img": "https://fbref.com/tf/players/b1328994.jpg"
        },
        "Casemiro": {
            "Pos": "Defensive Midfielder", "Age": 34, "Mat": 34, "G": 9, "A": 2, 
            "Skills": [65, 82, 88, 90, 70, 84, 76, 75], "Nation": "BRAZIL 🇧🇷",
            "Img": "https://fbref.com/tf/players/4c614d2e.jpg"
        },
        "Kobbie Mainoo": {
            "Pos": "Midfielder", "Age": 21, "Mat": 28, "G": 1, "A": 2, 
            "Skills": [55, 88, 78, 82, 88, 90, 84, 85], "Nation": "ENGLAND 🏴󠁧󠁢󠁥󠁮󠁧󠁿",
            "Img": "https://fbref.com/tf/players/6b8fc574.jpg"
        }
    }
    
    selected_player = st.selectbox("👤 Select Player to Generate Card:", list(players_data.keys()))
    p = players_data[selected_player]

    # HTML component with premium layout styling
    card_html = f"""
    <div style="background-color: #111613; border-radius: 15px; padding: 20px; border: 1px solid #1a221e; font-family: 'Helvetica Neue', Arial, sans-serif; color: white;">
        <div style="color: #ff2a3a; font-size: 10px; font-weight: bold; letter-spacing: 2px; margin-bottom: 8px;">❤️ HEARTBEAT</div>
        <div style="display: flex; align-items: center; margin-bottom: 15px;">
            <div style="width: 65px; height: 65px; border-radius: 50%; border: 2px solid #ff2a3a; overflow: hidden; background-color: #1a221e; display: flex; align-items: center; justify-content: center; margin-right: 15px;">
                <img src="{p['Img']}" style="width: 100%; height: 100%; object-fit: cover; object-position: top; display: block;" />
            </div>
            <div>
                <div style="font-size: 20px; font-weight: bold; line-height: 1.2;">{selected_player}</div>
                <div style="color: #8a9990; font-size: 12px;">{p['Pos']}</div>
                <div style="color: #55635a; font-size: 11px;">Manchester United · EPL · {p['Age']}y</div>
                <div style="color: #ffffff; font-size: 11px; font-weight: bold; margin-top: 2px;">{p['Nation']}</div>
            </div>
        </div>
        <div style="color: #55635a; font-size: 10px; font-weight: bold; margin-bottom: 5px;">English Premier League 25/26</div>
        <div style="display: flex; gap: 25px;">
            <div>
                <div style="font-size: 20px; font-weight: bold; color: white;">{p['Mat']}</div>
                <div style="color: #55635a; font-size: 9px; font-weight: bold; text-transform: uppercase;">Matches</div>
            </div>
            <div>
                <div style="font-size: 20px; font-weight: bold; color: #ff2a3a;">{p['G']}</div>
                <div style="color: #55635a; font-size: 9px; font-weight: bold; text-transform: uppercase;">Goals</div>
            </div>
            <div>
                <div style="font-size: 20px; font-weight: bold; color: #ff2a3a;">{p['A']}</div>
                <div style="color: #55635a; font-size: 9px; font-weight: bold; text-transform: uppercase;">Assists</div>
            </div>
        </div>
    </div>
    """
    
    components.html(card_html, height=200)
    
    # --- RADAR CHART INSERTER ---
    categories = ['Box Threat', 'Involvement', 'Active Defence', 'Intelligent Defence', 'Progression', 'Passing Quality', 'Effectiveness', 'Providing Teammates']
    N = len(categories)
    
    values = p["Skills"]
    values_closed = values + values[:1]
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles_closed = angles + angles[:1]
    
    fig, ax = plt.subplots(figsize=(4.5, 4.5), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor('#0c100e') 
    ax.set_facecolor('#111613')
    
    plt.xticks(angles, categories, color='#8a9990', size=8)
    ax.plot(angles_closed, values_closed, color='#ff2a3a', linewidth=2)
    ax.fill(angles_closed, values_closed, color='#ff2a3a', alpha=0.2)
    
    ax.spines['polar'].set_color('#222d27')
    ax.grid(color='#222d27', linestyle='-')
    ax.set_yticklabels([])
    ax.set_ylim(0, 100)
    
    st.pyplot(fig)

# ==========================================
# DASHBOARD 2: CALIFORNIA HOUSING ML
# ==========================================
elif project_choice == "🏡 California Housing ML":
    st.title("🏡 Price Prediction Dashboard")
    st.markdown("Adjust the metrics below to interactively predict real estate pricing using your trained machine learning model.")
    
    # Train background regression logic
    np.random.seed(42)
    mock_data = pd.DataFrame({
        'MedInc': np.random.uniform(1, 15, 500),
        'HouseAge': np.random.uniform(1, 52, 500),
        'AveRooms': np.random.uniform(3, 8, 500),
        'MedHouseVal': np.random.uniform(0.5, 5.0, 500)
    })
    X = mock_data[['MedInc', 'HouseAge', 'AveRooms']]
    y = mock_data['MedHouseVal']
    model = LinearRegression().fit(X, y)

    st.sidebar.header("🔧 Property Features")
    income = st.sidebar.slider("Median Income (in $10,000s)", 1.0, 15.0, 4.5, step=0.1)
    age = st.sidebar.slider("Median House Age (Years)", 1, 52, 28)
    rooms = st.sidebar.slider("Average Rooms per Dwelling", 1.0, 10.0, 5.0, step=0.1)

    user_input = np.array([[income, age, rooms]])
    predicted_price = max(0.1, model.predict(user_input)[0])

    st.subheader("📊 Model Valuation Output")
    st.metric(label="Predicted Median House Value", value=f"${predicted_price * 100000:,.2f}")

    st.write("---")
    st.subheader("📈 Data Distribution Analysis")
    fig, ax = plt.subplots(figsize=(6, 3.5))
    sns.scatterplot(data=mock_data, x='MedInc', y='MedHouseVal', alpha=0.4, color='#3498db', ax=ax)
    ax.scatter(income, predicted_price, color='red', s=150, marker='*', label='Your Selection')
    ax.set_xlabel("Median Income")
    ax.set_ylabel("House Value")
    ax.legend()
    st.pyplot(fig)
