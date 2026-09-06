import json
import pickle
import numpy as np
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    val = np.zeros(len(__data_columns))
    val[0] = sqft
    val[1] = bath
    val[2] = bhk
    if loc_index >= 0:
        val[loc_index] = 1
    return round(__model.predict([val])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts..start")
    global __data_columns
    global __locations

    with open("./artifacts/vadodara columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    global __model
    with open("./artifacts/vadodara_home_prices_model (1).pickle",'rb') as f:
        __model = pickle.load(f)
    print("Loading saved artifacts..done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('vasna road',1000,2,1))
    print(get_estimated_price('vasna road',2000,4,5))
    print(get_estimated_price('sama savli',1000,1,2))
    print(get_estimated_price('vasna road',4000,4,4))