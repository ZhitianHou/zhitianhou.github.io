"""Start a loopback-only Mihomo proxy using nodes from an Actions secret."""
import json
import base64
import gzip
import os
from pathlib import Path
import subprocess
import time
import urllib.request
import yaml
import requests

root = Path(os.environ['RUNNER_TEMP']) / 'scholar-proxy'
root.mkdir(mode=0o700, exist_ok=True)
nodes = yaml.safe_load(gzip.decompress(base64.b64decode(os.environ['CLASH_CONFIG']))).get('proxies', [])
nodes = [node for node in nodes if node.get('name') == '🇭🇰|香港家宽-中转 01']
if not nodes:
    raise SystemExit('CLASH_CONFIG contains no proxy nodes')
# Discard local settings, controllers, rules and subscriptions from the supplied config.
config = {'mixed-port': 7890, 'allow-lan': False, 'bind-address': '127.0.0.1',
          'external-controller': '127.0.0.1:9090', 'mode': 'rule', 'log-level': 'silent',
          'proxies': nodes, 'proxy-groups': [{'name': 'SCHOLAR', 'type': 'select',
          'proxies': [n['name'] for n in nodes]}], 'rules': ['MATCH,SCHOLAR']}
path = root / 'config.yaml'
path.write_text(yaml.safe_dump(config, allow_unicode=True), encoding='utf-8')
path.chmod(0o600)
# Run only the trusted official release downloaded by the workflow.
log = (root / 'proxy.log').open('w')
process = subprocess.Popen([str(root / 'mihomo'), '-d', str(root), '-f', str(path)],
                           stdout=log, stderr=log, start_new_session=True)
(root / 'pid').write_text(str(process.pid))
control = requests.Session()
control.trust_env = False
for _ in range(30):
    try:
        control.get('http://127.0.0.1:9090/version', timeout=1).raise_for_status()
        break
    except requests.RequestException:
        time.sleep(1)
else:
    raise SystemExit('Proxy failed to start; configuration details withheld')
probe = requests.Session()
probe.trust_env = False
probe.proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}
# Bound testing to limit load and avoid printing private node names or endpoints.
for index, node in enumerate(nodes[:20], 1):
    control.put('http://127.0.0.1:9090/proxies/SCHOLAR', json={'name': node['name']}, timeout=3).raise_for_status()
    try:
        response = probe.get('https://scholar.google.com.hk/citations',
                             params={'user': os.environ['GOOGLE_SCHOLAR_ID'], 'hl': 'en'}, timeout=12)
        if response.status_code == 200 and 'gsc_prf_in' in response.text:
            print(f'Proxy candidate {index}: Scholar profile accessible', flush=True)
            break
        print(f'Proxy candidate {index}: HTTP {response.status_code}, profile unavailable', flush=True)
    except requests.RequestException:
        print(f'Proxy candidate {index}: connection failed', flush=True)
else:
    raise SystemExit('No tested proxy could retrieve the Scholar profile')
