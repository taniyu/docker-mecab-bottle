from bottle import route, HTTPResponse, default_app
import MeCab
import json

@route('/mecab-neologd/<sentence:path>')
def mecab_neologd(sentence):
    mecab = MeCab.Tagger('-d /usr/lib/mecab/dic/mecab-ipadic-neologd')
    result = '\n'.join(mecab.parse(sentence).split('\n')[0:-2])
    r = HTTPResponse(status=302, body=json.dumps({ 'result':result }, ensure_ascii=False))
    r.set_header('Content-Type', 'application/json')
    return r

@route('/mecab/<sentence:path>')
def mecab(sentence):
    mecab = MeCab.Tagger()
    result = '\n'.join(mecab.parse(sentence).split('\n')[0:-2])
    r = HTTPResponse(status=302, body=json.dumps({ 'result':result }, ensure_ascii=False))
    r.set_header('Content-Type', 'application/json')
    return r

app = default_app()
