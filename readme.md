### Python API Print Server Project

목표 : 원격 서버 (컴퓨터2)에서 API를 통해 업로드된 파일을 자동 인쇄  
기능  
1. cache 폴더로 업로드된 파일 인쇄.
2. 업로드된 파일을 자동으로 삭제.
3. 업로드된 파일을 카피하여 storage에 저장

API 요청   
1. 파일 업로드
- TYPE : POST
- URL : http://localhost:8000/upload/{file_name}
- PARAMETER : file