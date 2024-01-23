from OTXv2 import OTXv2, IndicatorTypes
import os
import pandas as pd
import urllib.request
import json

#file = input('Input IoC Filehash Entity: ')
file = input('Input IoC Filehash(MD5) Entity: ')

# results OTX Threat Intelligence Entity
otx = OTXv2('input OTX key')
indicators1 = otx.get_indicator_details_full(IndicatorTypes.FILE_HASH_MD5, file)
print('===============================OTX TI Detection===============================')
print('fileinfo: ', pd.DataFrame(indicators1['analysis']['analysis']['info']))
print('related_pulse: ', pd.DataFrame(indicators1['general']['pulse_info']['related']))

# results VirusTotal Threat Intelligence Entity
url = "https://www.virustotal.com/api/v3/files/%s" % (file)
headers = {
    'accept' : 'application/json',
    'x-apikey' : 'Input VT API Key'
}
req = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(req)
jsonResponse = json.loads(res.read())
results = jsonResponse["data"]
print('===============================VT TI Detection===============================')
print(pd.DataFrame(results['attributes']['last_analysis_results']))
os.system('pause')
