import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="App Personnages v0.1",
    page_icon="📖",
    layout="wide"
)

st.title("📖 Conception de Fiches Personnages")
st.caption("Renseigne quelques éléments clés ou la totalité de la fiche, puis laisse l'IA compléter les espaces vides.")

# Création des trois onglets
tab1, tab2, tab3 = st.tabs([
    "👤 État civil & Physique",
    "🤝 Vie intime & Sociale",
    "⚡ Moteurs narratifs"
])

# --- VOLET 1 : ÉTAT CIVIL & PHYSIQUE ---
with tab1:
    col_img, col_vide = st.columns([1, 2])
    with col_img:
        fichier_image = st.file_uploader(
            "Portrait ou illustration du personnage", 
            type=["jpg", "jpeg", "png", "webp"]
        )
        if fichier_image is not None:
            st.image(fichier_image, caption="Portrait sélectionné", use_container_width=True)

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        prenom = st.text_input("Prénom", placeholder="Ex : Léonie")
        nom = st.text_input("Nom", placeholder="Ex : Morel")
        age = st.slider("Âge", min_value=1, max_value=105, value=35)
    with col2:
        cadre_vie = st.text_input("Adresse / Cadre de vie", placeholder="Ex : Ferme isolée sur le premier plateau jurassien")
        silhouette = st.text_input("Silhouette & allure générale", placeholder="Ex : Trapue, pas lourd mais décidé")
        mimiques = st.text_area("Mimiques, voix et détails physiques", placeholder="Ex : Fronce les sourcils avant de répondre, voix rauque...", rows=3)

# --- VOLET 2 : VIE INTIME & SOCIALE ---
with tab2:
    col_soc1, col_soc2 = st.columns(2)
    with col_soc1:
        histoire_passee = st.text_area("Histoire passée / Origines", placeholder="Originaire de quelle région ? Blessures d'enfance ?", rows=4)
        vie_famille = st.text_area("Famille et proches", placeholder="Parents, fratrie, dynamique familiale...", rows=4)
        vie_pro = st.text_input("Vie professionnelle / Activité", placeholder="Ex : Artisan du bois, ancienne institutrice...")
    with col_soc2:
        relations = st.text_area("Relations amoureuses & amicales", placeholder="Célibataire endurci, liens indéfectibles, trahisons passées...", rows=4)
        distractions = st.text_input("Passions & distractions", placeholder="Ex : Botanique, lecture tardive, longues marches...")
        dates_marquantes = st.text_area("Dates ou événements charnières", placeholder="Ex : L'hiver 1985, le départ du fils aîné...", rows=2)

# --- VOLET 3 : MOTEURS NARRATIFS ---
with tab3:
    col_narr1, col_narr2 = st.columns(2)
    with col_narr1:
        objectif = st.text_area("Objectif principal & rêves", placeholder="Que cherche-t-il à obtenir ou protéger à tout prix ?", rows=3)
        obstacles = st.text_area("Conflits & obstacles", placeholder="Qui ou quoi s'oppose directement à son but ?", rows=3)
    with col_narr2:
        faiblesse = st.text_area("Faiblesse cachée ou secret", placeholder="La fêlure secrète, le remords ou la peur inavouée...", rows=3)
        temperament = st.text_area("Caractère face à la crise", placeholder="Explose sous la colère, se mure dans le silence, calcule froidement...", rows=3)

st.divider()

# --- ACTION & RÉSULTAT ---
col_btn1, col_btn2 = st.columns([1, 4])
with col_btn1:
    generer = st.button("✨ Compléter avec l'IA", type="primary", use_container_width=True)

if generer:
    # Simulation visuelle pour valider le flux avant le branchement API
    st.info("Données prêtes à être envoyées à Gemini 3.7 Flash.")
    
    st.subheader("Aperçu des données saisies :")
    recapitulatif = {
        "Identité": f"{prenom} {nom} ({age} ans)",
        "Cadre": cadre_vie,
        "Objectif clé": objectif,
        "Secret / Fêlure": faiblesse,
        "Portrait joint": "Oui" if fichier_image is not None else "Non"
    }
    st.json({k: v for k, v in recapitulatif.items() if v})
    
    st.success("Structure d'interface opérationnelle avec gestion d'image !")