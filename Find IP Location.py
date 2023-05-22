import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "country": response.get("country_name"),
        "Calling Code":response.get("country_calling_code"),
        "Postal Code" : response.get("postal"),
        "timezone": response.get("timezone")+" "+"("+response.get("utc_offset")+')',
        "Currency" : response.get("currency"),
        "Languages" : response.get("languages"),
        "ASN" : response.get("asn"),
        "Org" : response.get("org")
    }
    return location_data

print("\033[1;4;36mDetails Of IP\033[0m\n")
for i,e in get_location().items():
    print(f"\033[1;31m{i} : \033[1;32m{e}")

print("\033[0m")