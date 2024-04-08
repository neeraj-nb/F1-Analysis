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
plt.suptitle("Australian Grand Prix")
analysis.rpm_v_speed(session, drivers, ax=ax)

all_teams = [Team('Ferrari','SF',ref_driver='SAI'),
             Team('Mercedes','MER',ref_driver='HAM'),
             Team('McLaren','MCL',ref_driver='NOR'),
             Team('Red Bull','RBR',ref_driver='VER'),
             Team('RB','RB',ref_driver='TSU'),
             Team('Sauber','SUB',ref_driver='BOT'),
             Team('Alpine','ALP',ref_driver='GAS'),
             Team('Hass','HAS',ref_driver='MAG'),
             Team('Willams','WR',ref_driver='ALB'),
             Team('Aston Martin','ASM',ref_driver='STR'),
             ]
analysis.vTop_v_vMean(session, all_teams)
plt.suptitle("Australian Grand Prix")

analysis.race_pace(session)
plt.suptitle("Australian Grand Prix")
analysis.driver_race_pace(session)
plt.suptitle("Australian Grand Prix")

drivers = [Driver('SAI','red',Team('Ferrari','SF')), Driver('NOR','orange',Team('McLaren','MC')),Driver('RUS','blue',Team('Mercedes','MERC'))]
analysis.laptime_vs_lap(session, drivers)
analysis.fc_laptime_vs_lap(session, drivers)
analysis.laptime_vs_lap(session, Driver.all_session_drivers(session))
plt.suptitle("Australian Grand Prix")

plt.show()