from flask import Flask, request, make_response

from summarizer_processor import summarizeFromContent, summarizeFromURL

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def hello():
    return "Testing get";

@app.route('/summarization-from-content',methods = ['POST'])
def summarizationFromContent():
    request_data = request.get_json(force=True)
    content = request_data.get('content')

    summary = summarizeFromContent(content)

    response_body = {'summary':summary,'fromContent':True,'fromUrl':False}
    # resp = make_response(response_body)
    print(response_body)
    return response_body, 200, {'Access-Control-Allow-Origin':'*'}

@app.route('/summarization-from-URL',methods = ['POST'])
def summarizationFromURL():
    request_data = request.get_json(force=True)
    url = request_data.get('url')

    summary = summarizeFromURL(url)

    response_body = {'summary':summary,'fromContent':False,'fromUrl':True}
    print(response_body)
    return response_body, 200, {'Access-Control-Allow-Origin':'*'}
