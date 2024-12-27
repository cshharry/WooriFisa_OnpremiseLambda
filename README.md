
# On Premise 환경에서 AWS Lambda 기능 구현하기 🚀

## 목차 📚
1. [개요](#개요-🌟)
2. [아키텍처 설명 및 흐름](#아키텍처-설명-및-흐름-🏗️)
3. [Lambda 호출 실습](#lambda-호출-실습-🔧)
4. [활용 사례](#활용-사례-🌐)
5. [결론](#결론-🏁)

---

## 개요 🌟

온프레미스 환경에서 AWS Lambda를 활용하여 **서버리스 컴퓨팅**의 장점을 도입하는 방법을 소개합니다.  
**온프레미스 환경의 안정성과 통제력**을 유지하면서도, **클라우드의 확장성과 유연성**을 결합할 수 있는 방법론을 탐구합니다.

---

## 아키텍처 설명 및 흐름 🏗️

AWS Lambda를 온프레미스 환경에 도입하기 위한 주요 구성 요소:

1. **WebSocket API Gateway**: 클라이언트 요청 데이터 전달  
2. **Docker 컨테이너**: Lambda 함수의 패키징 및 실행  
3. **DynamoDB**: 데이터 저장 및 조회  
4. **클라이언트**: 실시간 데이터 수신 및 결과 처리  

이 구성 요소들을 통해 온프레미스 환경에서도 클라우드와 유사한 서버리스 아키텍처를 구축할 수 있습니다.

---

## Lambda 호출 실습 🔧

### 필요 도구 🛠️
- **AWS 계정**: DynamoDB, API Gateway 설정
- **Docker**: Lambda 컨테이너 이미지 빌드 및 실행
- **Python**: Lambda 함수 작성

### 구현 단계 📋
1. **DynamoDB 테이블 생성**  
   - 테이블 이름: `VoteResults`
   - 파티션 키: `candidate`

2. **WebSocket API Gateway 설정**  
   - 라우팅 키: `vote-lambda-app`

3. **Lambda 함수 작성**  
   - 클라이언트 요청 데이터를 DynamoDB에 저장 및 결과 반환

4. **Dockerfile 작성**  
   ```dockerfile
   FROM public.ecr.aws/lambda/python:3.9
   COPY app.py ${LAMBDA_TASK_ROOT}
   COPY requirements.txt ./
   RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
   CMD ["app.lambda_handler"]
   ```

5. **컨테이너 이미지 빌드 및 실행**  
   ```bash
   docker build -t vote-lambda-app .
   docker run -p 9000:8080 vote-lambda-app
   ```

---

## 활용 사례 🌐

1. **금융 서비스** 💳: 자동화된 거래 시스템, 위험 관리 등  
2. **헬스케어 및 생명과학** 🏥: 민감한 데이터 처리 및 분석  
3. **정부 및 공공 부문** 🏛️: 데이터 주권 및 규제 준수 환경에서의 대규모 분석  

---

## 결론 🏁

AWS Lambda 컨테이너는 온프레미스와 클라우드 환경의 장점을 결합하여,  
유연성과 확장성을 제공하는 **하이브리드 아키텍처** 구현에 적합한 솔루션입니다.  
이를 통해 기업은 클라우드로의 전환을 점진적으로 진행할 수 있습니다.

---
