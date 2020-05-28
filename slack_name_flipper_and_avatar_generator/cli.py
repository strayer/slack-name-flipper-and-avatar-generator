import humanize

from . import avatar
from . import name
from . import slack


def main():
    flipped_name = name.flip_name()
    random_avatar_svg = avatar.download_random_avatar()
    random_avatar_png = avatar.svg_to_png(random_avatar_svg)

    print(f"New name: {flipped_name}")
    print(f"New avatar: PNG {humanize.naturalsize(len(random_avatar_png))}")
    print("---")

    slack.update_profile_name(flipped_name)
    print("Name updated in Slack")
    slack.update_avatar(random_avatar_png)
    print("Avatar updated in Slack")

    print("Bye!")
