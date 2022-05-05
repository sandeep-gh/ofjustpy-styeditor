import ofjustpy as oj
from .twstyreport import get_styReport
#from .wp_twstyeditor import target_wp
from . import wp_twstyeditor
import functools

# yes This is global; for edit for only one wp is possible

session_manager = None


def enableStyEdit(func):
    """
    register the stub in _hcs/stubStore
    """
    @functools.wraps(func)
    def stubGen_wrapper(*args, **kwargs):
        from . import wp_twstyeditor
        global target_wp
        global session_manager
        wp = func(*args, **kwargs)
        wp_twstyeditor.target_wp = wp
        # put href url to twstyconfig on target_wp under its own session manager
        session_manager = oj.get_session_manager("enableStyEdit")
        with oj.sessionctx(session_manager):
            oj.A_("twstyediturl", href="twstyconfig",
                  text="twstyconfig", target="_blank")(wp)


        #scracthpad for hierarchy navigator

        
        # print(styreport)
        # styedit this page
        return wp

    return stubGen_wrapper
