# https://hub.docker.com/r/nvidia/cuda/tags?page=&page_size=&ordering=&name=12.4
FROM docker.io/nvidia/cuda:12.4.1-runtime-ubuntu22.04 AS python-base

ENV VIRTUAL_ENV=/app/venv

RUN apt update && apt install --no-install-recommends -y \
      python3.11-minimal \
      python3.11-venv \
    && python3.11 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /app



FROM python-base AS install

COPY requirements.txt .
RUN pip install -r requirements.txt



FROM python-base

COPY --from=install "${VIRTUAL_ENV}" "${VIRTUAL_ENV}"

ARG ADD_PACKAGES

RUN if [[ ! -z "$ADD_PACKAGES" ]]; then apt update && apt install -y --no-install-recommends $ADD_PACKAGES; fi

# https://huggingface.co/docs/transformers/installation#offline-mode
ENV HF_DATASETS_OFFLINE=1
ENV HF_HUB_OFFLINE=1
ENV HF_HOME="/tmp/hf-home"

# https://www.gradio.app/guides/environment-variables
ENV GRADIO_ALLOW_FLAGGING="never"

ARG VERSION
LABEL "org.neuronaddict.secure-container-1.gradio-backend/version"=${VERSION}

ENV IMAGE_VERSION=${VERSION}

COPY app.py .

EXPOSE 7860

USER 1001

ENTRYPOINT ["python", "-I", "app.py", "--local-file-only"]
