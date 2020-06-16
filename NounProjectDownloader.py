#firstly, you should pip3 install TheNounProjectAPI
#limit is 5000/month

# See the Documentation for more information: https://cubiedev.github.io/TheNounProjectAPI
from TheNounProjectAPI import API
import requests
import os

key = "3ab6a7987aa7402392db036cd5ddd84e"
secret = "06844e2ec5c04130a217803cfe949778"

def getImage(query = 'Dog', limit = 3, storePath = 'dataset/'):

    # Create api object
    api = API(key=key, secret=secret)

    # See the documentation for more endpoints
    icons = api.get_icons_by_term(query, public_domain_only=True, limit=limit)

    # >>>icons
    # [<IconModel: Term: Goat Feeding, Slug: goat-feeding, Id: 24014>,
    # <IconModel: Term: Herbivore teeth, Slug: herbivore-teeth, Id: 675870>]

    tmpPath = storePath + '/' + query
    if not os.path.exists(tmpPath):
        os.makedirs(tmpPath)

    count = 0
    for icon in icons:
        print("Icon's term:", icon.term)
        tags = ", ".join(tag.slug for tag in icon.tags)
        print("This icon's tags:", tags)
        #print("Uploader's username:", icon.uploader.username)
        print(icon.preview_url)

        #get the preview png
        r = requests.get(icon.preview_url)

        filePath = tmpPath + '/' + str(count) + '.png'
        print(filePath)
        count = count + 1

        with open(filePath, 'wb') as f:
            f.write(r.content)

getImage('technology', 7, 'dataset/')
