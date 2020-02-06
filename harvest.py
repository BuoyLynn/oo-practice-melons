############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""

        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 'Muskmelon', 1998, 'green', True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 'Casaba', 2003, 'orange', False, False)
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', 'Crenshaw', 1996, 'green', False, False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow', False, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    # import pdb; pdb.set_trace()

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        # print(melon)
        index = 0
        print(f"{melon.name} pairs with\n- {melon.pairings[0]}")
        if len(melon.pairings) >= 2:
            print(f"- {melon.pairings[index+1]}")
            index += 0


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dictionary = {}
    code_key_list = []

    for melon in melon_types:
        attribute_value_list = []

        code_key_list.append(melon.code)

        attribute_value_list.append(melon.name)
        attribute_value_list.append(melon.first_harvest)
        attribute_value_list.append(melon.pairings)
        attribute_value_list.append(melon.is_seedless)
        attribute_value_list.append(melon.is_bestseller)

        for code in code_key_list:
            melon_dictionary.setdefault(code, attribute_value_list)

    return melon_dictionary

############
# Part 2   #
############


class Melon(MelonType):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, shape_rate, color_rate, harvested_from, harvested_by):
        """Initialize a melon."""
        # inherits self.code from parent class MelonType
        self.shape_rate = shape_rate
        self.color_rate = color_rate
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    def is_sellable(melon):
        """Checks whether a melon has rating higher than 5 and isn't from Field 3."""

        return (melon.shape_rate and melon.color_rate > 5) and (melon.harvested_from != 'Field 3')


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons = []

    # loop goes here

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:

        if melon.is_sellable:
            print(f"Harvested by {melon.harvested_by} from {melon.harvested_from} (CAN BE SOLD)")
        else:
            print(f"Harvested by {melon.harvested_by} from {melon.harvested_from} (NOT SELLABLE)")
