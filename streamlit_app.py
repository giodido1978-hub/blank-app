import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start buildingimport streamlit as st
import pandas as pd
import datetime

# Configurazione della pagina per adattarla al meglio agli schermi mobili (iPhone)
st.set_page_config(
    page_title="Betting AI Dashboard",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Stile CSS personalizzato per renderla una dashboard moderna ed elegante
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .metric-card {
        background-color: #1f2937;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #374151;
        text-align: center;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Titolo dell'applicazione
st.title("⚽ Betting AI Pro Dashboard")
st.markdown("### Sistema Autonomo di Pronostici & Bankroll Management")

# Inizializzazione dello Storico Scommesse nella memoria della sessione (Mockup iniziale)
if 'storico_scommesse' not in st.session_state:
    st.session_state.storico_scommesse = pd.DataFrame([
        {
            "Data": "2026-10-06",
            "Partita": "Inter vs Juventus",
            "Campionato": "Serie A",
            "Segno": "Gol",
            "Quota": 1.90,
            "Stake (€)": 10.0,
            "Probabilità %": 78,
            "Esito": "Vinta"
        },
        {
            "Data": "2026-10-07",
            "Partita": "Real Madrid vs Barcellona",
            "Campionato": "Liga",
            "Segno": "1",
            "Quota": 2.05,
            "Stake (€)": 10.0,
            "Probabilità %": 76,
            "Esito": "Persa"
        }
    ])

# Menu laterale di navigazione
menu = st.sidebar.selectbox("Navigazione", ["📊 Pronostici del Giorno", "📜 Storico & Bankroll", "⚙️ Configura Parametri AI"])

# ==========================================
# SEZIONE 1: PRONOSTICI DEL GIORNO
# ==========================================
if menu == "📊 Pronostici del Giorno":
    st.subheader("🎯 Match Selezionati dall'Algoritmo (Filtri Rigidi Attivi)")
    st.info("ℹ️ Vengono mostrate solo le partite con Quota ≥ 1.85, Probabilità ≥ 75% e mercati ristretti a [1, 2, Gol].")

    # Simulazione dati in arrivo dall'API e analizzati dall'IA
    match_del_giorno = [
        {
            "partita": "Arsenal vs Chelsea",
            "campionato": "Premier League (Inghilterra)",
            "segno": "Gol",
            "quota": 1.92,
            "probabilita": 79,
            "stanchezza": "Bassa (7 giorni di riposo)",
            "emotivita": "Alta (Scontro diretto per il vertice)",
            "spogliatoio": "Ottimo clima, gruppo coeso",
            "classifica": "3° posto (Anno scorso 2°)",
            "arbitro": "Michael Oliver (Media cartellini bilanciata)"
        },
        {
            "partita": "Bayern Monaco vs RB Lipsia",
            "campionato": "Bundesliga (Germania)",
            "segno": "1",
            "quota": 1.88,
            "probabilita": 82,
            "stanchezza": "Media (impegno infrasettimanale gestito)",
            "emotivita": "Fattore campo rovente (Giocano in casa)",
            "spogliatoio": "Umorismo alto dopo l'ultima vittoria",
            "classifica": "1° posto (Anno scorso 1°)",
            "arbitro": "Felix Zwayer (Favorevole ai falli di reazione casalinghi)"
        }
    ]

    for m in match_del_giorno:
        with st.container():
            col1, col2, col3 = st.columns([3, 2, 2])
            with col1:
                st.markdown(f"### **{m['partita']}**")
                st.caption(f"🌍 {m['campionato']}")
            with col2:
                st.markdown(f"**Segno Consigliato:** `{m['segno']}`")
                st.markdown(f"**Quota Sisal:** `{m['quota']}`")
            with col3:
                st.markdown(f"**Probabilità AI:** `{m['probabilita']}%`")
                # Pulsante per registrare direttamente la giocata nello storico
                if st.button(f"Registra Giocata", key=m['partita']):
                    nuova_riga = {
                        "Data": str(datetime.date.today()),
                        "Partita": m['partita'],
                        "Campionato": m['campionato'],
                        "Segno": m['segno'],
                        "Quota": m['quota'],
                        "Stake (€)": 10.0,
                        "Probabilità %": m['probabilita'],
                        "Esito": "In Corso"
                    }
                    st.session_state.storico_scommesse = pd.concat([st.session_state.storico_scommesse, pd.DataFrame([nuova_riga])], ignore_index=True)
                    st.success(f"Giocata salvata nello storico!")

            # Espandibile con tutti i dettagli qualitativi e comportamentali
            with st.expander("🔍 Analisi dettagliata dei parametri IA"):
                st.write(f"- **Carica Emotiva:** {m['emotivita']}")
                st.write(f"- **Stanchezza & Fisicità:** {m['stanchezza']}")
                st.write(f"- **Umorismo & Spogliatoio:** {m['spogliatoio']}")
                st.write(f"- **Obiettivo e Classifica Comparata:** {m['classifica']}")
                st.write(f"- **Analisi Arbitro:** {m['arbitro']}")
            st.divider()

# ==========================================
# SEZIONE 2: STORICO & BANKROLL
# ==========================================
elif menu == "📜 Storico & Bankroll":
    st.subheader("💰 Gestione Cassa & Storico Scommesse")

    df = st.session_state.storico_scommesse

    # Calcoli finanziari
    if not df.empty:
        vinte = df[df["Esito"] == "Vinta"]
        perse = df[df["Esito"] == "Persa"]
        
        totale_puntato = df[df["Esito"].isin(["Vinta", "Persa"])]["Stake (€)"].sum()
        totale_incassato = (vinte["Stake (€)"] * vinte["Quota"]).sum()
        utile_netto = totale_incassato - totale_puntato

        # Metriche principali in alto (ottime anche per iPhone)
        c1, c2, c3 = st.columns(3)
        c1.metric("Puntata Totale", f"€ {totale_puntato:.2f}")
        c2.metric("Utile / Perdita Netta", f"€ {utile_netto:.2f}", delta=f"{utile_netto:.2f}")
        c3.metric("Win Rate", f"{(len(vinte)/max(1, len(vinte)+len(perse))*100):.1f}%")

    st.markdown("---")
    st.markdown("### Elenco Giocate Registrate")
    
    # Tabella interattiva dello storico
    st.dataframe(df, use_container_width=True)

    # Modifica esito scommessa
    st.markdown("### Aggiorna Esito Partita")
    with st.form("aggiorna_esito"):
        riga_selezionata = st.selectbox("Seleziona partita da aggiornare", df["Partita"].tolist() if not df.empty else ["Nessuna"])
        nuovo_esito = st.selectbox("Esito Finale", ["In Corso", "Vinta", "Persa"])
        submit_esito = st.form_submit_button("Aggiorna Stato")
        
        if submit_esito and not df.empty:
            st.session_state.storico_scommesse.loc[st.session_state.storico_scommesse["Partita"] == riga_selezionata, "Esito"] = nuovo_esito
            st.rerun()

# ==========================================
# SEZIONE 3: CONFIGURAZIONE PARAMETRI AI
# ==========================================
elif menu == "⚙️ Configura Parametri AI":
    st.subheader("⚙️ Regole Rigide dell'Algoritmo")
    
    with st.form("config_form"):
        st.slider("Soglia Minima di Probabilità (%)", min_value=50, max_value=95, value=75)
        st.slider("Quota Minima", min_value=1.50, max_value=3.00, value=1.85)
        st.multiselect("Mercati Ammessi (Bloccati)", ["1", "2", "Gol"], default=["1", "2", "Gol"])
        st.text_area("Criteri Qualitativi Attivi (Stanchezza, Umorismo, Arbitro, Carica Emotiva)", 
                     value="Monitoraggio costante di stanchezza fisica, giorni di recupero, clima dello spogliatoio, motivazioni di classifica comparata rispetto all'anno precedente e stile dell'arbitro.")
        
        salva = st.form_submit_button("Salva Configurazione")
        if salva:
            st.success("Parametri aggiornati con successo per l'elaborazione globale!")
