# =====================================================================================================================
# PyQuantum.Tools
from PyQuantum.Tools.Assert import Assert, FILE, LINE
from PyQuantum.Tools.Print import cprint
from PyQuantum.Tools.Hz import to_Hz
# =====================================================================================================================


# =====================================================================================================================
class BaseCavity:
    # -----------------------------------------------------------------------------------------------------------------
    def __init__(self, wc):
        Assert(isinstance(wc, (int, float)),
               "wc is not numeric", FILE(), LINE())
        Assert(wc > 0, "wc <= 0", FILE(), LINE())

        self.wc = wc
    # -----------------------------------------------------------------------------------------------------------------

    # -----------------------------------------------------------------------------------------------------------------
    def wc_info(self):
        cprint("wc: ", "yellow")

        print(to_Hz(self.wc))

        print()
    # -----------------------------------------------------------------------------------------------------------------

    # -----------------------------------------------------------------------------------------------------------------
    def info(self, title="Cavity:"):
        cprint(title, "green")

        print()

        self.wc_info()
    # -----------------------------------------------------------------------------------------------------------------

# =====================================================================================================================
