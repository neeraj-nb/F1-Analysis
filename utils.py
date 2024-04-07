import numpy as np

def fuel_corrected_laptime(laptime, tLaps):
    cons_per_lap = 110/tLaps    #assuming empty on finish
    gain_per_lap = cons_per_lap * 30  # assuming 0.03 gain per kg of fuel lost
    gains = [int(gain_per_lap * lap) for lap in range(len(laptime))]
    # correction = np.array([np.timedelta64(gain,'ms') for gain in gains], dtype='timedelta64[ms]')
    correction = np.array(gains, dtype='timedelta64[ms]')
    corrected_laptime = np.add(laptime,correction)
    return corrected_laptime
