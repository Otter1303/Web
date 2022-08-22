import streamlit
a = streamlit.set_page_config(page_title="Phimm",page_icon="clapperboard.ico") 
a = streamlit.header("Phim hay o dayyy!")
col1,col2 = streamlit.columns(2) 
# (2) la so luong cot
a =
b = streamlit.sidebar.selectbox("Ten phim", ["Harry Potter", "Catch me if you can"])
with col1:
    a = streamlit.write("Harry Potter")
    a = streamlit.video("https://www.youtube.com/watch?v=VyHV0BRtdxo")
    a = streamlit.write("[Watch hereee](https://xemphim.vip/watch/195)")
with col2:
    a = streamlit.write("Catch me if you can")
    a = streamlit.video("https://www.youtube.com/watch?v=s-7pyIxz8Qg")
    a = streamlit.write("[Watch hereee](https://xemphim.vip/watch/1925)")
