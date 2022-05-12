import ofjustpy_react as ojr

#ui-path, appstate-path, value transformation
ui_app_trmap = [("/twreference/styValuesPanel", ("/append_twSty", None))]
app_ui_trmap = [
    ("/selected_dbref", ojr.AttrMeta(None, [ojr.Ctx("/append_twSty", ojr.isstr, ojr.UIOps.APPEND_CLASSES)])),
        ("/twreference/styValuesPanel", ojr.AttrMeta(None, []))
                ]

#cfg_CM = ["/target_wp/", AttrMeta(None, True, [], [Ctx("/append_twSty", isStr, custom_action)])
