
class Melon(object):

    def __init__(self,
                 melon_id,
                 melon_type,
                 common_name,
                 price,
                 image_url,
                 color,
                 seedless,
                 ):
        self.melon_id = melon_id
        self.melon_type = melon_type
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless
    def price_str(self):
        return f"${self.price:.2f}"
    def __repr__(self):
        return f"<Melon: {self.melon_id}, {self.common_name}, {self.price_str()}>"


def read_melon_types_from_file(filepath):
    melon_types = {}

    with open(filepath) as file:
        for line in file:
            (melon_id,
             melon_type,
             common_name,
             price,
             img_url,
             color,
             seedless) = line.strip().split("|")

            price = float(price)

            seedless = (seedless == "1")

            melon_types[melon_id] = Melon(melon_id,
                                          melon_type,
                                          common_name,
                                          price,
                                          img_url,
                                          color,
                                          seedless)

    return melon_types


def get_all():
    return list(melon_types.values())


def get_by_id(melon_id):

    return melon_types[melon_id]


# Dictionary to hold types of melons.
#
# Format is {id: Melon object, ... }

melon_types = read_melon_types_from_file("melons.txt")
