# Lambda Python 3.9 기본 이미지 사용
FROM public.ecr.aws/lambda/python:3.9

# Lambda 함수 코드 및 라이브러리 복사
COPY app.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt ./

# 의존성 설치
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Lambda 핸들러 설정
CMD ["app.lambda_handler"]


