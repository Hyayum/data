import requests
import re
import json

res = requests.get("https://gitlab.com/Dimbreath/AnimeGameData/-/raw/master/TextMap/TextMapJP.json")    # でかすぎ
text_map = res.json()

res = requests.get("https://raw.githubusercontent.com/EnkaNetwork/API-docs/master/store/characters.json")
chara_list = res.json()

result = {}
for id, data in chara_list.items():
    name = re.search(r"^UI_AvatarIcon_Side_(.+)$", data["SideIconName"])[1]
    text_id = str(data["NameTextMapHash"])
    jp_name = text_map[text_id]
    if name not in result:
        result[name] = jp_name

with open("./enka_chara_map.json", "w") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
