import streamlit as st
from pytubefix import YouTube

st.title("🎥 YouTube Downloader")

# ---- Input ----
url = st.text_input("Paste YouTube link")

# ---- Action ----
if st.button("Download"):
    if not url:
        st.error("Please enter a URL")
    else:
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()

            st.success("Video fetched successfully!")

            st.write("### Title")
            st.write(yt.title)

            st.write("### Download Link")
            st.markdown(stream.url)

        except Exception as e:
            st.error(f"Error: {e}")
