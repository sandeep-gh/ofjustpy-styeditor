from aenum import extend_enum
import logging
import os
if os:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

import justpy as jp
import ofjustpy as oj
from addict import Dict
from .twstyreport import get_styReport
from .components_twstyeditor import build_components
from .styjson_utils import matched_kpaths
import ofjustpy_react as ojr
from .dpathutils import dget, dset
from tailwind_tags import tstr, styClause

target_wp = None

# register with looprunner; update_sty should go here
extend_enum(ojr.ReactTag_UI, 'update_sty', 'update_sty')


def make_wp_react(wp):
    def react_ui(tag, arg: dict[str, str]):
        logger.debug(f"react_ui: {tag}, {arg}")
        styreport = get_styReport(target_wp)
        stubStore = target_wp.session_manager.stubStore
        match tag:
            case ojr.ReactTag_UI.update_sty:
                # styPathExprJ = arg.pathExprHead + "._sty"
                def update_sty(kpath):
                    """
                    update style/classes of component based upon updated styj
                    """
                    # path from root to sty
                    # TODO: this needs to be more generic
                    # logger.debug(f"update a match {kpath}")
                    print(dget(styreport, kpath + "/_val"))
                    dset(styreport, kpath +
                         "/_val", arg.targetValue)
                    print(dget(styreport, kpath + "/_val"))
                    kpath_tokens = kpath.split("/")
                    for i in range(len(kpath_tokens)-1, 0, -1):
                        print(i)
                        if kpath_tokens[i] == "_sty":
                            break
                    print(i, kpath_tokens[0:i+1])
                    stypath = "/".join(kpath_tokens[0:i+1])
                    print("stypath = ", stypath)
                    spath = dget(
                        styreport,   stypath + "/spath")
                    # component style in json format
                    styj = dget(styreport,   stypath)
                    print("spath = ", spath)
                    print("styj = ", styj)
                    stub = dget(stubStore, spath)
                    dbref = stub.target
                    print(stub, " ", dbref)
                    styUpdated = tstr(*styClause.to_clause(styj))
                    # #logger.debug(f"styUp {styUpdated}")
                    print(spath, " ", dbref.stub.key)
                    print("classes = ", dbref.classes)
                    print("styUpdated = ", styUpdated)
                    if isinstance(dbref, jp.WebPage):
                        dbref.body_classes = styUpdated
                        logger.debug(
                            f"SKIPPING : {kpath} for now : FIX ME {styUpdated}")
                    else:
                        logging.debug(
                            f"updatding {spath}-/-{kpath}/{dbref.stub.key} from {dbref.classes} to {styUpdated}")
                        #dbref.classes = styUpdated
                        dbref.set_class("bg-green-400")
                        print(dbref.classes)

                    # ====================== end =====================
                    pass
                # collections.deque(
                #     map(update_sty, matched_kpaths(arg.pathexpr, styreport)), maxlen=0)
                for _ in matched_kpaths(arg.pathexpr, styreport):
                    update_sty(_)
                # refresh the webpage
                jp.run_task(target_wp.update())
                pass
            case ReactTag_UI.append_sty:
                # logger.debug("appending ")
                # styPathExprJ = arg.pathExprHead + "._sty"
                # styreport = session_dict['styj']
                # matched_kpaths(styPathExprJ, styreport)

                # def append_sty(kpath):
                #     # append path
                #     logger.debug(kpath)
                #     new_kpath = kpath + "/" + \
                #         arg.pathExprTail.replace(".", "/") + "/_val"
                #     logger.debug(new_kpath)
                #     dnew(styreport, new_kpath, arg.appendValue)
                #     set_sty(kpath, styreport)
                #     pass

                # collections.deque(
                #     map(append_sty, matched_kpaths(styPathExprJ, styreport)), maxlen=0)
                # # panel_jsonEditor_.jsonEditor.replace_content(
                # #    styreport)
                # jp.run_task(session_dict['main_wp'].update())
                pass

            case ReactTag_UI.apply_sty:
                # styreport = session_dict['styj']
                # set_sty_styreport(styreport)
                # jp.run_task(session_dict['main_wp'].update())
                pass
    wp.react_ui = react_ui


@jp.SetRoute("/twstyconfig")
def wp_twstyeditor(request):
    print("invoked")
    session_id = "asession"
    session_manager = oj.get_session_manager(session_id)
    stubStore = session_manager.stubStore
    styreport = get_styReport(target_wp)
    print(f"sty edit {target_wp.stub.key}")
    with oj.sessionctx(session_manager):
        build_components(session_manager)
        oj.Container_(
            "tlc", cgens=[stubStore.bulkedit.Panel, stubStore.componentedit.Panel])
        wp = oj.WebPage_("sty_wp", cgens=[stubStore.tlc])()
    wp.session_manager = session_manager
    make_wp_react(wp)
    # print(stubStore)
    return wp


# request = Dict()
# request.session_id = "asession"
# wp = wp_twstyeditor(request)
