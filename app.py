import streamlit as st

pg = st.navigation([st.Page('pages/Home.py'),
                    st.Page('pages/Risk.py'),
                    st.Page('pages/Map.py')])

pg.run()