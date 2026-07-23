git bash에서 openssl로 RSA 키 쌍을 만들기
Git 설치시 Git Bash에서 사용할 수 있는 여러 리눅스 명령어와 함께 openssl.exe도 함께 설치됨
그래서 일반 cmd창 말고 git bash에서 실행하는게 좋음
일반 cmd에서 실행하려면 openssl.ext 경로를 설정해줘야함
(OpenSSL : 다양한 암호 기술을 제공하는 암호화 도구이자 라이브러리)

\# 개인키 생성 (PKCS#8 형식)
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048

\# 개인키에서 공개키 추출
openssl rsa -pubout -in private.pem -out public.pem
