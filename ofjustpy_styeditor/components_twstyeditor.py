
import ofjustpy as oj


def build_components(session_manager):
    stubStore = session_manager.stubStore
    oj.Button_("btn", text="btn", value="btn")
    oj.Subsection_("Editor", "Editor", stubStore.btn)
