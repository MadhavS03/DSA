### A node is value and the pointer ###
### A LL is a dictionary ###

head =  {
    "value": 10,
    "next": {
        "value": 23,
        "next":{
            "value":4,
            "next": None
        }
    }
}

print(head["next"]["next"]["value"])
print(head["next"]["value"])

### A set of nested dictionaries ###