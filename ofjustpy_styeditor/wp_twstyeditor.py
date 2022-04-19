import justpy as jp
import ofjustpy as oj
from addict import Dict
from .twstyreport import get_styReport
from .components_twstyeditor import build_components

target_wp = None


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
        oj.Container_("tlc", cgens=[stubStore.Editor])
        wp = oj.WebPage_("sty_wp", cgens=[stubStore.tlc])()

    # print(stubStore)
    return wp


# request = Dict()
# request.session_id = "asession"
# wp = wp_twstyeditor(request)
