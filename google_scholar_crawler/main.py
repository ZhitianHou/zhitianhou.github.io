from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
if os.environ.get('SCHOLAR_PROXY_URL'):
    pg = ProxyGenerator()
    pg.SingleProxy(http=os.environ['SCHOLAR_PROXY_URL'], https=os.environ['SCHOLAR_PROXY_URL'])
    scholarly.use_proxy(pg, pg)

print('Fetching Google Scholar author profile...', flush=True)

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
print('Author profile retrieved; fetching citation counts and publications...', flush=True)
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
