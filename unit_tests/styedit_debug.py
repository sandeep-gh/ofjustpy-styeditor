import ofjustpy as oj
from tailwind_tags import *
import justpy as jp
from tailwind_tags import *

import ofjustpy_styeditor as ojs
import jsbeautifier
import json


@ojs.enableStyEdit
def launcher(request):
    session_id = "asession"
    session_manager = oj.get_session_manager(session_id)

    def on_btn_click(dbref, msg):
        print("circle clicked", dbref.text, msg.value)

        pass

    def on_input_change(dbref, msg):
        print("on input called", msg.value)
        pass

    with oj.sessionctx(session_manager):
        mybtn = oj.Button_("mybtn", value="myval",
                           text="Click me ", pcp=[bg/blue/100])

        wp = oj.WebPage_("wp", body_styl=[
                         bg/pink/"100/10"], cgens=[mybtn])()
        styreport = ojs.get_styReport(wp)
    # mystackw(wp)
    # mystackg(wp)
    # oj.Subsection_("subsection", "Grid display", mystackg)(wp)
    # oj.Subsubsection_("subsubsection", "Wrap display", mystackw)(wp)
    wp.session_manager = session_manager
    return wp


# wp = jp.WebPage()
# circle = circleStub(wp)
# print(circle.twsty_tags)
#wp = launcher(None)
app = jp.app
jp.justpy(launcher, debug=True, start_server=False)

# ===================== test the styedit workflow ====================
# request = Dict()
# request.session_id = "ah"
# wp = launcher(request)
# msg = Dict()
# msg.page = wp
# ojs.session_manager.stubStore.twstyediturl.target.on_click(msg)
# wp_ed = ojs.wp_twstyeditor.wp_twstyeditor(request)

# # print(ojs.wp_twstyeditor.target_wp)

# ed_stubStore = wp_ed.session_manager.stubStore
# ed_stubStore.bulkedit.componentSelectorPathExpr.target.value = "$."
# ed_stubStore.bulkedit.stySelectorPathExpr.target.value = "FontWeight"
# ed_stubStore.bulkedit.styTargetValue.target.value = "bold"
# msg.page = wp_ed
# ed_stubStore.bulkedit.updateStyBtn.target.on_click(msg)

# styreport = ojs.get_styReport(wp)
# opts = jsbeautifier.default_options()
# res = jsbeautifier.beautify(json.dumps(styreport), opts)
# with open("styreport.json", "w") as fh:
#     fh.write(res)
# print(styreport)
# ================================ end ===============================
# ===================== test the styedit workflow ====================
# request = Dict()
# request.session_id = "ah"
# wp = launcher(request)
# msg = Dict()
# msg.page = wp
# ojs.session_manager.stubStore.twstyediturl.target.on_click(msg)
# wp_ed = ojs.wp_twstyeditor.wp_twstyeditor(request)
# # print(wp_ed)
# # print(ojs.wp_twstyeditor.target_wp)
# # wp_ed.edbtn.on_click(msg)
# ed_stubStore = wp_ed.session_manager.stubStore
# ed_stubStore.bulkedit.componentSelectorPathExpr.target.value = "$."
# ed_stubStore.bulkedit.stySelectorPathExpr.target.value = "bg"
# ed_stubStore.bulkedit.styTargetValue.target.value = "20"
# msg.page = wp_ed
# ed_stubStore.bulkedit.updateStyBtn.target.on_click(msg)

# styreport = ojs.get_styReport(wp)
# opts = jsbeautifier.default_options()
# res = jsbeautifier.beautify(json.dumps(styreport), opts)
# with open("styreport.json", "w") as fh:
#     fh.write(res)
# print(styreport)
# ================================ end ===============================
