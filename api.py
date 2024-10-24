import nlpcloud
client = nlpcloud.Client("finetuned-llama-3-70b", "5f17eaa75496d8857a19fcd0a202ed579149b821", gpu=True)
def ner(text):
    return client.entities(text,
        searched_entity="programming languages"
    )