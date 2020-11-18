# Work in Progress

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
