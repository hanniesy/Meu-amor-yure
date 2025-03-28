import streamlit as st

# HTML e CSS para a animação
html_code = """
<style>
@keyframes juntar {
    0% { transform: translateX(-50px); }
    50% { transform: translateX(0px); }
}

.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.heart {
    width: 100px;
    height: 100px;
    position: relative;
    display: inline-block;
    animation: juntar 2s ease-in-out forwards;
}

.heart::before,
.heart::after {
    content: "";
    width: 50px;
    height: 80px;
    position: absolute;
    background-color: red;
    border-radius: 50px 50px 0 0;
    top: 0;
}

.heart::before {
    left: 50px;
    transform: rotate(-45deg);
    background-color: blue;
}

.heart::after {
    left: 0;
    transform: rotate(45deg);
    background-color: red;
}
</style>

<div class="container">
    <div class="heart"></div>
</div>
"""

# Exibir a animação no Streamlit
st.markdown(html_code, unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Você e eu, juntos para sempre! 💙❤️</h2>", unsafe_allow_html=True)
