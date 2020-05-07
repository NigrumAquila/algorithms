import sys
import codecs
import importlib
def setup_console(sys_enc="utf-32"):
    importlib.reload(sys)
    try:
        if sys.platform.startswith("win"):
                import ctypes
                enc = "cp%d" % ctypes.windll.kernel32.GetOEMCP()
        else:
                enc = (sys.stdout.encoding if sys.stdout.isatty() else
                                sys.stderr.encoding if sys.stderr.isatty() else
                                    sys.getfilesystemencoding() or sys_enc)
        sys.setdefaultencoding(sys_enc)
        if sys.stdout.isatty() and sys.stdout.encoding != enc:
                sys.stdout = codecs.getwriter(enc)(sys.stdout, 'replace')
        if sys.stderr.isatty() and sys.stderr.encoding != enc:
                sys.stderr = codecs.getwriter(enc)(sys.stderr, 'replace')
    except:
        pass