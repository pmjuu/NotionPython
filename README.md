# Notion - Python API 활용하기
참고자료 [Unofficial Python 3 client for Notion.so API v3](https://github.com/jamalex/notion-py)
### 추가 설명
MY_TOKEN 은 개별적으로 발급받으면 됩니다.   
(크롬 개발자 도구 - Application - Cookies - token_v2의 Value값 복사)   
보안상 문제 때문에 저는 .gitignore 처리한 `MY_TOKEN.txt`에 따로 저장해놓고 불러왔습니다.

### 트러블 슈팅 기록
SSL Error `can't connect to https url because the ssl module is not available.`   
=> 시스템 환경 변수 편집 - path 추가
```
C:\Anaconda3
C:\Anaconda3\Scripts
C:\Anaconda3\Library\bin
```