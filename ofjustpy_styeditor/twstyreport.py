"""Create/edit/save styreport from webpage"""
from addict import Dict
from tailwind_tags import styClause
from dpath.util import get as dget, set as dset,  new as dnew, delete as ddelete

from aenum import Enum
def get_attribute_value(twsty_tags, elabel="mr"):
    for _ in filter(lambda _ : not isinstance(_, Enum), twsty_tags):
        if _.elabel == elabel:
            return int(_.arg2)
    return 0


def get_margin(twsty_tags):
    return get_attribute_value(twsty_tags, "mr")

def get_height(twsty_tags):
    return get_attribute_value(twsty_tags, "H")

def get_padding(twsty_tags):
    return get_attribute_value(twsty_tags, "pd")

def recurse(root):
    child_spacings = [recurse(child_comp) for child_comp in root.components]
    all_margins = [_cs.mr for _cs in child_spacings]
    all_effective_heights = [_cs.effective_height  for _cs in child_spacings]
    print ("margin and heights ", all_margins, " ", all_effective_heights, " ", root.stub.key)
    if len(set(all_margins)) > 1:
        print ('uneven margin at sibling=', all_margins, " ", root.stub.key)

    if len(set(all_effective_heights)) > 1:
        print ('uneven effective_heights for  sibling=', all_effective_heights, " ", root.stub.key)
                

    root_margin = get_margin(root.twsty_tags)
    root_effective_height = get_height(root.twsty_tags) + get_padding(root.twsty_tags)
    max_mr = 0
    if all_margins:
        max_mr = max(all_margins)
    max_effective_height = 0
    if all_effective_heights:
        max_effective_height = max(all_effective_heights)
        
    return  Dict({'mr': max_mr + root_margin, 'effective_height': max_effective_height + root_effective_height})
res = recurse(wp)
