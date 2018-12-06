자연어 이벤트 데이터
=============================

* 본 데이터는 자연어 분석 성능 향상 및 타 연구에서의 협업을 위한 Encoder/Decoder 데이터 셋으로 위키피디아를 기반으로 함
* 문장과 그 문장에 상응하는 지식이 하나의 데이터 단위가 됨
* 지식은 RDF triple 형태로 DBpedia namespace를 사용하여 표현
* Input으로 문장을 사용 하고, Target으로 그 문장에 상응하는 RDF triple 지식을 이용
* 데이터는 1,111,769건으로 텍스트 파일 형식
* 예시
```
Alabama is a state in the southeastern region of the United States.    <http://dbpedia.org/resource/Alabama> <http://dbpedia.org/ontology/country> <http://dbpedia.org/resource/United_States>
Greenwood also played  in the NASL for the Boston Minutemen.        <http://dbpedia.org/resource/Paddy_Greenwood> <http://dbpedia.org/ontology/team> <http://dbpedia.org/resource/Boston_Minutemen>
Robbah is a district in El Oued Province, Algeria.  <http://dbpedia.org/resource/Robbah_District> <http://dbpedia.org/ontology/country> <http://dbpedia.org/resource/Algeria>
```


run.py
=============================

* 텍스트 파일 형식의 오픈 데이터를 JSON 형식으로 변형해 주는 파일
* 본 파일은 python3 기반으로 구현함
* 사용법
```
1. data_name 파라미터에 오픈데이터명을 적는다.
2. save_name 파라미터에 저장 할 데이터명을 적는다. (JSON 형식)
3. python3 run.py 실행
```
* ```python3 run.py```를 실행하면 다음과 같은 JSON 형식의 OUTPUT이 생성
```
{
        "sentence": "Alabama is a state in the southeastern region of the United States.", // 지식 출처 문장
        "target": "<http://dbpedia.org/resource/Alabama> <http://dbpedia.org/ontology/country> <http://dbpedia.org/resource/United_States>" // 지식 출처 문장에 상응하는 RDF triple 형태의 지식
}
```


Acknowledgements
=============================
This work was supported by Institute for Information & communications Technology Promotion(IITP) grant funded by the Korea government(MSIT) (2017-0-01780, The technology development for event recognition/relational reasoning and learning knowledge based system for video understanding)




This data is licensed under the terms of the [Creative Commons Attribution-ShareAlike 3.0](https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License) license and the [GNU Free Documentation License](https://en.wikipedia.org/wiki/Wikipedia:Text_of_the_GNU_Free_Documentation_License).

