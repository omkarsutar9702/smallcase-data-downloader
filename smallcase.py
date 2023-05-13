#%%
import requests
import pandas as pd
#%%

url = "https://gatewayapi.smallcase.com/v1/omkaer/engine/smallcases?sortBy=default&sortOrder=1&count=100&offset=0"

headers = {
    "accept": "application/json",
    "x-gateway-secret": "gatewayDemo_secret",
    "x-gateway-authtoken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJndWVzdCI6dHJ1ZSwiaWF0IjoxNjU0MzIxMDAwfQ.qiZ_w1yFYXhkdLMlqI28XJOXitfZwr64e2oL-lMEHZU"
}

response = requests.get(url, headers=headers)

response = response.json()
# %%
## get name of the smallcase
Name = []
for smallcase in response['data']['smallcases']:
    name = smallcase['info']['name']
    Name.append(name)
print(Name)

publisherName = []
for i in response['data']['smallcases']:
    publisher = i['info']['publisherName']
    publisherName.append(publisher)
print(publisherName)

created =[]
for i in response['data']['smallcases']:
    create = i['info']['created']
    created.append(create)
print(created)

rebalanceschedule =[]
for i in response['data']['smallcases']:
    rebalance = i['info']['rebalanceSchedule']
    rebalanceschedule.append(rebalance)
print(rebalanceschedule)

Monthlyreturns = []
for i in response['data']['smallcases']:
    month = i['stats']['returns']['monthly']
    Monthlyreturns.append(month)
print(Monthlyreturns)

halfyearly = []
for i in response['data']['smallcases']:
    halfyear = i['stats']['returns']['halfyearly']
    halfyearly.append(halfyear)
print(halfyearly)

fullyearly = []
for i in response['data']['smallcases']:
    year = i['stats']['returns']['halfyearly']
    fullyearly.append(year)
print(fullyearly)


threeyear = []
for i in response['data']['smallcases']:
    threeyr = i['stats']['returns']['threeYear']
    threeyear.append(threeyr)
print(threeyear)

fiveYear = []
for i in response['data']['smallcases']:
    fivYear = i['stats']['returns']['fiveYear']
    fiveYear.append(fivYear)
print(fiveYear)

maxreturn = []
for i in response['data']['smallcases']:
    maxx = i['stats']['returns']['sinceInception']
    maxreturn.append(maxx)
print(maxreturn)

divreturn = []
for i in response['data']['smallcases']:
    diuv = i['stats']['divReturns']
    divreturn.append(diuv)
print(divreturn)

minamounttoinvest = []
for i in response['data']['smallcases']:
    minmi = i['stats']['minInvestAmount']
    minamounttoinvest.append(minmi)
print(minamounttoinvest)


marketCapCategory = []
for i in response['data']['smallcases']:
    marketCapCateg = i['stats']['ratios']['marketCapCategory']
    marketCapCategory.append(marketCapCateg)
print(marketCapCategory)


riskLabel = []
for i in response['data']['smallcases']:
    riskLab = i['stats']['ratios']['riskLabel']
    riskLabel.append(riskLab)
print(riskLabel)

cagr = []
for i in response['data']['smallcases']:
    cag = i['stats']['ratios']['cagr']
    cagr.append(cag)
print(cagr)

cagr1 = []
for i in response['data']['smallcases']:
    cag1 = i['stats']['ratios']['cagr1y']
    cagr1.append(cag1)
print(cagr1)


cagr3 = []
for i in response['data']['smallcases']:
    cag3 = i['stats']['ratios']['cagr3y']
    cagr3.append(cag3)
print(cagr3)


cagr5 = []
for i in response['data']['smallcases']:
    cag5 = i['stats']['ratios']['cagr5y']
    cagr5.append(cag5)
print(cagr5)



# %%
df = pd.DataFrame(data=Name, columns=['Name'])
df['publisherName'] = publisherName
df['created date'] = created
df['rebalance schedule'] = rebalanceschedule
df['half yearly'] = halfyearly
df['Monthly returns'] = Monthlyreturns
df['one year'] = fullyearly
df['five year'] = fiveYear
df['three year'] = threeyear
df['max return'] = maxreturn
df['devidance return'] = divreturn
df['risk label'] = riskLabel
df ['cagr'] = cagr
df ['cagr1yr'] = cagr1
df ['cagr3yr'] = cagr3
df ['cagr5yr'] = cagr5
df ['market cap category'] = marketCapCategory
df['min amount to invest'] = minamounttoinvest
# %%
df
# %%
