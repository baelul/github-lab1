import json

def search_json(json_data, search_string):
    results = []
    # Place your search code here
    # you will have to loop through the json_data file you created earlier
    keys = json_data[0].keys()

    if search_string in keys:
        # results is list of values
        for item in json_data:
            results.append(item[search_string])
    else:
        # results is list of items
        for i in range(len(json_data)):
            vals = json_data[i].values()
            if search_string in vals:
                results.append(json_data[i])

    # finally you can store the match in the result list and return it
    print("You have " + str(len(results)) + " search results:")
    return results