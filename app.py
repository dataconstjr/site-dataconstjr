import streamlit as st
from streamlit_navigation_bar import st_navbar
import os


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
        "background-color": "#E0E0E0",
        "color": "#F15A24",
        "font-weight": "normal",
        "padding": "14px",
    },
    "hover":{
        "background-color":"#E0E0E0",
    }
}

parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "images/logotipo.svg")

page = st_navbar(pages, urls=urls, styles=styles, logo_path=logo_path,)


if page == "Quem Somos":
    st.markdown(
        '# DataConstJr'
        )
    





elif page == "Serviços":
    st.markdown(
        """
        Mauris neque dui, scelerisque vel consequat maximus, hendrerit nec
        lorem. Vestibulum suscipit tortor nec gravida imperdiet. Morbi eget ex
        sed nunc hendrerit bibendum in ultrices urna. Pellentesque vitae est
        tellus. Maecenas fringilla ullamcorper tempus. Nulla molestie arcu
        quam. In et nibh a enim volutpat molestie ac id metus.
        """
    )
elif page == "Blog":
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
    st.markdown(
        """
        Sed egestas justo vel leo pulvinar fringilla. Nam aliquam metus vitae
        odio aliquam, in laoreet sapien tempus. Sed sit amet mauris quam.
        Curabitur euismod convallis sapien, sed euismod tellus finibus ac.
        Mauris ut felis vehicula, tincidunt magna quis, dignissim nisi. In
        neque nisi, ultricies in lobortis at, venenatis non neque.
        """
    )
