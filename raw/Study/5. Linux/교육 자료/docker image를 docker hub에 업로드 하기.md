내가 직접 build한 docker image를 docker hub에 올리는 방법
\------------------------------------------------------------------------------
직접 만든 Docker 이미지를 \*\*Docker Hub\*\*에 올리는 과정은 크게 4단계입니다.

🚀 전체 흐름

1️⃣ Docker Hub 계정 준비
2️⃣ 로그인
\# 이미지 태깅(tag)
\# 이미지 업로드(push)



docker container run --name commit-ctr -d -p 8090:80 httpd

docker cp ~/docker/commit/index04.html commit-ctr:/usr/local/apache2/htdocs/index.html
docker cp ~/docker/commit/image17_02.png commit-ctr:/usr/local/apache2/htdocs/image17_02.png


docker exec -it commit-ctr /bin/

\# 컨테이너 내부에서 텍스트 파일을 `/usr/local/apache2/htdocs` 디렉터리에 작성합니다.
echo "This is jeju test" > /usr/local/apache2/htdocs/jeju.txt

exit



참조 :
rktngusals를 여러 분의 계정으로 치환해 주세요.


1️⃣ Docker Hub 계정 생성
사이트: https://hub.docker.com
회원가입 후 로그인

👉 여기서 만든 username이 매우 중요 (이미지 이름에 들어감)

\# Docker Hub 로그인
docker login -u rktngusals@gmail.com

i Info → A Personal Access Token (PAT) can be used instead.
         To create a PAT, visit https://app.docker.com/settings


Password:   비밀 번호 입력

WARNING! Your credentials are stored unencrypted in '/home/broadcast/.docker/config.json'.
Configure a credential helper to remove this warning. See
https://docs.docker.com/go/credential-store/

👉 로그인 성공하면:

Login Succeeded 라고 보이면 성공


\# 이미지 태깅
내가 만든 이미지를 Docker Hub 형식으로 이름 변경해야 합니다.


📌 형식
jeju-img

docker tag [내이미지] [DockerHub아이디]/[이미지이름]:[버전]
docker tag jeju-img rktngusals/jeju-img:1.0


📌 예시
"jeju-img라는 로컬 이미지를 → rktngusals 계정의 jeju-img:1.0 이라는 이름으로 하나 더 등록한다"
docker tag jeju-img:latest rktngusals/jeju-img:latest

👉 의미

myapp:latest → 내가 만든 이미지
rktngusals/myapp:1.0 → Docker Hub에 올라갈 이름


\# 이미지 업로드(push)
docker push rktngusals/jeju-img:latest
The push refers to repository [도커 허브 리파지토리 주소]
855bcfc20616: Pushed
4f4fb700ef54: Mounted from library/wordpress
3531af2bc2a9: Mounted from library/httpd
d32ec5ee95cb: Mounted from library/httpd
b267b545226b: Mounted from library/httpd
5b16784cbecd: Mounted from library/httpd
1935f25c7dc4: Mounted from library/httpd
latest: digest: sha256:eb936a319226486fc0eb6c605ceda20f4cf6ec09a3ebf2f6a5dcb7f1e7c66c63 size: 1828




\# Docker Hub에서 확인
https://hub.docker.com/repositories/rktngusals


이미지 확인 가능


\# 다른 컴퓨터에서 실행
docker container run --name 컨테이너이름설정 -d -p 9100:80 도커이미지이름

Unable to find image '도커이미지이름:latest' locally
docker: Error response from daemon: pull access denied for jeju-img, repository does not exist or may require 'docker login'


docker container run --name jeju-librarian-ctr -d -p 9100:80 rktngusals/jeju-img


docker login -u 아이디

i Info → A Personal Access Token (PAT) can be used instead.
         To create a PAT, visit https://app.docker.com/settings


Password:

WARNING! Your credentials are stored unencrypted in '/home/librarian/.docker/config.json'.
Configure a credential helper to remove this warning. See
https://docs.docker.com/go/credential-store/

Login Succeeded <-- 비밀 번호 입력 성공하면 보입니다.







docker pull 도커허브_리파지토리_주소



💡 전체 명령어 한 번에 보기
\# 1. 로그인
docker login

\# 2. 이미지 확인
docker images

\# 3. 태깅
docker tag myapp:latest rktngusals/myapp:1.0

\# 4. 업로드
docker push rktngusals/myapp:1.0
⚠️ 자주 하는 실수

👉 ❌ 태깅 안 하고 push
→ 오류 발생

👉 ❌ username 틀림
→ 권한 에러

👉 ❌ private repo인데 권한 없음
→ push 실패

🔥 추가 팁
✔️ latest 태그도 같이 올리기
docker tag myapp:latest rktngusals/myapp:latest
docker push rktngusals/myapp:latest
📌 한 줄 정리

👉 docker tag로 이름을 Docker Hub 형식으로 바꾸고 → docker push 하면 업로드 완료

원하면
👉
private/public repository 차이
👉
GitHub Actions로 자동 배포 (CI/CD)
👉
Docker registry 자체 구축

까지 이어서 설명해드릴게요.
