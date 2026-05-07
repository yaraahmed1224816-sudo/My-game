import streamlit as st

# إعدادات اللعبة
st.set_page_config(page_title="KING", layout="wide")
st.markdown("<h1 style='text-align: center; color: gold;'>👑 KING 👑</h1>", unsafe_allow_html=True)
st.write("---")

# واجهة الدخول
name = st.text_input("ادخل اسمك يا ملك:")
password = st.text_input("كلمة السر:", type="password")

if st.button("دخول الساحة 🚀"):
    if name and password:
        st.success(f"أهلاً بك يا {name}! جاري تجهيز الجيم...")
        st.balloons()
    else:
        st.error("اكتب الاسم والباسورد الأول!")
