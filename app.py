import streamlit as st

# --------------------------------------------------
# CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Study Abroad Assistant",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# STYLE
# --------------------------------------------------

st.markdown("""
<style>
.main-title{
    font-size:42px;
    font-weight:bold;
}
.card{
    padding:20px;
    border-radius:10px;
    border:1px solid #ddd;
    margin-bottom:15px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<p class="main-title">🎓 AI Study Abroad Assistant</p>',
    unsafe_allow_html=True
)

st.write(
    "Trouvez le pays d'étude le plus adapté à votre profil."
)

# --------------------------------------------------
# TABS
# --------------------------------------------------

tab1, tab2, tab3 = st.tabs(
    [
        "👤 Profil",
        "🌍 Recommandation",
        "📄 Lettre Motivation"
    ]
)

# --------------------------------------------------
# TAB 1
# --------------------------------------------------

with tab1:

    st.subheader("Informations")

    age = st.number_input(
        "Âge",
        min_value=16,
        max_value=60,
        value=25
    )

    diploma = st.selectbox(
        "Dernier diplôme",
        [
            "Baccalauréat",
            "Licence",
            "Master",
            "Doctorat"
        ]
    )

    average = st.number_input(
        "Moyenne",
        min_value=0.0,
        max_value=20.0,
        value=12.0
    )

    budget = st.number_input(
        "Budget disponible (€)",
        min_value=0,
        value=5000
    )

    country = st.text_input(
        "Pays actuel"
    )

# --------------------------------------------------
# TAB 2
# --------------------------------------------------

with tab2:

    if st.button("Obtenir une recommandation"):

        recommendation = []

        if budget < 5000:
            recommendation.append(
                "🇫🇷 France (universités publiques)"
            )
            recommendation.append(
                "🇧🇪 Belgique"
            )

        elif budget < 15000:
            recommendation.append(
                "🇨🇦 Canada"
            )
            recommendation.append(
                "🇱🇺 Luxembourg"
            )

        else:
            recommendation.append(
                "🇨🇦 Canada"
            )
            recommendation.append(
                "🇬🇧 Royaume-Uni"
            )

        st.success("Résultat")

        for item in recommendation:
            st.write(item)

        st.info(
            f"""
            Profil analysé :

            • Diplôme : {diploma}

            • Moyenne : {average}

            • Budget : {budget} €
            """
        )

# --------------------------------------------------
# TAB 3
# --------------------------------------------------

with tab3:

    fullname = st.text_input(
        "Nom complet"
    )

    university = st.text_input(
        "Université ciblée"
    )

    program = st.text_input(
        "Programme souhaité"
    )

    if st.button("Générer la lettre"):

        letter = f"""
Objet : Candidature au programme {program}

Madame, Monsieur,

Je souhaite intégrer votre programme
{program} au sein de {university}.

Titulaire d'un diplôme de niveau {diploma},
je suis particulièrement motivé à poursuivre
mes études dans un environnement académique
d'excellence.

Mon projet professionnel consiste à développer
des compétences avancées afin de contribuer
au développement de mon pays.

Je vous remercie de l'attention portée à ma
candidature.

Cordialement,

{fullname}
        """

        st.text_area(
            "Lettre générée",
            value=letter,
            height=300
        )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Développé avec Streamlit"
)
