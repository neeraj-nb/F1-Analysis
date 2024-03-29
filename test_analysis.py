import fastf1
import fastf1.plotting

from analysis import Driver
import analysis

fastf1.plotting.setup_mpl()

session = fastf1.get_session(2024, 'Australian Grand Prix', 'R')
session.load()

drivers = [Driver('SAI','red'), Driver('NOR','orange')]
laps = [10,10]

analysis.lap_speed_comparision(session, drivers, laps)