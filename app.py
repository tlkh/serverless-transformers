import functools
import streamlit as st
#st.set_page_config(page_title="Transformer on Cloud Run",
#                   initial_sidebar_state="expanded")
import requests
from newspaper import Article

DEFAULT_QUESTION = "What is COVID-19?"
DEFAULT_URL = "https://en.wikipedia.org/wiki/COVID-19_pandemic"
DEFAULT_ENDPOINT = "https://cloudrun-transformer-test-34x4ouuclq-de.a.run.app/predict"

st.sidebar.markdown("# Transformer on Cloud Run")
st.sidebar.markdown("**Options**")
article_url = st.sidebar.text_input("Document URL", DEFAULT_URL)
max_words = st.sidebar.slider("Max Word Count", min_value=128, max_value=1024, value=512, step=32)

@st.cache
def download_article(article_url):
    article = Article(article_url, fetch_images=False)
    article.download()
    article.parse()
    article_text = article.text
    return article_text.strip()

@st.cache
def make_api_query(context, question, endpoint):
    query_json = {
        "context": str(context).strip(),
        "question": str(question).strip(),
    }
    response = requests.post(endpoint, json=query_json).json()
    return response

def main():
    st.sidebar.markdown("## Question Answering Demo")
    article_text = download_article(article_url)
    article_text = " ".join(article_text.split(" ")[:max_words])
    context = article_text
    with st.beta_expander(label="Document", expanded=False):
        st.markdown(article_text)
    question = st.text_input("Question", DEFAULT_QUESTION)
    response = make_api_query(context, question, DEFAULT_ENDPOINT)
    try:
        answer = response["answer"][0]
        st.markdown("### "+answer)
    except:
        st.markdown(response)

main()