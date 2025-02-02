from PyQuantum.Tools.Assert import *

Hz = 1         # 1 Гц
KHz = 10 ** 3  # 1 KГц
MHz = 10 ** 6  # 1 МГц
GHz = 10 ** 9  # 1 ГГц

ms = 1e-3  # 1 мс
mks = 1e-6  # 1 мкс
ns = 1e-9  # 1 мкс


# ---------------------------------------------------------------------------------------------------------------------
def time_unit(time):
    # Assert(not(time != 0 and time < 1e-9), 'time < 1 ns')

    if time >= 1:
        unit = 's'
    elif time >= 1e-3:
        unit = 'ms'
    elif time >= 1e-6:
        unit = 'mks'
    elif time >= 1e-9:
        unit = 'ns'
    else:
        unit = 'fs'


    return unit
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
def time_unit_full(time, precision=3):
    # Assert(not(time != 0 and time < 1e-9), 'time < 1 ns')
    # Assert(time >= 1e-9, 'time < 1 ns')

    if time >= 1:
        return str(round(time, precision)) + ' s'
    elif time >= 1e-3:
        return str(round(time/1e-3, precision)) + ' ms'
    elif time >= 1e-6:
        return str(round(time/1e-6, precision)) + ' mks'
    elif time >= 1e-9:
        return str(round(time/1e-9, precision)) + ' ns'
    else:
        return str(round(time/1e-12, precision)) + ' ns'

    return time
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
def frequency_unit(frequency):
    Assert(frequency >= 1, 'frequency < 1 Hz')

    if frequency >= 1e9:
        unit = 'GHz'
    elif frequency >= 1e6:
        unit = 'MHz'
    elif frequency >= 1e3:
        unit = 'KHz'
    else:
        unit = 'Hz'

    return unit
# ---------------------------------------------------------------------------------------------------------------------
