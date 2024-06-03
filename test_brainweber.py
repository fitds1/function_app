import requests
 
url = "https://cloud.jdpower.ai/data-api/UAT/valuationservices/valuation/accessoriesByVehicleId?period=0&ucgvehicleid=201736369&region=3"
 
payload = {}
headers = {
  'api-key': 'c274a27d-5afc-4529-9d7c-eeb7df2e4754'
}
 
response = requests.request("GET", url, headers=headers, data=payload)
 
print(response.text)
