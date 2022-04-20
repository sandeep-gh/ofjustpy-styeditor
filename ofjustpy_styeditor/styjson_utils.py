""" manipulation of webpage style represented as json
"""
from tailwind_tags import tstr

import json
import logging
import os
import sys
import jsbeautifier
from dpath.util import get as dget, set as dset,  new as dnew
from addict import Dict, walker as dict_walker
from jsonpath_ng import parse
from tailwind_tags import styClause

opts = jsbeautifier.default_options()
logger = logging.getLogger(__name__)


def matched_kpaths(jsonPathExpr: str, jsonDict: Dict):
    """find paths in jsonDict that match jsonPathExpr. 
    jsonDict:json expressed as nested dictionary
    jsonPathExpr: json path query
    Returns kpath of type /a/b/c.
    """
    jsonpath_expr = parse(jsonPathExpr)

    num_matches = 0
    for _ in jsonpath_expr.find(jsonDict):
        #logger.debug(f"mpath: {_.full_path}")
        num_matches += 1
    if num_matches == 0:
        print(f"json path expression {jsonPathExpr} has no matches")
        logger.info(
            f"json path expression {jsonPathExpr} has no matches")
        # logger.debug(session_dict['styj'])
    return map(lambda jmatch:
               "/" +
               str(jmatch.full_path).replace(".", "/"),
               jsonpath_expr.find(jsonDict)
               )


# def save_sty():
#     logger.debug("saving sty in styreport.json")
#     with open("styreport.json", "w") as fh:
#         res = jsbeautifier.beautify(json.dumps(session_dict['styj']), opts)
#         fh.write(res)


# def set_sty(stypath: str, styreport: Dict):
#     """
#     update the sty/classes of hc defined
#     styreport/stypath.
#     """
#     spath = dget(
#         styreport,   stypath + "/spath")
#     styj = dget(styreport,   stypath)
#     #logger.debug(f"spath {spath}")
#     sref = dget(stubStore, spath)
#     dbref = sref.target

#     styUpdated = tstr(*styClause.to_clause(styj))
#     #logger.debug(f"styUp {styUpdated}")

#     if 'wp_index._sty' in stypath:  # TODO: this isn't correct predicate to locate webapge
#         logger.debug(
#             f"SKIPPING : {stypath} for now : FIX ME {styUpdated}")
#     else:
#         logger.debug(
#             f"updatding {spath}-/-{dbref.key} from {dbref.classes} to {styUpdated}")
#         dbref.classes = styUpdated


# def set_sty_styreport(styreport: Dict):
#     """
#     apply sty to every HC of the main wp
#     """
#     for k, v in dict_walker(styreport, guards=["_sty"]):
#         set_sty(k, styreport)
#         pass
#     pass


# def apply_sty_from_file():
#     with open("styreport.json", "r") as fh:
#         styreport = Dict(json.load(fh.read()))
#         set_sty_styreport(styreport)
#     pass


# def build_json_from_kpaths(kpaths):
#     resJson = Dict()

#     def process_kpath(kpath):
#         print(f"now processing {kpath}")
#         try:
#             dnew(resJson, kpath, True)
#         except Exception as e:
#             print("got exception is build_json", e)
#             pass
#     res = [_ for _ in map(process_kpath, kpaths)]
#     print(resJson)
#     return resJson
