list = {
    "1": "T",
    "2": "T",
    "3": "T",
    "4": "T",
    "5": "T",
    "6": "T",
    "7": "T",
    "8": "T",
    "9": "T",
    "10": "T",
}
list["2"] = "F"
list["7"] = "F"
del list["3"]
list["4"] = 0
print(list)

