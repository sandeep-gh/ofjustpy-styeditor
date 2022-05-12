
import ofjustpy as oj
import ofjustpy_react as ojr
from addict import Dict
from ofjustpy_extn import HierarchyNavigator_
from aenum import Enum
from tailwind_tags import style_values as sv
def build_components(session_manager, component_hierarchy, callback_component_hierarchy):
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
        
        def on_click(dbref, msg):
            pass
        HierarchyNavigator_(
            "hinav", component_hierarchy, callback_component_hierarchy).event_handle(oj.click, on_click)
        #oj.Subsection_("Panel", "Edit Single Component", _ictx.btn)


    with session_manager.uictx("twreference") as _twreferencectx:
        _ictx = _twreferencectx
        @ojr.CfgLoopRunner
        def handle_twSty_select(dbref, msg):
            ecls = sv.styValueDict[dbref.stub.key]  # enum class
            selected_attr = getattr(ecls, dbref.value)
            print("handle_twSty_select: ", ecls, " ", selected_attr)
            #return as if the 
            return _ictx.styValuesPanel.target.stub.spath, selected_attr
            # logger.debug(f"{selected_attr}")
            #styconfigComponents.inputPathExprSty.target.setValue(dbref.key)
            #styconfigComponents.inputValue.target.setValue(dbref.getValue())
            #return dbref.key, dbref.getValue()

        def hc_enum_selector(attrClass: Enum):
            """Build selector htmlcomponent for enum class
            attrClass: enum type that describes a tailwind utility -- e.g. fw, fsz, etc.
            """
            #pcp = [shdw.md, bg/gray/1]
            name = attrClass.__name__
            return oj.WithBanner_(f"{name}Banner", name, oj.Select_(name, [oj.Option_(_.name, text = _.value , value=_.name) for _ in attrClass]).event_handle(oj.change, handle_twSty_select))
        #do not mix uictx and lambda
        cgens = [_ for _ in map(lambda kv: hc_enum_selector(kv[1]), sv.styValueDict.items())]
        oj.Subsection_("styValuesPanel", "Tailwing Style Directives",
                       oj.StackG_("content", num_cols=3,  cgens=cgens)
                       )
