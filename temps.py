"""
Read internal and external temp sensor
"""

import utime
from library import internal_temp, tmp36

tmp36 = tmp36.GetTemp(2)
internal = internal_temp.GetTemp()
while True:
    print("TMP36 = %s, Internal = %s" % (tmp36.get_temp_str(), internal.get_temp_str()))
    utime.sleep(2)
