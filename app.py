import streamlit as st
import random

st.set_page_config(page_title="لعبة الأحكام", page_icon="🎲")

st.title("🎲 لعبة الأحكام العشوائية")
st.write("العبوا أونلاين.. اختاروا الضحية ونفذوا الحكم!")

# تحديد عدد اللاعبين
num_players = st.number_input("عدد اللاعبين (2-10):", min_value=2, max_value=10, value=2)

# إنشاء خانات لأسماء اللاعبين
st.subheader("👤 أسماء الأبطال")
player_names = []
cols = st.columns(2) # تقسيم الشاشة لعمودين عشان الشكل يبقى أنظم
for i in range(num_players):
    name = cols[i % 2].text_input(f"اللاعب {i+1}", key=f"p{i}")
    if name:
        player_names.append(name)

# إنشاء خانات للأحكام
st.subheader("📜 قائمة الأحكام")
challenges = []
for i in range(num_players):
    task = st.text_input(f"الحكم {i+1}", key=f"c{i}")
    if task:
        challenges.append(task)

# زر البدء
if st.button("🎯 مين الضحية؟"):
    if len(player_names) == num_players and len(challenges) == num_players:
        victim = random.choice(player_names)
        selected_task = random.choice(challenges)
        
        st.balloons() # حركة احتفالية
        st.success(f"الضحية هي: **{victim}**")
        st.warning(f"الحكم هو: **{selected_task}**")
    else:
        st.error("لازم تملوا كل الأسماء والأحكام الأول!")
