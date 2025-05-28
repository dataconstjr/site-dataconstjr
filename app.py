import streamlit as st
from streamlit_navigation_bar import st_navbar
import os
from PIL import Image

st.set_page_config(layout='wide')
pages = ["Quem Somos", "Serviços", "Blog", "Contato"]
urls = {}
styles = {
    "nav": {
        "background-color": "#8523F5",
        "display" : "flex",
        "justify-content": "space-between",
        "height": "80px",
    },
    "img": {
        "padding-right": "14px",
        "transform": "scale(8)",
        "margin-right": "500px",
        "margin-left": "100px",
        "margin-top" :"20px",
        "margin-bottom" : "20px",
    },
    "span": {
        "color": "black",
        "padding": "10px 30px",  
        "border-radius": "16px",
        "font-size": "18px", 
        "min-width": "130px",
        "font-weight" : "bold",
        "text-align" : "center",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
           },
    "hover":{
        "background-color":"#E0E0E0",
    }
}

parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "images/logotipo.svg")

page = st_navbar(pages, urls=urls, styles=styles, logo_path=logo_path,)


col1, col2 = st.columns(2)
if page == "Quem Somos":
    
    st.title("Bem-vindo a Dataconst Jr")
    st.markdown(""" #### Análises confiáveis, soluções inteligentes  """)

    st.markdown("---")

    st.markdown("""
    ### Sobre Nós

    A Dataconst Jr é a Empresa Júnior de Estatística da UFBA, formada por estudantes apaixonados por dados e tecnologia. 
    Nosso propósito é aproximar a academia do mercado, oferecendo soluções estatísticas acessíveis e de alta qualidade.

    Acreditamos na democratização da estatística e trabalhamos com uma diversidade de projetos que vão desde análises descritivas, 
    modelagem preditiva, estudos de mercado, até inteligência artificial, sempre com foco em gerar valor para nossos clientes.
    """)


    col1, col2 = st.columns(2)

    with col1:
        image_path = os.path.join("images", "membros2.jpg")
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, use_container_width=True)

    with col2:
        image_path = os.path.join("images", "membros3.jpg")
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, use_container_width=True)


    
    


elif page == "Serviços":
    st.markdown("### Nossos Serviços")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
    <div class="service-card">
        <div style="height: 100px;">
            <h5>• Serviços Acadêmicos</h5>
            <p style="margin: 0;">Realizamos análises para IC, TCC, Mestrado e Doutorado</p>
        </div>
        <div style="height: 140px;">
            <h5>• Dashboards personalizados</h5>
            <p style="margin: 0;">Transformamos dados complexos em visualizações interativas e intuitivas, com dashboards desenvolvidos para facilitar a tomada de decisão</p>
        </div>
        <div style="height: 120px;">
            <h5>• Planejamento amostral e de experimentos</h5>
            <p style="margin: 0;">Realizamos o planejamento da amostragem e estruturação de experimentos para garantir resultados confiáveis e representativos</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
    <div class="service-card">
        <div style="height: 100px;">
            <h5>• Inteligência Artificial e Machine Learning</h5>
            <p style="margin: 0;">Soluções com IA como chatbots, modelos preditivos e classificatórios</p>
        </div>
        <div style="height: 140px;">
            <h5>• Treinamentos e cursos</h5>
            <p style="margin: 0;">Capacitamos pessoas e equipes com conteúdos sobre estatística, análise de dados e ferramentas digitais como Python, R, Power BI</p>
        </div>
        <div style="height: 120px;">
            <h5>• Pesquisa de mercado e formulário</h5>
            <p style="margin: 0;">Elaboramos formulários e pesquisas de mercado, ajudando a gerar dados estratégicos</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    

        
elif page == "Blog":
    with col1:
        st.markdown(
        """
        Maecenas mollis, mauris sit amet pretium convallis, massa augue
        scelerisque felis, in sagittis ante risus quis arcu. Nullam eu dolor id
        tellus venenatis dapibus. Praesent a feugiat metus, a congue leo.
        Suspendisse ipsum nunc, mattis eget luctus vel, molestie in ante.
        Aliquam erat volutpat. Donec sollicitudin quam ac aliquet pellentesque.
        """
    )
elif page == "Contato":
    with col1:
        st.markdown(
        """
        Sed egestas justo vel leo pulvinar fringilla. Nam aliquam metus vitae
        odio aliquam, in laoreet sapien tempus. Sed sit amet mauris quam.
        Curabitur euismod convallis sapien, sed euismod tellus finibus ac.
        Mauris ut felis vehicula, tincidunt magna quis, dignissim nisi. In
        neque nisi, ultricies in lobortis at, venenatis non neque.
        """
    )
        




st.divider()
st.markdown("<p style='text-align: center;'>Desenvolvido por Dataconst Jr - Empresa Júnior de Estatística da UFBA</p>", unsafe_allow_html=True)

    
st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
        <a href='mailto:dataconstjr@gmail.com' target='_blank'>
            <img src='https://img.icons8.com/color/48/000000/email.png' width='40'/>
        </a>
        <a href='https://www.instagram.com/dataconstjr' target='_blank'>
            <img src='https://img.icons8.com/color/48/000000/instagram-new.png' width='40'/>
        </a>
        <a href='https://github.com/dataconstjr' target='_blank'>
            <img src='https://img.icons8.com/ios-filled/50/000000/github.png' width='40'/>
        </a>
        <a href='https://wa.me/5571991216019' target='_blank'>
            <img src='https://img.icons8.com/color/48/000000/whatsapp.png' width='40'/>
        </a>
        <a href='https://www.linkedin.com/in/dataconst-jr-992375355/' target='_blank'>
            <img src='https://img.icons8.com/color/48/000000/linkedin.png' width='40'/>
        </a>
        </div>
        """, unsafe_allow_html=True) 
    
st.write("")
st.write("")
