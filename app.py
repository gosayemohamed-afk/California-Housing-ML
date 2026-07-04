import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🚀 Data Science Lab")
project_choice = st.sidebar.radio("Select a Project Dashboard:", ["🏡 California Housing ML", "⚽ United Player Analytics"])

st.sidebar.write("---")

# ==========================================
# PROJECT 1: CALIFORNIA HOUSING
# ==========================================
if project_choice == "🏡 California Housing ML":
    st.title("🏡 California Housing Price Prediction Dashboard")
    st.markdown("Adjust the metrics below to interactively predict real estate pricing using your trained machine learning model.")
    
    # Simple Multi-variable Model Mock
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

    # Sidebar inputs
    st.sidebar.header("🔧 Adjust Property Features")
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

# ==========================================
# PROJECT 2: UNITED PLAYER ANALYTICS
# ==========================================
elif project_choice == "⚽ United Player Analytics":
    st.title("🔴 Manchester United Performance Analytics")
    st.markdown("Explore player efficiency metrics and dataset visualization charts interactively.")
    
    raw_data = {
        "Player": ["Luke Shaw", "Bruno Fernandes", "Diogo Dalot", "Casemiro", "Bryan Mbeumo", "Matheus Cunha", "Amad Diallo", "Leny Yoro", "Benjamin Šeško", "Kobbie Mainoo", "Patrick Dorgu", "Mason Mount", "Harry Maguire", "Noussair Mazraoui", "Lisandro Martínez", "Ayden Heaven", "Matthijs de Ligt", "Manuel Ugarte"],
        "Position": ["DF", "MF", "DF", "MF", "FW", "FW", "MF", "DF", "FW", "MF", "MF", "MF", "DF", "DF", "DF", "DF", "DF", "MF"],
        "Matches_Played": [38, 35, 34, 34, 33, 33, 32, 32, 30, 28, 26, 23, 23, 20, 18, 17, 13, 22],
        "Minutes": [3219, 3063, 2614, 2571, 2609, 2494, 2341, 1740, 1643, 1662, 1449, 1017, 1653, 985, 1233, 924, 1170, 1010],
        "Goals": [1, 9, 1, 9, 11, 10, 2, 0, 11, 1, 4, 3, 1, 0, 0, 0, 1, 0],
        "Assists": [1, 21, 3, 2, 3, 2, 3, 0, 1, 2, 4, 0, 2, 0, 0, 1, 0, 0]
    }
    df = pd.DataFrame(raw_data)
    df['G_A'] = df['Goals'] + df['Assists']
    df['G_A_per_90'] = (df['G_A'] / (df['Minutes'] / 90)).round(2)

    view_option = st.radio("🔎 Choose Analytics View:", ["Attacker Efficiency Chart", "Full Roster Data Explorer"])

    if view_option == "Attacker Efficiency Chart":
        st.subheader("🔥 Top 5 Most Efficient Attackers (G+A per 90)")
        reliable_players = df[df['Minutes'] > 500]
        top_5 = reliable_players.sort_values(by='G_A_per_90', ascending=False).head(5)
        
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(8, 4.5))
        sns.barplot(
            x='G_A_per_90', y='Player', data=top_5, 
            hue='Player', legend=False, palette='Reds_r', ax=ax
        )
        ax.set_title("United Attacker Efficiency", fontsize=12, pad=10)
        ax.set_xlabel("Goals + Assists per 90 Minutes")
        ax.set_ylabel("")
        sns.despine(left=True, bottom=True)
        ax.grid(axis='x', linestyle='--', alpha=0.3)
        
        for index, value in enumerate(top_5['G_A_per_90']):
            ax.text(value + 0.01, index, f"{value}", va='center', fontweight='bold')
            
        st.pyplot(fig)

    elif view_option == "Full Roster Data Explorer":
        st.subheader("📋 Outfield Player Metrics Explorer")
        position_filter = st.multiselect("Filter by Position:", options=df['Position'].unique(), default=df['Position'].unique())
        filtered_df = df[df['Position'].isin(position_filter)]
        st.dataframe(filtered_df.sort_values(by="Minutes", ascending=False), use_container_width=True)

