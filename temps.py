import tmp36
import internal_temp
import utime

tmp36 = tmp36.GetTemp(2)
internal = internal_temp.GetTemp()
while True:
    print("TMP36 = %.4f C, Internal = %.4f C" % (tmp36.get_temp(), internal.get_temp()))
    utime.sleep(2)
