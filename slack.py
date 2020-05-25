import requests
import json
import os

SESSION = requests.Session()
SESSION.headers.update(
    {"Authorization": "Bearer " + os.environ["SLACK_TOKEN"],}
)


def update_profile_name(name):
    r = SESSION.post(
        "https://slack.com/api/users.profile.set",
        headers={"Content-Type": "application/json; charset=utf-8",},
        data=json.dumps(
            {
                "profile": {
                    "first_name": name.split(" ")[0],
                    "last_name": name.split(" ")[1],
                }
            }
        ),
    )
    r.raise_for_status()
    if not r.json()["ok"]:
        print(r.json())
        raise Exception("Slack API error")


def update_avatar(png):
    r = SESSION.post("https://slack.com/api/users.setPhoto", files={"image": png},)
    r.raise_for_status()
    if not r.json()["ok"]:
        print(r.json())
        raise Exception("Slack API error")
