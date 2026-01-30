import streamlit as st
from groq import Groq

# ------------------ OSNOVNI PODATKI O STRANI ------------------

OPIS_STRANI = """
Brewed Awakenings je prodajalna za kavo, ki ponuja širok izbor kofeinskih in brezkofeinskih kav,
različne aromatične mešanice ter kavna zrna.

HOME PAGE:
Naši okusi prinašajo edinstveno doživetje vsake skodelice – od bogatih, intenzivnih kav do nežnih,
aromatičnih mešanic. Cilj Brewed Awakenings je začeti tvoj dan z navdihom in skrbno izbranimi kavami,
ki popestrijo vsak trenutek. Ponujamo klasične napitke in gourmet mešanice.

PONUDBA:
• Klasična črna kava – 5.99€
• Kava z vanilijevo aromo – 6.99€
• Kava z pridihom kakava – 6.99€
• Kava z okusom kokosa – 6.99€

KAVNA ZRNA:
• Polnočni Amber – najbolj priljubljena mešanica, bogata, polna in aromatična.
  Cena: od 10.99€ dalje.

KONTAKT:
Telefon: 111-111-111
Email: brewed.awakenings@gmail.com
Delovni čas: Pon–Pet 9:00–16:00, Sob–Ned zaprto
Naslov: Preradovičeva ulica 33, 2000 Maribor
"""

KLJUCNE_BESEDE = [
    "kava", "kave", "kavno", "kavna", "brewed awakenings", "ponudba",
    "cena", "cene", "okus", "okusi", "zrna", "kavna zrna", "polnočni amber",
    "kontakt", "delovni čas", "naslov", "maribor", "prodajalna",
    "kofeinska", "brezkofeinska", "ledena kava", "home page"
]

def je_relevantno(vprasanje: str) -> bool:
    vprasanje = vprasanje.lower()
    return any(beseda in vprasanje for beseda in KLJUCNE_BESEDE)


# ------------------ STREAMLIT NASTAVITVE ------------------

st.set_page_config(
    page_title="Brewed Awakenings Chatbot",
    layout="centered"
)

# ------------------ CSS — COFFEE FOAM GRADIENT ------------------

st.markdown("""
<style>

/* Ozadje */
body, .stApp {
    background-color: #fff8ef !important; /* latte cream */
    color: #3a2418 !important;
    font-family: "Inter", system-ui, sans-serif !important;
}

/* Glavni container */
.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
    max-width: 800px !important;
}

/* ASSISTANT oblaček – coffee foam gradient */
div[data-testid="stChatMessage"]:not([data-testid="stChatMessageUser"]) {
    background: radial-gradient(circle at top left,
        #f7efe6 0%,
        #e8d6c3 40%,
        #d2b89a 100%
    ) !important; /* cappuccino foam */
    border: 2px solid #a06b3b !important;
    border-radius: 20px !important;
    padding: 16px !important;
    margin-bottom: 14px !important;
}

/* USER oblaček – dark roast gradient */
div[data-testid="stChatMessage"][data-testid="stChatMessageUser"] {
    background: linear-gradient(135deg,
        #8b5a2b 0%,
        #6b3f1f 50%,
        #4a2a14 100%
    ) !important; /* espresso swirl */
    border: 2px solid #5c3a1a !important;
    border-radius: 20px !important;
    padding: 16px !important;
    margin-bottom: 14px !important;
}

/* BEL, BOLD TEKST v oblačkih */
div[data-testid="stChatMessage"] p {
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 16px !important;
}

/* Avatar */
div[data-testid="stChatMessageAvatar"] {
    background-color: #5c3a1a !important; /* dark roast */
    color: white !important;
    border-radius: 50% !important;
    width: 32px !important;
    height: 32px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-weight: bold !important;
    font-size: 16px !important;
}

/* INPUT – espresso + bel tekst */
.stChatInput > div > div > textarea {
    background-color: #3a2418 !important;
    color: #ffffff !important;
    border-radius: 12px !important;
    border: 2px solid #8b5a2b !important;
    padding: 12px !important;
    font-size: 16px !important;
}

/* Placeholder – latte beige */
.stChatInput > div > div > textarea::placeholder {
    color: #e3d2c3 !important;
}

/* Gumb */
.stButton > button {
    background-color: #8b5a2b !important;
    color: #ffffff !important;
    border-radius: 12px !important;
    border: none !important;
    padding: 10px 20px !important;
    font-size: 16px !important;
}

</style>
""", unsafe_allow_html=True)

# ------------------ UI ------------------

st.title("Brewed Awakenings – klepetalnik o kavi")
st.write(
    "Postavi mi vprašanje o naši kavi, ponudbi ali kontaktu. "
    "Če vprašanje ni povezano s Brewed Awakenings, ti bom to vljudno povedal."
)

# ------------------ SPOMIN ------------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "Ti si asistent za spletno stran Brewed Awakenings. "
                "Odgovarjaš izključno v slovenščini in samo na vprašanja, "
                "ki so povezana s kavo, ponudbo, kavnimi zrni Polnočni Amber, "
                "okusi, cenami, delovnim časom, kontaktom ali lokacijo Brewed Awakenings. "
                "Če vprašanje ni povezano s tem, odgovori: "
                "'Za to področje žal nimam informacij. Lahko pa ti povem več o Brewed Awakenings.' "
                "Tukaj so informacije o strani: " + OPIS_STRANI
            )
        }
    ]

for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ------------------ GROQ ------------------

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ------------------ VNOS ------------------

vnos = st.chat_input("Vprašaj me kaj o Brewed Awakenings...")

if vnos:
    with st.chat_message("user"):
        st.markdown(vnos)

    if not je_relevantno(vnos):
        odgovor_text = (
            "Za to področje žal nimam informacij. "
            "Lahko pa ti povem več o Brewed Awakenings."
        )
        with st.chat_message("assistant"):
            st.markdown(odgovor_text)

        st.session_state.messages.append({"role": "user", "content": vnos})
        st.session_state.messages.append({"role": "assistant", "content": odgovor_text})

    else:
        st.session_state.messages.append({"role": "user", "content": vnos})

        odgovor = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages
        )

        ai_text = odgovor.choices[0].message.content

        with st.chat_message("assistant"):
            st.markdown(ai_text)

        st.session_state.messages.append({"role": "assistant", "content": ai_text})
