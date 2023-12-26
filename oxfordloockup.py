import requests
import json
app_id='8d671525'
app_key='b66074deba0d1127ca08b8d7c022d26a'

language = 'en-gb'


def get_definitions(word_id):
    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower()
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    res=r.json()
    if 'error' in res.keys():
        return False
    output={}
    try:
        senses=res["results"][0]['lexicalEntries'][0]['entries'][0]['senses']
        definitions=[]
        for sense in senses:
            definitions.append(f"👉{sense['definitions'][0]}")
        output['definition']="\n".join(definitions)
        if res["results"][0]['lexicalEntries'][0]['entries'][0]["pronunciations"][0].get("audioFile"):
            output['audio']=''.join(res["results"][0]['lexicalEntries'][0]['entries'][0]["pronunciations"][0]["audioFile"])
        return output
    except KeyError:
        return False


if __name__=='__main__':
    from pprint import pprint as print
    print(get_definitions('word'))