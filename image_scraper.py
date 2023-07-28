import os
import urllib.request, urllib.error
from setup import region_ids, card_counts, sets

base_url = "https://cdn-lor.mobalytics.gg/production/images/"
images_path = os.path.abspath("/home/logan/Documents/webscraper/images_dump")

def format_card_url(base: str,set: str,region: str,id: str) -> str:
    return "".join([base,"set",set,"/en_us/img/card/game/",set.zfill(2),region,id,"-full.png"])


def download_image_from_url(url,name):
    try:
        return urllib.request.urlretrieve(url,name)
    except(urllib.error.HTTPError):
        ...
        #print("Image not found")
    except:
        ...
        #print("Unknown error occurred downloading the image")

def download_images_from_urls(urls: list,names: list):
    for url,name in zip(urls,names):
        download_image_from_url(url,name)


def download_ionian_package():
    urls = []
    names = []
    base = base_url
    region = region_ids["Ionia"]
    for set_num in sets:
        #print(set_num)
        for id in range(1,100):
            urls.append(
                format_card_url(base,str(set_num),region,str(id).zfill(3))
            )
            names.append(
                "".join(["images_dump/image-set",str(set_num),"-",str(region),"-",str(id).zfill(3),".png"])
            )

    #print(len(urls))
    download_images_from_urls(urls,names)
    
def main():
    download_ionian_package()

if __name__ == "__main__":
    main()