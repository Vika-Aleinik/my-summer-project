def load_config(filename):
    config = {}
    file = open(filename, "r")
    for line in file:
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        config[key] = value

    file.close()
    return config
