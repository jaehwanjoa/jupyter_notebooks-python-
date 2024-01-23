from OTXv2 import OTXv2, IndicatorTypes
import os
import pandas as pd

API_KEY = 'Input OTX API Key'
otx = OTXv2(API_KEY)

# Input Threat Intelligence Entity
ip = input('Input IoC IP Entity: ')

indicators1 = otx.get_indicator_details_full(IndicatorTypes.IPv4, ip)
indicators = otx.get_indicator_details_by_section(IndicatorTypes.IPv4, ip, section='general')

# Results IP list
print('Country_Name: '+indicators['country_code'])
print('IP_Info: ', pd.DataFrame.from_dict(indicators['base_indicator'], orient='index'))
print('ASN_Info: ', indicators['asn'])
print('IP_Related_Pulses_Info: ', pd.DataFrame(indicators['pulse_info']['pulses']))
print('정상적으로 스캔하였습니다.')
os.system('pause')
