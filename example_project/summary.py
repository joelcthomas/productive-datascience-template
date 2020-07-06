

def summary(data):
    return data.describe().toPandas().set_index("summary").transpose()