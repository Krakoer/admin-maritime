import requests
import json
from models import Agent

def auth():
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        'Origin': 'http://127.0.0.1:8888',
        'Connection': 'keep-alive',
        'Referer': 'http://127.0.0.1:8888/login',
    }

    res = requests.post("http://127.0.0.1:8888/enter", data={"username": "admin", "password":"admin"}, headers=headers, allow_redirects=False)
    if res.status_code != 302:
        print("Error loging in")
        return
    return res.headers["Set-Cookie"].strip().split("\"")[1]

def create_op(name, auth_cookie):
    cookies = {
        'API_SESSION': f'"{auth_cookie}"',
    }
    json_data = {
        'name': name,
        'group': '',
        'adversary': {
            'adversary_id': '',
        },
        'auto_close': False,
        'state': 'running',
        'autonomous': 1,
        'planner': {
            'id': 'aaa7c857-37a0-4c4a-85f7-4e9f7f30e31a',
        },
        'source': {
            'id': 'ed32b9c3-9593-4c33-b0db-e2007315096b',
        },
        'use_learning_parsers': True,
        'obfuscator': 'plain-text',
        'jitter': '2/8',
        'visibility': '51',
    }

    response = requests.post('http://127.0.0.1:8888/api/v2/operations', cookies=cookies, json=json_data)
    if response.status_code != 200:
        print("Fail to create op")
        return
    try:
        data = json.loads(response.content)
    except Exception as e:
        print(f"Fail to parse create op repsonse : {e}")
        return

    return data["id"]

def run_command(command, auth_cookie, op_id, plateform, paw):
    cookies = {
        'API_SESSION': f'"{auth_cookie}"',
    }

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    #     'Accept': '*/*',
    #     'Accept-Language': 'en-US,en;q=0.5',
    #     'Referer': 'http://127.0.0.1:8888/?',
    #     'Origin': 'http://127.0.0.1:8888',
    #     'Connection': 'keep-alive',
    #     'Sec-Fetch-Dest': 'empty',
    #     'Sec-Fetch-Mode': 'cors',
    #     'Sec-Fetch-Site': 'same-origin',
    # }
    if plateform == 'linux':
        name = 'sh'
    elif plateform == 'windows':
        name = 'psh'

    json_data = {
        'paw': f'{paw}',
        'executor': {
            'name': f'{name}',
            'platform': f'{plateform}',
            'command': f'{command}',
        },
    }

    print("Sending: "+str(json_data))
    response = requests.post(f'http://127.0.0.1:8888/api/v2/operations/{op_id}/potential-links', cookies=cookies, json=json_data)
    if response.status_code != 200:
        print(f"Fail to add command {command} to op {op_id}")
        print(response)
        print(response.content)
        return

def get_agents(auth_cookie):
    """Get online agents
    
    Keyword arguments:
    argument -- auth cookie
    Return: dict of the for "paw': Agent()
    """
    
    agents = {}
    cookies = {
        'API_SESSION': f'"{auth_cookie}"',
    }

    response = requests.get("http://127.0.0.1:8888/api/v2/agents", cookies=cookies)
    if not response.status_code == 200:
        print("Could not fetch agents")
        return
    
    try:
        json_data = json.loads(response.content)
    except Exception as e:
        print(f"Couldnt parse json for agents: {e}")
        return

    for d in json_data:
        agents[d["paw"]] = Agent.from_dict(d)
    return agents

def main():
    c = caldera.auth()
    print(get_agents(c))

    

def main():
    cookie = auth()
    if not cookie:
        return
    op_id = create_op("couou", cookie)
    print(op_id)
    #run_command("whoami", cookie, op_id, "windows", "svidku")
    
if __name__ == "__main__":
    main()
