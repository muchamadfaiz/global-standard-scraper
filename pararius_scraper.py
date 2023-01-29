import codetiming
import httpx
from selectolax.parser import HTMLParser

t = codetiming.Timer(name="execTime")
t.start()

HEADERS = {
'authority': 'www.pararius.com',
'method' : 'GET',
'path': '/apartments/groningen/page-2',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
'cache-control': 'max-age=0',
'cookie': 'fl_mgc=JwkreXJDVBIUTbrvtAgrasJrsVFHOouuARVdtaahpiztOVRq; fl_d_p_v2_a=QACTIHYPQ2BSFURFVOYLXRSIDEOXDOJK; fl_pass_v2_b=eyJhbGciOiJkaXIiLCJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwidHlwIjoiSldUIn0..ZEsv3I9FhJMDYlmXSIyU6A.-eoGgJ12Z6pMDLukROIUqdjy5hhgD425qUKNe_RkJD08za16T4No1Tno6Azo6VyyTK4UucUHhl8uVMxD629Y12J3va85s_QdHKSKbmAgSgqm5JfYzWeIxdOh1kIbygbSVvlHbPlKbuz52D-mOpQ7zkVNH4cabIffFA2371iwMXpzB-tLyAQe9BCykQErrDqbD7IgxN3eaLxqwpka2OpR4KdaZ8yjDLRpMtCD36v9sddaPCvjop-EBrYqQ4X4HgxI7d9fK6nfzTJMIn-dltWLgwaZQJt5ZJYrae-6lQ8eAUovSd8wEIm7CT0qOU3xue98oYaEjdOd8YiHiyTSsLNl_brGmPAPFhtudt1BUO251Q7tUVd5WLk2lN4lscPPV0GPLIvEIz9PbrE6Yixdw83ZeCYnURfG5mYMxztp8q3Ccz1v935Fk_zKFhhPs4_ikXTcMBnlMouYY19x5X-5ycCI0SyA2oBLXrkC1mCMmXYTMteYcJaqVygbaKu3CEcIQA3hVQUZ97FzQMm45hejZNnoCaEDIsqyspEcpjHqLUx7exFBpvnTWYP64YGVzASJx5wSAbDOZyAqKXdnztBU3z--9uJStkeePew3uXxi6F__EVN310umgEwYoUZnzRcOeeSJHt8EVeZQJa9bqRcvHk0JnDdOaN4EZQIlTxeSBhjimtGAnF6AIfSK2fc8Qc28WJdlBCOPmXEt05W9Cmk0U0qkLRE5u5ZEjbJusGPsAX-wWaG9zkqE2VTS5ePfwNJQYvZET9i_hzKzL8vzxQL6ayoae6-0jS0NzI-SRaWWp5PzZFE.rxTzcWWwJX5BAOCOdW2DSDf0ANBYOn6mX3kUrvmyLws; _gid=GA1.2.1663060850.1674903053; OptanonAlertBoxClosed=2023-01-28T10:57:41.565Z; eupubconsent-v2=CPmUfu6PmUfu6AcABBENC1CsAP_AAH_AAChQfstf_X__b2_r-_5_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF36tq4KuR4ku3LBIUdlHPHcTUmw6okVryPsbk2cr7NKJ7PEmnMbOydYGH9_n1_z-ZKY7___f_7z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYJNgEmGrcQBdmWODNtGEUCIEYVhIdQKACigGFogMIHVwU7K4CfWECABAKAJwIgQ4AowYBAAAJAEhEQEgR4IBAARAIAAQAKhEIAGNgEFgBYGAQACgGhYoxQBCBIQZEBEUpgQFSJBQT2VCCUH-hphCHWWAFBo_4qEBGsgYrAiEhYOQ4IkBLxZIHmKN8gBGAFAKJUK1FJ6aAA.f_gAD_gAAAAA; _fbp=fb.1.1674903462112.236929863; __gads=ID=f18cbdbfdcf6dd70:T=1674903462:S=ALNI_MZofb2ml5PYkmAmVxg4ja5d-upuSQ; __gpi=UID=00000baf2e443b25:T=1674903462:RT=1674903462:S=ALNI_MYmTToasCmH1N28eUK68sJoRggotw; latest_search_locations=%5B%22amsterdam%22%2C%22groningen%22%5D; _ga=GA1.2.1545976896.1674903053; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Jan+28+2023+19%3A21%3A51+GMT%2B0700+(Indochina+Time)&version=6.27.0&isIABGlobal=false&hosts=&consentId=6059ee61-07a4-46bd-a797-10452ee09ded&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CSTACK42%3A1&AwaitingReconsent=false&geolocation=ID%3BJK; _ga_YCYTBWR959=GS1.1.1674908510.2.0.1674908512.0.0.0',
'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

for page in range (2,3):
    print(f"page {page}")
    url = f"https://www.pararius.com/apartments/groningen/page-{page}"
    req = httpx.get(url, headers=HEADERS)
    html = HTMLParser(req.text)
    selector = ".listing-search-item__title"
    text = html.css(selector)

    for a in text:
        print(a.text().strip())

t.stop()