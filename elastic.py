
from elasticsearch import Elasticsearch
import json

es = Elasticsearch([{'host': 'http://192.168.32.10', 'post': 9200}])

document = '{"file_name": "page1.html", "content": "blablablablablabla"}'

json_doc = json.loads(document)

es.put_template(json_doc)
