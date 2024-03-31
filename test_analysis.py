import fastf1
import fastf1.plotting
from matplotlib import pyplot as plt
from analysis import Driver
import analysis

fastf1.plotting.setup_mpl()

session = fastf1.get_session(2024, 'Australian Grand Prix', 'R')
session.load()

drivers = [Driver('SAI','red'), Driver('NOR','orange')]
laps = [10,10]

analysis.lap_speed_comparision(session, drivers, laps)

analysis.lap_delta(session, drivers, laps)

analysis.lap_throttle(session, drivers, laps)

fig, ax = plt.subplots(1,2)
print(ax[0])
analysis.lap_speed_comparision(session, drivers, laps, ax=ax[0])
analysis.lap_speed_comparision_time(session, drivers, laps, ax=ax[1])

plt.show()