# Work in Progress

# Serverless Transformer

Serve HuggingFace Transformer models via serverless (mostly free):

* Cloud Run (with generous free quota)
* Free web interface via Streamlit Share

## Deployment

### Build Backend Container

```shell
cd backend
docker build . -t cloudrun-transformer
```

