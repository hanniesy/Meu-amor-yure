import streamlit as st
import time

def heart_animation():
    st.title("💖 Para o Yure 💖")
    st.write("\n")
    st.subheader("Te amo, Yure! 💕")
    
    heart = [
        "  *****     *****  ",
        "*******   *******",
        " *************** ",
        "   ***********   ",
        "     *******     ",
        "       ***       ",
        "        *        "
    ]
    
    heart_placeholder = st.empty()
    
    for i in range(10):
        heart_text = "\n".join(heart)
        heart_placeholder.markdown(f"<pre>{heart_text}</pre>", unsafe_allow_html=True)
        time.sleep(0.5)
        heart[2] = " " + heart[2] + " " if i % 2 == 0 else heart[2][1:-1]

heart_animation()
