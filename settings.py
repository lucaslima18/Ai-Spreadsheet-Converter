import argparse

parser = argparse.ArgumentParser(description="Um programa de exemplo.")
parser.add_argument("--repository_uuid", required=True, type=str)
parser.add_argument("--auth_token", required=True, type=str)
parser.add_argument("--service", required=True, type=str)
arguments = parser.parse_args()

REPOSITORY_UUID = arguments.repository_uuid
LANGUAGE = "pt_br"
AUTH_TOKEN = arguments.auth_token

if (
    arguments.service == "tests"
    or arguments.service == "examples"
    or arguments.service == "categorize"
):
    SERVICE_TYPE = arguments.service

else:
    print("This option is not avaliable, please reload and try one of this options:\n")
    print("tests\nexamples\ncategorize")


