import fastf1
import fastf1.plotting
from matplotlib import pyplot as plt
from analysis import Driver, Team
import analysis

fastf1.plotting.setup_mpl()

session = fastf1.get_session(2024, 'Australian Grand Prix', 'R')
session.load()

drivers = [Driver('SAI','red',Team('Ferrari','SF')), Driver('NOR','orange',Team('McLaren','MC'))]

laps = [10,10]

fig, ax = plt.subplots(5,1)
plt.suptitle("Australian Grand Prix")
print(ax[0])
analysis.lap_speed_comparision(session, drivers, laps, ax=ax[0])
analysis.lap_delta(session, drivers, laps, ax=ax[1])
analysis.lap_throttle(session, drivers, laps, ax=ax[2])
analysis.lap_brake(session, drivers, laps, ax=ax[3])
analysis.lap_gear(session, drivers, laps, ax=ax[4])

fig, ax = plt.subplots()
analysis.rpm_v_speed(session, drivers, ax=ax)

analysis.vTop_v_vMean(session, [Team('Ferrari','SF',ref_driver='SAI'),Team('Mercedes','MER',ref_driver='HAM')])

plt.show()