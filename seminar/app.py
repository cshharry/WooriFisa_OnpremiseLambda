import json
import boto3
from decimal import Decimal

# DynamoDB 리소스 생성
dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
table = dynamodb.Table('VoteResults')

# WebSocket 통신을 위한 API Gateway 클라이언트 생성
apig_management = boto3.client('apigatewaymanagementapi', endpoint_url='https://<your-websocket-endpoint>')

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

def lambda_handler(event, context):
    try:
        # WebSocket connectionId 추출
        connection_id = event['requestContext']['connectionId']

        # 요청 바디에서 데이터 추출
        body = json.loads(event.get('body', '{}'))
        candidate = body.get('candidate')

        if not candidate:
            return {'statusCode': 400, 'body': json.dumps('Candidate parameter is required')}

        # DynamoDB에 투표 데이터 저장
        table.update_item(
            Key={'candidate': candidate},
            UpdateExpression='ADD votes :incr',
            ExpressionAttributeValues={':incr': 1}
        )

        # 전체 투표 결과 조회
        response = table.scan()
        results = response['Items']

        # WebSocket 연결을 통해 실시간 결과 전송
        apig_management.post_to_connection(
            ConnectionId=connection_id,
            Data=json.dumps(results, default=decimal_default)
        )

        return {'statusCode': 200, 'body': 'Vote recorded and result sent'}

    except apig_management.exceptions.GoneException:
        print(f"Connection {connection_id} is gone.")
        return {'statusCode': 410, 'body': 'Connection not found'}

    except Exception as e:
        print(f"Error: {str(e)}")
        return {'statusCode': 500, 'body': 'Internal server error'}

