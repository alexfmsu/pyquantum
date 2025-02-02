# ---------------------------------------------------------------------------------------------------------------------
# Common
from PyQuantum.Tools.Assert import *
from PyQuantum.Tools.Print import *
from PyQuantum.Tools.Hz import *
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
class Cavity:

    # ---------------------------------------------------------------------------------------------
    def __init__(self, wc, wa, g, n_atoms, n_levels=2):
        Assert(isinstance(wc, (int, float)),
               "wc is not numeric", FILE(), LINE())
        Assert(isinstance(wa, (int, float)),
               "wa is not numeric", FILE(), LINE())
        Assert(isinstance(g, (int, float)), "g is not numeric", FILE(), LINE())
        Assert(isinstance(n_atoms, int),
               "n_atoms is not integer", FILE(), LINE())

        Assert(wc > 0, "wc <= 0", FILE(), LINE())
        Assert(wa > 0, "wa <= 0", FILE(), LINE())
        Assert(g > 0, "g <= 0", FILE(), LINE())
        Assert(n_atoms > 0, "n <= 0", FILE(), LINE())

        self.wc = wc
        self.wa = wa

        self.g = g

        self.n_atoms = n_atoms
        self.n_levels = n_levels

    # ---------------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------------

    def n_atoms_info(self):
        print(" n_atoms: ", color="yellow")

        print(self.n_atoms)

        print()
    # ---------------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------------
    def wc_info(self):
        print("wc: ", color="yellow")

        print(to_Hz(self.wc))

        print()
    # ---------------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------------
    def wa_info(self):
        print("wa: ", color="yellow")

        print(to_Hz(self.wa))

        print()
    # ---------------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------------
    def g_info(self):
        print(" g: ", color="yellow")

        print(to_Hz(self.g))

        print()
    # ---------------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------------
    def info(self, title="Cavity:"):
        print(title, color="green")

        print()

        self.wc_info()
        self.wa_info()
        self.g_info()
        self.n_atoms_info()
    # ---------------------------------------------------------------------------------------------

# =====================================================================================================================

# # from PyQuantum.TC.Cavity import *

# # -------------------------------------------------------------------------------------------------
# # Common
# from PyQuantum.Tools.Assert import *
# from PyQuantum.Tools.Print import *
# from PyQuantum.Common.STR import *
# # -------------------------------------------------------------------------------------------------


# # -------------------------------------------------------------------------------------------------
# class Cavity:

#     # ---------------------------------------------------------------------------------------------
#     def __init__(self, n, wc, wa, g):
#         Assert(isinstance(n, int), "n is not integer", FILE(), LINE())
#         Assert(isinstance(wc, (int, float)),
#                "wc is not numeric", FILE(), LINE())
#         Assert(isinstance(wa, (int, float)),
#                "wa is not numeric", FILE(), LINE())
#         Assert(isinstance(g, (int, float)), "g is not numeric", FILE(), LINE())

#         Assert(n > 0, "n <= 0", FILE(), LINE())
#         Assert(wc > 0, "wc <= 0", FILE(), LINE())
#         Assert(wa > 0, "wa <= 0", FILE(), LINE())
#         Assert(g > 0, "g <= 0", FILE(), LINE())

#         self.n = n

#         self.wc = wc
#         self.wa = wa

#         self.g = g
#     # ---------------------------------------------------------------------------------------------

#     # ---------------------------------------------------------------------------------------------
#     def print_n(self):
#         print(" n: ", color="yellow")

#         print(self.n)

#         print()
#     # ---------------------------------------------------------------------------------------------

#     # ---------------------------------------------------------------------------------------------
#     def print_wc(self):
#         print("wc: ", color="yellow")

#         print(wc_str(self.wc))

#         print()
#     # ---------------------------------------------------------------------------------------------

#     # ---------------------------------------------------------------------------------------------
#     def print_wa(self):
#         print("wa: ", color="yellow")

#         print(wa_str(self.wa))

#         print()
#     # ---------------------------------------------------------------------------------------------

#     # ---------------------------------------------------------------------------------------------
#     def print_g(self):
#         print(" g: ", color="yellow")

#         print(g_str(self.g))

#         print()
#     # ---------------------------------------------------------------------------------------------

#     # ---------------------------------------------------------------------------------------------
#     def print(self):
#         print("Cavity:", color="green")

#         print()
#         print()

#         self.print_n()
#         self.print_wc()
#         self.print_wa()
#         self.print_g()
#     # ---------------------------------------------------------------------------------------------

# # -------------------------------------------------------------------------------------------------
