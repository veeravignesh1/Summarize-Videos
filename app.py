# Imports
import youtube_dl
import streamlit as st


# ============================
# TO-DO
# Create a stramlit app which can take in URL from the user
# Validate that it is youtube URL using regex
# If passes the validation move on to downloading the caption in English if available.
# If not post the user that the caption was not available
# On sumbit allow user to have a text box with the summary populated
# Find out if the text box can contain the copy option so that the summary can be saved elsewhere as per needs
# ============================

# Download Caption
def closed_caption(url):
    pass

# Summarizer
def summarizer(cc,fraction):
    pass

# Main UI
def main():
    st.title("Video Summarizer")
    url = st.text_input(
        "URL",
        help="Currently we support Youtube URL",
    )
    cc = closed_caption(url)
    fraction = st.slider(
        "Length of Summary",
        min_value=0.1,
        max_value=1.0,
        value=0.3,
        step=0.1,
        help="Adjust the Slider to Get varying Output Length",
    )
    summary = summarizer(cc,fraction)
    if st.button("Get Summary"):
        st.text_area(
            "Summary",
            value=summary,
            height=300,
        )


if __name__ == "__main__":
    main()
