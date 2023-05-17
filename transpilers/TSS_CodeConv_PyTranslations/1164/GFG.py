import math

class GFG:
    @staticmethod
    def distance(lat1, lat2, lon1, lon2):
        lon1 = Math.toRadians(lon1)
        lon2 = Math.toRadians(lon2)
        lat1 = Math.toRadians(lat1)
        lat2 = Math.toRadians(lat2)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        r = 6371
        return (c * r)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        lat1 = 53.32055555555556
        lat2 = 53.31861111111111
        lon1 = - 1.7297222222222221
        lon2 = - 1.6997222222222223
        print(str(GFG.distance(lat1, lat2, lon1, lon2)) + " K.M")
