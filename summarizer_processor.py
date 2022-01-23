import urllib.request 
import pickle
import bs4 as BeautifulSoup


def summarizeFromContent(content):
    model = pickle.load(open('model.pkl','rb'))
    tokenizer = pickle.load(open('tockenizer.pkl','rb'))
    inputs = tokenizer.encode("summarize: " + content, return_tensors="pt", max_length=512, truncation=True)
    
    # generate the summarization output
    outputs = model.generate(
        inputs, 
        max_length=150, 
        min_length=40, 
        length_penalty=2.0, 
        num_beams=4, 
        early_stopping=True)

    summary = tokenizer.decode(outputs[0])
    summary = summary.replace('<pad>','')
    summary = summary.title()
    return summary


def summarizeFromURL(url):
    article_content = fetchDataFromUrl(url)
    print(article_content[100])
    summary = summarizeFromContent(article_content)
    return summary

def fetchDataFromUrl(url):
    # fetch
    fetched_data = urllib.request.urlopen(url)
    article_read = fetched_data.read()

    # parse
    article_parsed = BeautifulSoup.BeautifulSoup(article_read,'html.parser')
    paragraphs = article_parsed.find_all('p')

    #populate
    article_content = ''
    for p in paragraphs:  
        article_content += p.text
    return article_content

