import streamlit as st

```python
import streamlit as st
from groq as st
from groq import Groq

# ---------- import Groq

# ---------- OSNOVNE INFO O STR OSNOVNE INFO O STRANI ----------

ANI ----------

OPIS_STRANI = """
OPIS_STRANI = """
Brewed AwakeningsBrewed Awakenings je prodajalna za je prodajalna za kavo, ki ponuja kavo, ki ponuja širok izbor kof širok izbor kofeinskih in brezkofeinskih kav,
razeinskih in brezkofeinskih kav,
različne aromatične mešanice ter kavna zrna.

HOME PAGElične aromatične mešanice ter kavna zrna.

HOME PAGE:
Naši okusi prina:
Naši okusi prinašajo edinstveno došajo edinstveno doživetje vsake skživetje vsake skodelice – od bogatih, intenzivnihodelice – od bogatih, intenzivnih kav do nežnih,
aromatičnih mešanic. Cilj Brewed Aw kav do nežnih,
aromatičnih mešanic. Cilj Brewed Awakenings je začetiakenings je začeti tvoj dan z navd tvoj dan z navdihom in skrbno izbranimi kavami,
ki popestrijo vsak trenutek. Ponujihom in skrbno izbranimi kavami,
ki popestrijo vsak trenutek. Ponujamo klasične napitke in gourmet mešanice.

PONUDBA:
• Klasična črnaamo klasične napitke in gourmet mešanice.

PONUDBA:
• Klasična črna kava – 5.99€
• K kava – 5.99€
• Kava z vanilijevo aromo – 6.99€
• Kava z pridihomava z vanilijevo aromo – 6.99€
• Kava z pridihom kakava – 6.99€
• Kava z okusom kok kakava – 6.99€
• Kava z okusom kokosa – 6.99€

Kavnaosa – 6.99€

Kavna zrna:
• Polnočni Amber – najbolj priljubljena me zrna:
• Polnočni Amber – najbolj priljubljena mešanica, bogata, polna in aromatičnašanica, bogata, polna in aromatična.
  Cena: od 10.99€ dalje.

KONTAKT:
Telefon: 111.
  Cena: od 10.99€ dalje.

KONTAKT:
Telefon: 111-111-111
Email: brewed.awakenings@gmail.com
Delovni čas: Pon–Pet 9:00–16-111-111
Email: brewed.awakenings@gmail.com
Delovni čas: Pon–Pet 9:00–16:00, Sob–Ned zapr:00, Sob–Ned zaprto
Naslov: Preradto
Naslov: Preradovičeva ulica 33ovičeva ulica 33, 2000 Maribor
"""

, 2000 Maribor
"""

KLJUCNE_BESEDE = [
    "kava", "KLJUCNE_BESEDE = [
    "kava", "kave", "kavno", "kave", "kavno", "kavna", "brewed awakenings", "ponudba",
kavna", "brewed awakenings", "ponudba",
    "cena", "cene    "cena", "cene", "okus", "okusi", "okus", "okusi", "zrna", "kavna", "zrna", "kavna zrna", "polnočni zrna", "polnočni amber",
    "kontakt amber",
    "kontakt", "delovni čas", "naslov", "maribor", "prodajalna",", "delovni čas", "naslov", "maribor", "prodajalna", "kofeinska",
    "brezkofeinska", "ledena kava", " "kofeinska",
    "brezkofeinska", "ledena kava", "ledene kave", "homeledene kave", "home page", "ponudba page", "ponudba"
]


def je_relevant"
]


def je_relevantno(vprasanje: strno(vprasanje: str) -> bool:
    vprasanje = vprasanje.lower()
    return any(beseda in vprasanje for) -> bool:
    vprasanje = vprasanje.lower()
    return any(beseda in vprasanje for beseda in KLJUCNE_BESEDE)


# ---------- STREAMLIT NASTAV beseda in KLJUCNE_BESEDE)


# ---------- STREAMLIT NASTAVITVE ----------

ITVE ----------

st.set_page_configst.set_page_config(
    page_title(
    page_title="Brewed Awakenings Chatbot",
    page="Brewed Awakenings Chatbot",
    page_icon="☕",
    layout_icon="☕",
    layout="centered"
)

#="centered"
)

# Temno rjav dizajn Temno rjav dizajn
st.markdown(
   
st.markdown(
    """
    <style> """
    <style>
    body {
       
    body {
        background-color background-color: #2b1b12;
       : #2b1b12;
        color: #f5f0e8;
 color: #f5f0e8;
        font-family        font-family: system-ui, -apple: system-ui, -apple-system, BlinkMac-system, BlinkMacSystemFont, "SegoeSystemFont, "Segoe UI", sans-serif UI", sans-serif;
    }
    .stApp;
    }
    .stApp {
        background {
        background-color: #2b1b12;
-color: #2b1b12;
    }
    .block-container {
           }
    .block-container {
        padding-top: 1. padding-top: 1.5rem;
        padding-bottom: 1.5rem;
5rem;
        padding-bottom: 1.5rem;
        max-width        max-width: 800px;
    }
   : 800px;
    }
    .stChatMessage {
        background .stChatMessage {
        background-color: #3a2418 !-color: #3a2418 !important;
       important;
        border-radius: 12px !important;
 border-radius: 12px !important;
    }
    .stText    }
    .stTextInput > div > div > input,
    .stInput > div > div > input,
    .stChatInput > div >ChatInput > div > div > textarea {
 div > textarea {
        background        background-color: #3a2418 !important;
       -color: #3a2418 !important;
        color: #f5f0e8 !important;
        border-radius:  color: #f5f0e8 !12px !important;
important;
        border-radius: 12px !important;
        border:         border: 1px solid #8b5a21px solid #8b5a2b !important;
   b !important;
    }
    .stButton }
    .stButton>button {
       >button {
        background-color: #8b5a2b !important;
        color: background-color: #8b5a2b !important;
        color: #f5f0e8 !important;
        border #f5f0e8 !important;
        border-radius: 12px !important;
        border-radius: 12px !important;
        border: none;
    }
   : none;
    }
    </style>
    "" </style>
    """,
    unsafe_allow",
    unsafe_allow_html=True
)

st_html=True
)

st.title("☕ Brewed Awakenings – kle.title("☕ Brewed Awakenings – klepetalnik o kavi")

petalnik o kavi")

st.write(
    "Postst.write(
    "Postavi mi vprašanjeavi mi vprašanje o naši kavi, ponudbi ali kontaktu. "
    "Če vprašanje ni povezano z Brewed Awakenings, ti bom to vljudno povedal."
)

# ---------- SPOMIN V SEJI ----------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "Ti si asistent za spletno stran Brewed Awakenings. "
                "Odgovarjaš izklju_state.messages = [
        {
            "role": "system",
            "content": (
                "Ti si asistent za spletno stran Brewed Awakenings. "
                "Odgovarjaš izključno v slovenščinično v slovenščini in samo na vpraš in samo na vprašanja, "
               anja, "
                "ki so povezana s kavo, ponudbo "ki so povezana s kavo, ponudbo, kavnim zrnom Pol, kavnim zrnom Polnočni Amber, "
               nočni Amber, "
                "okusi, cenami, "okusi, cenami, delovnim časom, delovnim časom, kontaktom ali lok kontaktom ali lokacijo Brewed Awakenings. "
                "Če vprašanje ni povezano s tem,acijo Brewed Awakenings. "
                "Če vprašanje ni povezano s tem, odgovori: "
                "'Za to področje žal nimam informacij. Lahko pa ti pov odgovori: "
                "'Za to področje žal nimam informacij. Lahko pa ti povem več o Brewed Awakenings.' "
               em več o Brewed Awakenings.' "
                "Tukaj so informacije "Tukaj so informacije o strani: " + OP o strani: " + OPIS_STRANI
            )
        }
   IS_STRANI
            )
        }
    ]

# Prikaz zgodovine pogovora
for ]

# Prikaz zgodovine pogovora
for msg in st.session_state.messages:
    if msg["role msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
["content"])
    elif msg["role"]        with st.chat_message("assistant"):
            st == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

# ----------.markdown(msg["content"])

# ---------- GROQ KLIENT ---------- GROQ KLIENT ----------

client = Groq(api

client = Groq(api_key=st.secrets["_key=st.secrets["GROQ_API_KEY"])

# ---------- VNOSGROQ_API_KEY"])

# ---------- VNOS UPORABNIKA ---------- UPORABNIKA ----------

vnos = st.chat_input("Vprašaj me

vnos = st.chat_input("Vprašaj me kaj o Brewed Aw kaj o Brewed Awakenings...")

ifakenings...")

if vnos:
    # naj vnos:
    # najprej prikažemo uporabnikov vnos
    withprej prikažemo uporabnikov vnos
    with st.chat_message("user"):
        st.markdown(vnos)

    # preverimo st.chat_message("user"):
        st.markdown(vnos, ali je vprašanje relevantno
    if)

    # preverimo, ali je vprašanje relevantno
    if not je_relevantno(vnos):
        not je_relevantno(vnos):
        odgovor_text = "Za to področje žal nimam informacij odgovor_text = "Za to področje žal nimam informacij. Lahko pa ti povem več o Brewed Awakenings."
       . Lahko pa ti povem več o Brewed Aw with st.chat_message("assistant"):
            st.markdown(odgovor_text)
       akenings."
        with st.chat_message("assistant"):
            st.markdown(odgovor_text)
        st.session_state.messages.append st.session_state.messages.append({"role": "user", "content": vnos})
        st.session({"role": "user", "content": vnos})
        st.session_state.messages.append({"role": "assistant_state.messages.append({"role": "assistant", "content": odgovor", "content": odgovor_text})
    else_text})
    else:
        # dodamo:
        # dodamo vnos v zgodovino vnos v zgodovino za model
        za model
        st.session_state st.session_state.messages.append.messages.append({"role": "user",({"role": "user", "content": vnos})

        # klic "content": vnos na Groq API
       })

        # klic odgovor = client.chat.completions.create(
            model="llama-3. na Groq API
        odgovor = client.chat.completions3-70b-versatile",
            messages=st.session_state.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages
        )

        ai_text = odgovor.choices.messages
       [0].message.content

        # prikaz odgovora
        )

        ai_text = odgovor.choices[0].message.content

        # prikaz odgovora
        with st.chat_message("assistant"):
            with st.chat_message st.markdown(ai_text)

        # shranimo odgovor v spomin
        st.session_state.messages.append({"role": "assistant", "content": ai_text})
