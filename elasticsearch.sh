ENDPOINT='https://search-fide-sugcghmp4dyqfgc6yj4xotumje.us-east-1.es.amazonaws.com:443'
INDEX='test-201804'

# delete index
curl -XDELETE ${ENDPOINT}/test
curl -XDELETE ${ENDPOINT}/${INDEX}

# create index
curl -XPUT ${ENDPOINT}/${INDEX}?pretty -H 'Content-Type: application/json' --data-binary @mappings.json

# index ratings
curl -XPUT ${ENDPOINT}/${INDEX}/rating/_bulk -H "Content-Type: application/x-ndjson" --data-binary @201804-10000.ndjson

