import streamlit as st
import streamlit_antd_components as sac

with st.sidebar:
    st.image('hat.png')

    selected_item = sac.menu([
        sac.MenuItem('Home', icon='arrow-through-heart'),
        sac.MenuItem('Picture', icon='images'),
        sac.MenuItem('notebook', icon='journal-bookmark-fill'),
    ])

if selected_item == 'Picture':
    with st.container():
        st.audio('jingle_bells.mp3', format="audio/mp3")

        sac.divider(label='divider', icon='house', align='center')

        st.image('pp_1.JPG', caption='屁屁1号')

        st.image('pp_3.JPG')

        st.image('pp_4.JPG')
if selected_item == 'notebook':
    with st.container():
        selected_step = sac.steps(
            items=[
                sac.StepsItem(title='2023.09.16', subtitle='****', description='*****，********，'),
                sac.StepsItem(title='step 2'),
                sac.StepsItem(title='step 3'),
                sac.StepsItem(title='step 4', disabled=True),
            ], format_func='title'
        )
    if selected_step == '2023.09.16':
        st.caption('屁屁')


