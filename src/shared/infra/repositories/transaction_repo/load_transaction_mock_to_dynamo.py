from decimal import Decimal

import boto3
import dotenv
from src.shared.infra.repositories.transaction_repo.transaction_repository_dynamo import TransactionRepositoryDynamo
from src.shared.infra.repositories.transaction_repo.transaction_repository_mock import TransactionRepositoryMock
from src.shared.environments import Environments


def setup_dynamo_table():
    dynamo_table_name = "transaction_mss_template-table"
    endpoint_url = "http://localhost:8000"
    print("Setting up DynamoDB table...")

    dynamo_client = boto3.client('dynamodb', endpoint_url=endpoint_url)
    print("DynamoDB client created")
    tables = dynamo_client.list_tables()['TableNames']

    if dynamo_table_name not in tables:
        print("Creating table...")
        dynamo_client.create_table(
            TableName=dynamo_table_name,
            KeySchema=[
                {
                    'AttributeName': 'PK',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'SK',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'PK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'SK',
                    'AttributeType': 'S'
                }

            ],
            BillingMode='PAY_PER_REQUEST',
        )
        print("Waiting for table to be created...")
        dynamo_client.get_waiter('table_exists').wait(TableName=dynamo_table_name)

        print('Loading table...')

        dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)

        table = dynamodb.Table(dynamo_table_name)

        print("Adding counter to table")

        table.put_item(
            Item={
                'PK': 'COUNTER',
                'SK': 'COUNTER',
                'COUNTER': Decimal(0)
            }
        )

        print('Table "transaction_mss_template-table" created!')

    else:
        print("Table already exists!")


def load_mock_to_local_dynamo():
    setup_dynamo_table()
    mock_repo = TransactionRepositoryMock()
    dynamo_repo = TransactionRepositoryDynamo()

    count = 0

    print('Loading mock data to dynamo...')
    for transaction in mock_repo.transactions:
        print(f"Post transaction {transaction.current_balance} | {transaction.value} to dynamo")
        dynamo_repo.post_transaction(transaction)
        count += 1

    print(f"{count} transactions loaded to dynamo!")


def load_mock_to_real_dynamo():
    mock_repo = TransactionRepositoryMock()
    dynamo_repo = TransactionRepositoryDynamo()

    count = 0

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(dynamo_table_name=Environments.get_envs().dynamo_table_name)

    print("Adding counter to table")

    table.put_item(
        Item={
            'PK': 'COUNTER',
            'SK': 'COUNTER',
            'COUNTER': Decimal(0)
        }
    )

    print('Loading mock data to dynamo...')
    for transaction in mock_repo.transactions:
        print(f"Post transaction {transaction.current_balance} | {transaction.name} to dynamo")
        dynamo_repo.post_transaction(transaction)
        count += 1

    print(f"{count} transactions loaded to dynamo!")


if __name__ == '__main__':
    dotenv.load_dotenv()
    load_mock_to_local_dynamo()
