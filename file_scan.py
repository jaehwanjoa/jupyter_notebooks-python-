from OTXv2 import OTXv2, IndicatorTypes
import os
import pandas as pd
import urllib.request
import json

#file = input('Input IoC Filehash Entity: ')
file = input('Input IoC Filehash(MD5) Entity: ')

# results OTX Threat Intelligence Entity
otx = OTXv2('2c5cf84144f2052145bee430b136da40757637989a7c6cfddb08e059377d5cad')
indicators1 = otx.get_indicator_details_full(IndicatorTypes.FILE_HASH_MD5, file)
print('===============================OTX TI Detection===============================')
print('fileinfo: ', pd.DataFrame(indicators1['analysis']['analysis']['info']))
print('related_pulse: ', pd.DataFrame(indicators1['general']['pulse_info']['related']))

# results VirusTotal Threat Intelligence Entity
url = "https://www.virustotal.com/api/v3/files/%s" % (file)
headers = {
    'accept' : 'application/json',
    'x-apikey' : 'e37f2e31aed5ea0cd706bc48be41b8c28fcdceace4d910b57b82be3ce601501b'
}
req = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(req)
jsonResponse = json.loads(res.read())
results = jsonResponse["data"]
print('===============================VT TI Detection===============================')
print(pd.DataFrame(results['attributes']['last_analysis_results']))
os.system('pause')
