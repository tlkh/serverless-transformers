# Work in Progress [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/tlkh/serverless-transformers/main/app.py)

Live link: https://share.streamlit.io/tlkh/serverless-transformers/main/app.py

# Serverless Transformer

Serve HuggingFace Transformer models via serverless (mostly free):

* Cloud Run
  * 4GB + 4 vCPU: run up to 200+M parameter Transformer (e.g. T5-base)
  * autoscale to 0, free monthly quota
* Free web interface via Streamlit Share

## Deployment

### Build Backend Container

```shell
cd backend
docker build . -t cloudrun-transformer
```
