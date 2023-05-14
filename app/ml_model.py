from transformers import pipeline

model = pipeline("question-answering",
                 model="distilbert-base-cased-distilled-squad",
                 tokenizer="distilbert-base-cased")


def find_answer(question, context, model):
    result = model(question=question, context=context)
    return result


def open_txt():
    with open('data.txt', 'r') as file:
        text = file.read()
        return text
