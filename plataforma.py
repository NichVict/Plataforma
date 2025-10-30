import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Métricas para Investidores", page_icon="⚡")

# ---------- Fundo preto ----------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #000000;
    }
    ::-webkit-scrollbar-thumb {
        background: #333333;
        border-radius: 4px;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Logo central do topo ----------
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("logo.png", use_container_width=True)
    st.markdown(
        "<p style='text-align:center; font-size:15px; color:#FFD700; margin-top:5px; white-space: nowrap;'>Transformando dados em decisões estratégicas.</p>",
        unsafe_allow_html=True
    )

st.markdown(
    "<h1 style='text-align: center; margin-top: 20px; color:#FFFFFF;'>Plataforma para Investidores</h1>",
    unsafe_allow_html=True
)
st.write("")



# ---------- Função para criar card clicável ----------
def clickable_card(path, link, main_title, sub_title, description, width=250):
    with open(path, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    
    html = f"""
    <a href="{link}" target="_blank" class="card-link">
        <div class="card">
            <img src="data:image/png;base64,{encoded}" width="{width}">
            <h1 class="main-title">{main_title}</h1>
            <h2 class="sub-title">{sub_title}</h2>
            <p>{description}</p>
        </div>
    </a>
    """
    return html

# ---------- CSS ----------
st.markdown(
    """
    <style>
    /* Remove sublinhado de links */
    .card-link {
        text-decoration: none !important;
        color: inherit !important;
    }

    /* Card */
    .card {
        text-align: center;
        background-color: #333333;
        padding: 25px;
        border-radius: 15px;
        width: 90%;
        margin: 20px auto;
        transition: transform 0.3s, box-shadow 0.3s;
    }

    .card:hover {
        transform: scale(1.03);
        box-shadow: 0 12px 25px rgba(0,0,0,0.5);
    }

    .card img {
        margin-bottom: 20px;
    }

    /* Títulos e textos */
    .main-title {
        font-size: 18px;  
        color: #FFD700 !important;  /* amarelo */
        margin: 0;
        margin-bottom: 10px;
        font-family: 'Arial', sans-serif;
    }

    .sub-title {
        font-size: 15px;  
        color: #21bca8 !important;  /* verde água */
        margin: 0;
        margin-bottom: 10px;
        font-family: 'Arial', sans-serif;
    }

    .card p {
        font-size: 14px;
        color: #FFFFFF;  /* branco */
        margin-top: 5px;
        font-family: 'Arial', sans-serif;
    }

    /* Layout responsivo */
    @media (max-width: 768px) {
        .card {
            width: 90% !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Layout vertical com 5 cards ----------
st.markdown(
    clickable_card(
        "logo.png",
        "https://dashboardopcoes.streamlit.app/",
        "DASHBOARD OPCOES",
        "Análise de Opções B3",
        "Tenha todas as métricas necessárias para simular e encontrar oportunidades no mercado de opções de ações da B3",
    ),
    unsafe_allow_html=True
)

st.markdown(
    clickable_card(
        "logo.png",
        "https://buscadordeopcoes.streamlit.app/",
        "SCANNER",
        "Busca Automática por Opções",
        "Seleciona os ativos subjacentes e seus parâmetros e o algoritmo faz as buscas",
    ),
    unsafe_allow_html=True
)

st.markdown(
    clickable_card(
        "logo.png",
        "https://fluxos.streamlit.app/",
        "FLUXO",
        "Monitoramento de Fluxo de Investidores e Ativos B3",
        "Informações valiosas sobre o fluxo dos principais players do mercado, e também de todos os ativos listados na B3",
    ),
    unsafe_allow_html=True
)

st.markdown(
    clickable_card(
        "logo.png",
        "https://calculadoranotion.streamlit.app/",
        "NOTIONAL",
        "Calculadora de Notional de Opções",
        "Descubra a equivalência entre comprar Ações e Opções",
    ),
    unsafe_allow_html=True
)

st.markdown(
    clickable_card(
        "logo.png",
        "https://calculadorblackescholes.streamlit.app/",
        "Black & Scholes",
        "Calculadora de Black & Scholes",
        "Calcule e simule o prêmio de cada opção, métricas gregas e gráfico de Payoff",
    ),
    unsafe_allow_html=True
)

st.markdown(
    clickable_card(
        "logo.png",
        "https://radaropcoes.streamlit.app/",
        "Radar",
        "Radar de Tendência por Opções",
        "Estimativa de Tendência baseada nos strikes com maior negociação",
    ),
    unsafe_allow_html=True
)
