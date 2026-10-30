import streamlit as st

st.set_page_config(page_title="Calcul Note", page_icon="📚")

st.title("📚 Calcul de la moyenne")
st.write("Choisissez votre division :")

tab1, tab2, tab3 = st.tabs(["SM", "PC", "SVT"])


def calcul(div_name):
    st.subheader(f"Contenu de {div_name}")
    if div_name == "SM":
        note_math = st.number_input(
            "Math", min_value=0.0, max_value=20.0, key=f"{div_name}_math"
        )
        note_pc = st.number_input(
            "PC", min_value=0.0, max_value=20.0, key=f"{div_name}_pc"
        )
        note_svt = st.number_input(
            "SVT", min_value=0.0, max_value=20.0, key=f"{div_name}_svt"
        )
        note_arab = st.number_input(
            "Arabe", min_value=0.0, max_value=20.0, key=f"{div_name}_arab"
        )
        note_fr = st.number_input(
            "Français", min_value=0.0, max_value=20.0, key=f"{div_name}_fr"
        )
        note_ie = st.number_input(
            "IE", min_value=0.0, max_value=20.0, key=f"{div_name}_ie"
        )
        note_sport = st.number_input(
            "Sport", min_value=0.0, max_value=20.0, key=f"{div_name}_sport"
        )
        note_ph = st.number_input(
            "Philosophie", min_value=0.0, max_value=20.0, key=f"{div_name}_ph"
        )
        note_english = st.number_input(
            "Anglais", min_value=0.0, max_value=20.0, key=f"{div_name}_english"
        )

        if st.button("Calculer", key=f"{div_name}_button"):

            resultat = (
                               note_math * 9
                               + note_pc * 7
                               + note_svt * 3
                               + note_arab * 2
                               + note_fr * 4
                               + note_ie * 2
                               + note_sport * 5
                               + note_ph * 2
                               + note_english * 3
                       ) / 37

            st.write(f"### Votre moyenne est : {resultat:.2f}")

            if resultat >= 16:
                st.success("🎉 Très bien")
            elif resultat >= 14:
                st.success("😊 Bien")
            elif resultat >= 12:
                st.success("👍 Assez bien")
            elif resultat >= 10:
                st.success("✅ Passable")
            else:
                st.error("❌ Échoué")
    if div_name == "PC":
        note_math = st.number_input(
            "Math", min_value=0.0, max_value=20.0, key=f"{div_name}_math"
        )
        note_pc = st.number_input(
            "PC", min_value=0.0, max_value=20.0, key=f"{div_name}_pc"
        )
        note_svt = st.number_input(
            "SVT", min_value=0.0, max_value=20.0, key=f"{div_name}_svt"
        )
        note_arab = st.number_input(
            "Arabe", min_value=0.0, max_value=20.0, key=f"{div_name}_arab"
        )
        note_fr = st.number_input(
            "Français", min_value=0.0, max_value=20.0, key=f"{div_name}_fr"
        )
        note_ie = st.number_input(
            "IE", min_value=0.0, max_value=20.0, key=f"{div_name}_ie"
        )
        note_sport = st.number_input(
            "Sport", min_value=0.0, max_value=20.0, key=f"{div_name}_sport"
        )
        note_ph = st.number_input(
            "Philosophie", min_value=0.0, max_value=20.0, key=f"{div_name}_ph"

        )
        note_english = st.number_input(
            "Anglais", min_value=0.0, max_value=20.0, key=f"{div_name}_english"
        )

        if st.button("Calculer", key=f"{div_name}_button"):

            resultat = (
                               note_math * 7
                               + note_pc * 7
                               + note_svt * 5
                               + note_arab * 2
                               + note_fr * 4
                               + note_ie * 2
                               + note_sport * 5
                               + note_ph * 2
                               + note_english * 3
                       ) / 37

            st.write(f"### Votre moyenne est : {resultat:.2f}")

            if resultat >= 16:
                st.success("🎉 Très bien")
            elif resultat >= 14:
                st.success("😊 Bien")
            elif resultat >= 12:
                st.success("👍 Assez bien")
            elif resultat >= 10:
                st.success("✅ Passable")
            else:
                st.error("❌ Échoué")
    if div_name == "SVT":
        note_math = st.number_input(
            "Math", min_value=0.0, max_value=20.0, key=f"{div_name}_math"
        )
        note_pc = st.number_input(
            "PC", min_value=0.0, max_value=20.0, key=f"{div_name}_pc"
        )
        note_svt = st.number_input(
            "SVT", min_value=0.0, max_value=20.0, key=f"{div_name}_svt"
        )
        note_arab = st.number_input(
            "Arabe", min_value=0.0, max_value=20.0, key=f"{div_name}_arab"
        )
        note_fr = st.number_input(
            "Français", min_value=0.0, max_value=20.0, key=f"{div_name}_fr"
        )
        note_ie = st.number_input(
            "IE", min_value=0.0, max_value=20.0, key=f"{div_name}_ie"
        )
        note_sport = st.number_input(
            "Sport", min_value=0.0, max_value=20.0, key=f"{div_name}_sport"
        )
        note_ph = st.number_input(
            "Philosophie", min_value=0.0, max_value=20.0, key=f"{div_name}_ph"
        )
        note_english = st.number_input(
            "Anglais", min_value=0.0, max_value=20.0, key=f"{div_name}_english"
        )

        if st.button("Calculer", key=f"{div_name}_button"):

            resultat = (
                               note_math * 7
                               + note_pc * 5
                               + note_svt * 7
                               + note_arab * 2
                               + note_fr * 4
                               + note_ie * 2
                               + note_sport * 2
                               + note_ph * 2
                               + note_english * 3
                       ) / 34

            st.write(f"### Votre moyenne est : {resultat:.2f}")

            if resultat >= 16:
                st.success("🎉 Très bien")
            elif resultat >= 14:
                st.success("😊 Bien")
            elif resultat >= 12:
                st.success("👍 Assez bien")
            elif resultat >= 10:
                st.success("✅ Passable")
            else:
                st.error("❌ Échoué")


with tab1:
    calcul("SM")

with tab2:
    calcul("PC")

with tab3:
    calcul("SVT")