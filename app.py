import streamlit as st

st.set_page_config(
    page_title = "Streamlit Practice App",
    page_icon=":apple:",
    layout="centered",   # 'wide'
    initial_sidebar_state="collapsed",  # 'expanded', 'wide'
#     menu_items={
#         'Get Help': 'This id help page',
#         'About': "# This is a header. This is an *extremely* cool app!"
#     }
)
st.title('스트림릿 맛보기 :safety_pin:')

# streamlit으로 파일 실행: streamlit run 파일이름.py
# Emoji : 'https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/'

# text = st.Page('pages/text_elements.py', title='텍스트요소', icon='📌')

# sess = st.Page('pages/9_session.py', title='세션이해', icon='⭐')
# order = st.Page('pages/10_caching_ex_주문관리.py', title='주문관리', icon='⭐')
#nav = st.navigation({'대시보드':[sess. order]})