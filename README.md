# docker-mecab-bottle
## 説明
docker と bottle を使ったmecabのAPI

```
docker build -t taniyu/docker-mecab-bottle .
docker run --rm -p 3000:3000 taniyu/docker-mecab-bottle
```

mecab/  
mecab-neologd/  

以下のURLに対して下記のように実行することで結果を取得できる。  
例  
mecab?sentence=abc  
mecab-neologd?sentence=abc  

resultの中に、解析結果がそのまま入っている。
