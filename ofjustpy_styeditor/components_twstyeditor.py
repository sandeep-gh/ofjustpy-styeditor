
import ofjustpy as oj
import ofjustpy_react as ojr
from addict import Dict


def build_components(session_manager):
    stubStore = session_manager.stubStore
    with session_manager.uictx("bulkedit") as _bulkeditctx:
        _ictx = _bulkeditctx
        oj.InputChangeOnly_("componentSelectorPathExpr", type="text",
                            text="Component Selector Json Path", placeholder="wp_index..P")
        oj.InputChangeOnly_("stySelectorPathExpr", text="Sty Selector", type="text",
                            placeholder="fc._color")

        oj.InputChangeOnly_("styTargetValue", text="Sty Value", type="text",
                            placeholder="pink/100")

        oj.Button_("btn", text="btn", value="btn")

        @ojr.LoopRunner
        def handle_click_updateStyBtn(dbref, msg):
            print("handle_click_updateStyBtn:update sty based on json path expression")
            # collect the  inputs
            pathexpr = f"""{_bulkeditctx.componentSelectorPathExpr.target.value}._sty.{_bulkeditctx.stySelectorPathExpr.target.value}"""
            targetValue = _bulkeditctx.styTargetValue.target.value
            rts = ojr.TaskStack()
            rts.addTask(ojr.ReactTag_UI.update_sty,
                        Dict({'pathexpr': pathexpr,
                              'targetValue': targetValue})
                        )
            return msg.page, rts

        oj.Button_("updateStyBtn", text="Update", value="Update").event_handle(
            oj.click, handle_click_updateStyBtn)
        oj.Subsection_("Panel", "Bulk edits using Json Paths", oj.StackV_(
            "bin", cgens=[_ictx.componentSelectorPathExpr,
                          _ictx.stySelectorPathExpr,
                          _ictx.styTargetValue,
                          _ictx.updateStyBtn

                          ]))
    with session_manager.uictx("componentedit") as _componenteditctx:
        _ictx = _componenteditctx
        oj.Button_("btn", text="btn", value="btn")
        oj.Subsection_("Panel", "Bulk edits using Json Paths", _ictx.btn)
