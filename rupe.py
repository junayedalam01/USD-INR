import requests 


url ="https://v6.exchangerate-api.com/v6/3e92091348028ebfcfb48fdc/latest/USD"
usd =input("Enter Doler $ : ")

data =requests.get(url)
if data.status_code ==200:
    re= data.json()
    rup= re["conversion_rates"]

    value = rup['INR']
    ans = float(float(usd)*value)
    last =re['time_last_update_utc']
    next =re['time_next_update_utc']
    print(f"last data updata: {last} ")
    print(f"Next updata is: {next}")
    print(f"Rupe value is: {ans}")