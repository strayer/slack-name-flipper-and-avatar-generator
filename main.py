#!/usr/bin/env python3
import humanize

import avatar
import name
import slack

if __name__ == "__main__":
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

