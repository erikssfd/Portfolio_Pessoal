from pathlib import Path
import streamlit as st
from PIL import Image


#--------- Configurações de Localização dos arquivos -------------#

caminho_Atual = Path(__file__).parent if "__file__" in locals () else Path.cwd()

Arq_css = caminho_Atual / "estilos" / "estilo.css"
curriculo = caminho_Atual / "arquivos"/ "Erik Marta Garcia.pdf"
foto = caminho_Atual / "arquivos"/ "ft5.png"

#C:\Users\Beto\Desktop\portfolio_digital\estilos\estilo.css

# -----------------CONFIGURAÇÕES GERAIS---------------------- # 
PAGE_TITLE = "Cúrriculo Digital | Erik Marta Garcia"
PAGE_ICON = ":wave"
NAME = "Erik Garcia"
DESCRIPTION = """ Ciêntista de Dados - Ajudando as empresas a tomar decisões com base em fundamentos estatísticos."""
EMAIL = "erik.martaneva@gmail.com"
SOCIAL_MEDIA = {
        "GitHub" : "https://github.com/erikssfd",
        "Medium" : "https://medium.com/@erik.martaneva",
        "LinkedIn" : "https://www.linkedin.com/in/erikmartagarcia/"
}

PROJECTS = {
        "💻 Amazon Dashboard - Comparação de produtos amazon" : "https://github.com/erikssfd/AmzonDashboard",
        "💻 Coursera Dashboard - Comparações de Preços e Avaliações" : "https://github.com/erikssfd/CourseraDashboard",
        "💻 Como fazer seu portfólio Digital" : "https://github.com/erikssfd/PortfolioDigital"
}

st.set_page_config(page_title = PAGE_TITLE, page_icon = PAGE_ICON)

# ----------------- Carregando CSS, PDF & FOTO DE PERFIL --------------------- #

with open(Arq_css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html = True)
    
with open(curriculo, "rb") as curriculo_pdf:
    PDFbyte = curriculo_pdf.read()
    
foto_perfil = Image.open(foto)

# -------------------------- Colunas ------------------------------------------ #

coluna1, coluna2 = st.columns(2, gap = "small")

with coluna1:
    st.image(foto_perfil, width = 230)
    
with coluna2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "Baixe meu Cúrriculo Aqui ✅",
        data = PDFbyte,
        file_name = curriculo.name,
        mime = "application/octet-stream",
    )
    st.write("📧", EMAIL)
    
# ---------------------------- Links de Mídias Sociais ------------------------- #

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --------------------------- Experiência e Qualificações ---------------------- #
 
st.write("#")
st.subheader("Experiência & Qualificações")
st.write("""
         - ✔ Carreira de excelência em Tecnologia da Informação com 3 anos de experiência.
         - ✔ Bom conhecimento em Python e SQL
         - ✔ Criação de insights em Dashboard com StoryTelling
         - ✔ Ótimo Relacionamento Interpessoal e Respeito a hierarquia de Cargo
         - ✔ Excelente trabalho em equipe e iniciativa para resolver problemas
         """)

# --------------------------- Habilidades ------------------------------------- #
st.write("#")
st.subheader("Habilidades")
st.write("""
         - ✔ 💻Programação: Python (Pandas, Numpy, MatplotLib, Statistics e StreamLit)
         - ✔ 💻Programação: R (Pandas, Numpy, MatplotLib, Statistics e StreamLit)
         - ✔ 📊Visualização de Dados: Tableau e Plotly
         - ✔ 🔍Análise Exploratória, Limpeza de Dados e  ForeCasting
         - ✔ 📋Modelação: Regressão Logística, Regressão Linear e Arvores de Decisões
         - ✔ 🎲Banco de Dados: MySQL
         - ✔ ♟IA: Me especializando em Machine Learning e Deep Learning
         """)

# --------------------------- Histórico de Trabalho ---------------------------- #
st.write("#")
st.subheader("Histórico de Trabalho")
st.write("-----")
 
 
st.write("🧑‍💼", "** Conferente - Chefe | BUNGE**")
st.write("(01/2023) - (08/2023)")
st.write("""
         - Desenvolvimento de controles industriais com planilhas automatizadas.
         Com a implementação, foi garantido um aumento de 45% na produtividade industrial,
         aumentando gradativamente de 3987.4 mil para 6.977.77 mil dólares ao patrimônio mensal.
         - Implementação e configuração de dispositivos Zebra e desenvolvimento de etiquetas.
         Todo o processo de configuração e fase de criação de etiquetas obteve ótimos resultados do gestor fabril,
         acompanhando sempre o desenvolvimento e criação de tais. 
         O processo levou cerca de 7 meses para ser implementado, e obtivemos um retorno de 120% de eficácia
         em todos os processos que utilizaram.
         """)

st.write("🧑‍💼", "** Auxiliar de Almoxarifado | Alliz**")
st.write("(09/2020)-(25/07/2021)")
st.write("""
         - Migração de planilhas automatizadas para sistema o Sankhya.
         A empresa em foco tinha todas as informações em planilhas automáticas e em uma reunião opinei em um sistema otimizado
         e tecnológico, resultando em, organização de dados, análises mais práticas e rápidas,
         evolução de '50%' a mais de pedidos de clientes estrangeiros e '73%' de pedidos nacionais.
         - Com o aumento de pedidos nacionais e internacionais, houve um aumento significativo
         de lucros com a implementação do sistema, em torno de 39.000,00 Dólares a mais de pedidos internacionais diários
         e 27.000,00 Dólares de pedidos nacionais.
         """)

# --------------------------- Projetos & Conquistas ---------------------------- #
st.write("#")
st.subheader("Projetos e Conquistas")
st.write("-----")

for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")