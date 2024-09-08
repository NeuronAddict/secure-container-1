import argparse
import os
from transformers import pipeline
import gradio as gr
import requests
import html2text


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--model_type', help='model type for pipeline (or use env var MODEL_TYPE)', default=os.environ.get('MODEL_TYPE'))
    parser.add_argument('--model', help='model name ot path (or use env var MODEL)', default=os.environ.get('MODEL'))
    parser.add_argument('--device', help='device to use (or use env var DEVICE)', default=os.environ.get('DEVICE', 'cuda'))
    parser.add_argument('--local-file-only', help='only allow local file for model (env var: LOCAL_FILE_ONLY)',
                        action='store_true')
    parser.add_argument('--host', help='Host to bind server (env var: HOST)', default=os.environ.get('HOST', '0.0.0.0'))

    args = parser.parse_args()

    for key, value in vars(args).items():
        print(f"{key}: {value}")

    image_version = os.environ.get('IMAGE_VERSION')
    if image_version is not None:
        print(f'image version: {image_version}')



    nlp = pipeline(
        args.model_type,
        model=args.model,
        local_files_only=args.local_file_only,
        device=args.device,
        clean_up_tokenization_spaces=False
    )

    def handle_input(link: str, question: str):

        print(f'get url {link}')
        r = requests.get(link, timeout=10)
        r.raise_for_status()
        print(f'receive response {r.status_code} with content: {r.text[:1000]}')
        context = r.text

        input_data = {'context': html2text.html2text(context), 'question': question}

        response = nlp(input_data)

        print(response)
        return response['answer']

    inputs = [gr.Textbox(), gr.Textbox()]

    outputs = [gr.Textbox()]

    examples = [["https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git",
                "Comment installer git sur linux ?"]]

    interface = gr.Interface(fn=handle_input, inputs=inputs, outputs=outputs, examples=examples)
    interface.launch(
        server_name=args.host,
    )


