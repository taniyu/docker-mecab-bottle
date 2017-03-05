# docker-mecab-bottle
## 説明
docker と bottle を使ったmecabのAPI

```
docker build -t taniyu/docker-mecab-bottle .
docker run --rm -p 3000:3000 taniyu/docker-mecab-bottle
```

mecab/  
mecab-neologd/  

それぞれ後ろに、つけた文字列を形態素解析した結果を返却する。  
例  
mecab/ほげ  
mecab-neologd/ほげ  

resultの中に、解析結果がそのまま入っている。
