import requests
import cairosvg
import random
import string

TINYGRAPHS_URL = "https://www.tinygraphs.com/labs/isogrids/hexa16/__TERM__?theme=seascape&numcolors=4"


def download_random_avatar():
    randstr = random_string(20)
    url = TINYGRAPHS_URL.replace("__TERM__", randstr)

    r = requests.get(url)
    r.raise_for_status()

    return r.content


def svg_to_png(svg_data):
    return cairosvg.svg2png(bytestring=svg_data, output_width=1024, output_height=1024)


def random_string(size):
    return "".join(random.choice(string.ascii_letters) for _ in range(size))
