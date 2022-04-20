"""Create/edit/save styreport from webpage"""
from addict import Dict
from tailwind_tags import styClause
from dpath.util import get as dget, set as dset,  new as dnew, delete as ddelete


def annotate_styreport(de):
    rr = styClause.to_json(*de.twsty_tags)
    #rr.hctype = de.stub.hctype
    rr.spath = de.stub.spath
    x = Dict()
    x._sty = rr
    return x


def get_styReport(rootdspe):
    """
    rootdspe: basically root dbref

    """
    def walker(de, kpath="/"):
        yield f"{kpath}{de.stub.key}", de
        for ce in de.components:
            try:
                if getattr(de, 'stub'):
                    yield from walker(ce, f"{kpath}{de.stub.key}/")
            except AttributeError as e:
                print(f"skipping sty for {de} since no stub found")

    styreport = Dict(track_changes=True)
    for kpath, de in walker(rootdspe):
        rr = annotate_styreport(de)
        dnew(styreport, kpath, rr)

    return styreport
