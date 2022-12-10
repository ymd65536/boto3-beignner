
def get_cloudwatch_alarm_tags(session, arn):
    """
    CloudWatchAlarm のタグ情報を取得します
    :param session: セッション
    :return: CloudWatchAlarm のタグ情報
    """
    r = session.client("cloudwatch").list_tags_for_resource(
        ResourceARN=arn
    )

    return r


def describe_cloudwatch_metric_alarms(session):

    r = session.client("cloudwatch").describe_alarms(
        AlarmTypes=['MetricAlarm'],
    )
    # キーが存在するかどうかを調べる
    if "NextToken" in r:

        next_token = r["NextToken"]
        has_next_token = True

        # NextTokenが返ってくる間はメソッドを繰り返し実行する
        while has_next_token:

            next_data = session.client("cloudwatch").describe_alarms(
                    AlarmTypes=['MetricAlarm'],
                    NextToken=next_token
                )

            # メトリクスデータを追加する
            r["MetricAlarms"].extend(next_data["MetricAlarms"])

            # NextTokenが存在する場合
            if "NextToken" in next_data:
                next_token = next_data["NextToken"]
            else:
                has_next_token = False
    return r

