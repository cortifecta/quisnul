def dictionaries_disagree(dict1, dict2):
    for key in dict1:
        if key in dict2:
            if dict1[key] != dict2[key]:
                return True
    return False
