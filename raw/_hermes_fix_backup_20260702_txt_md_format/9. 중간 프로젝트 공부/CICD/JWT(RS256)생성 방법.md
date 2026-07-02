git bash에서 openssl로 RSA 키 쌍을 만들기

\# 개인키 생성 (PKCS#8 형식)
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048

\# 개인키에서 공개키 추출
openssl rsa -pubout -in private.pem -out public.pem