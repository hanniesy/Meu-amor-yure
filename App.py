import streamlit as st  

# Código SVG para animação
svg_code = """
<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
    <style>
        @keyframes moveLeft {
            0% { transform: translateX(-40px); }
            100% { transform: translateX(0px); }
        }
        @keyframes moveRight {
            0% { transform: translateX(40px); }
            100% { transform: translateX(0px); }
        }
        .left { animation: moveLeft 2s ease-in-out forwards; }
        .right { animation: moveRight 2s ease-in-out forwards; }
    </style>
    <path class="left" d="M 100 180 Q 20 120 50 60 A 30 30 0 1 1 100 60 A 30 30 0 1 1 150 60 Q 180 120 100 180" fill="blue"/>
    <path class="right" d="M 100 180 Q 180 120 150 60 A 30 30 0 1 0 100 60 A 30 30 0 1 0 50 60 Q 20 120 100 180" fill="red"/>
</svg>
"""

# Exibir no Streamlit
st.markdown("<h2 style='text-align: center;'>💙❤️ Você e eu, juntos para sempre! ❤️💙</h2>", unsafe_allow_html=True)
st.markdown(f"<div style='text-align: center;'>{svg_code}</div>", unsafe_allow_html=True)
