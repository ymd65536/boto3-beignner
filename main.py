import boto3


# entry point
if __name__ == '__main__':

    # バージョン表示
    print(f'boto3 version: {boto3.__version__}')

    boto3_ver = f'boto3 version: {boto3.__version__}'

    if boto3_ver == "boto3 version: 1.17.32":
        print("session start")
        session = boto3.Session(region_name=DEFAULT_REGION)

        r = describe_cloudwatch_metric_alarms(session=session)

