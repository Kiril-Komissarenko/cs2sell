from dotenv import load_dotenv;
import requests;
import os;
import json;
import random;

load_dotenv();
CS_MARKET_KEY = os.getenv("CS_MARKET_KEY");

def get_random_proxy(file = "data/proxy.txt"):
    file = open(file, "r")
    aline = next(file);
    for num, aline in enumerate(file, 2):
        if random.randrange(num):
            continue;
        line = aline;
    return line;

def get_acess_token(directory):
    with open(directory, "r") as file:
        dictonary = json.load(file); # mafile
    
    return dictonary['Session']['AccessToken'] #access token

def get_username(directory):
    with open(directory, "r") as file:
        dictonary = json.load(file); # mafile
    
    return dictonary['account_name'];

def files_in_folder(directory = "data/maFiles"):
    return [files for files in os.listdir(directory) if os.path.isfile(os.path.join(directory, files))];

def items_not_listed():
    url = "https://market.csgo.com/api/v2/my-inventory"
    params = {
        "key": CS_MARKET_KEY,
        "lang": "en"
    }
    response = requests.get(url, params = params);
    data  =response.json()
    print(data);

def generate_API_Keys():
    url = "https://market.csgo.com/api/v2/my-inventory"
    base = "data/maFiles/"

    #file is fully rewroten each itteration, adding/recreating all api keys. NodeProxy used for proxy.
    with open("data/csmarket_api_keys.txt", "w") as file:
        file.write("{");

        for account in files_in_folder():
            path = base + account;

            params = {
                "access_token": get_acess_token(path),
                "proxy": get_random_proxy(),
                "currency": "USD"
            }

            response = requests.post(url, params = params);
            data = response.json();

            if data["sucess"] == True:
                file.write(f"{get_username(path)}:{data["apikey"]},");
            else:
                raise ValueError(f"Error {response.status_code}: {response.reason}");
        file.write("}");


#print(get_username("data/maFiles/aaronflux514.maFile"));
#print(files_in_folder(r"E:\cs2 farm\renamed_maFiles"));
#print(get_random_proxy());
