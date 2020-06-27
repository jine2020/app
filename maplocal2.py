import json


def response(flow):
    if "quote.json" in flow.request.pretty_url:
        data = json.loads(flow.response.content)
        data['data']['items'][0]['quote']['name']='天地壹号001'
        data['data']['items'][1]['quote']['name'] = '天地壹号002'
        data['data']['items'][1]['quote']['current'] = 9999
        flow.response.text=json.dumps(data)