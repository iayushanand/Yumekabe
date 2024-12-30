import os
import platform
import shutil

os_name = platform.system()

categ = {
    'abs': 'abstract',
    'liv': 'animated',
    'ani': 'anime',
    'col': 'colorful',
    'dar': 'dark',
    'dig': 'digital art',
    'fan': 'fantasy',
    'gam': 'games',
    'min': 'minimalist',
    'spa': 'space',
    'tec': 'technology'
}

# move files to their respective folders

for file in os.listdir("dump"):
    file_categ = file.split(".")[0][-3:]
    try:
        moveto = categ[file_categ]
    except KeyError:
        moveto = "other"
    
    shutil.move(f"./dump/{file}", f"./wallpapers/{moveto}")
    if not moveto == "other":
        os.rename(f"./wallpapers/{moveto}/{file}", f"./wallpapers/{moveto}/{file.split(".")[0][:-4]}.{file.split(".")[1]}")


# update readme file

pre_text = """
# welcome to my personal wallpaper dump
(inspired by [flicko](https://github.com/flickowoa/kabegami))

## previews
<hr>
<p align="center">


"""

post_text = """
</p>
"""

with open("README.md", "w") as readme:
    dump_text = ""
    dump_text+=pre_text
    for category in os.listdir("wallpapers"):
        if category == "other": continue
        dump_text+=f"## {category}\n"
        dump_text+="<details><summary></summary>\n"
        for img in os.listdir(f"wallpapers/{category}"):
            dump_text+=f"""<img src="./wallpapers/{category}/{img}" title = "{img.split(".")[0]}"><br>\n"""
        dump_text+="</details>\n\n"
    dump_text+=f"{post_text}"
    readme.write(dump_text)