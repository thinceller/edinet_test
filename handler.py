import json
import subprocess
from edinet_xbrl.edinet_xbrl_downloader import EdinetXbrlDownloader


def index(event, context):
    xbrl_downloader = EdinetXbrlDownloader()

    ticker = 7203
    target_dir = "/tmp"

    xbrl_downloader.download_by_ticker(ticker, target_dir)

    result = subprocess.check_output(["ls", "-l", target_dir])
    print(result)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "result": result
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
