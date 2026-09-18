import streamlit as st

st.title('카운터 예제')
count = 0
if st.button('증가'):
    count += 1

st.write('count=', count)

# session_state 사용

if 'count' not in st.session_state:
    st.session_state.count = 0



# if st.button('증가', key='btn_ㅑincrease'):
#     st.session_state.count += 1
def increase():
    st.session_state.count += 1
st.button('증가', key='btn_increase', on_click=increase)
    

st.write('count=', st.session_state.count)

if st.button('감소', key='btn_decrease'):
    st.session_state.count -= 1

st.write('count=', st.session_state.count)