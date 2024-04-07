import fastf1.plotting
from fastf1 import utils
from fastf1.core import Session
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from utils import fuel_corrected_laptime

class Team:
    def __init__(self, name: str, abbreviation: str, color:str=None, ref_driver=None) -> None:
        self.name = name
        self.abbrevation = abbreviation
        if color == None:
            self.color = fastf1.plotting.team_color(name)
        else:
            self.color = color
        self.ref_driver = ref_driver
    
    @staticmethod
    def all_teams():
        all_team = []
        teams = fastf1.plotting.TEAM_TRANSLATE.keys()
        for team in teams:
            name = fastf1.plotting.TEAM_TRANSLATE[team]
            abbrevation = team
            all_team.append(Team(name,abbrevation))
        return all_team


class Driver:
    def __init__(self, abbreviation: str, color: str, team: Team=None) -> None:
        self.abbrevation = abbreviation
        self.color = color
        self.team = team
    
    @staticmethod
    def all_drivers():
        all_driver = []
        drivers = fastf1.plotting.DRIVER_TRANSLATE.keys()
        for driver in drivers:
            name = fastf1.plotting.DRIVER_TRANSLATE[driver]
            abbrevation = driver
            color = fastf1.plotting.DRIVER_COLORS[name]
            all_driver.append(Driver(abbrevation,color))
        return all_driver
    
    @staticmethod
    def all_session_drivers(session: Session):
        all_driver = []
        drivers = [session.get_driver(driver)['Abbreviation'] for driver in session.drivers]
        for driver in drivers:
            name = fastf1.plotting.DRIVER_TRANSLATE[driver]
            abbrevation = driver
            color = fastf1.plotting.DRIVER_COLORS[name]
            all_driver.append(Driver(abbrevation,color))
        return all_driver

def lap_speed_comparision_time(session: Session, drivers: list[Driver], laps: list[int], **kwargs):
    """Give driver comparision data"""
    if "ax" in kwargs:
        ax = kwargs["ax"]
    else:
        fig, ax = plt.subplots()
        ax.set_title('Lap Speed')
    for driver, lap in zip(drivers, laps):
        lap_data = session.laps.pick_driver(driver.abbrevation).pick_lap(lap)
        car_data = lap_data.get_car_data()
        time = car_data['Time']
        vCar = car_data['Speed']
        ax.plot(time, vCar, label=f'{driver.abbrevation} Lap {lap}', color=driver.color)
    ax.set_xlabel('Time')
    ax.set_ylabel('Speed [Km/h]')
    ax.legend()

def lap_speed_comparision(session: Session, drivers: list[Driver], laps: list[int], **kwargs):
    if "ax" in kwargs:
        ax = kwargs["ax"]
    else:
        fig, ax = plt.subplots()
        ax.set_title('Lap Speed')
    for driver, lap in zip(drivers, laps):
        lap_data = session.laps.pick_driver(driver.abbrevation).pick_lap(lap)
        tel = lap_data.get_telemetry()
        dist = tel['Distance']
        vCar = tel['Speed']
        ax.plot(dist, vCar, label=f'{driver.abbrevation} Lap {lap}', color=driver.color)
    ax.set_xlabel('Distance [m]')
    ax.set_ylabel('Speed [Km/h]')
    ax.legend()

def lap_delta(session: Session, drivers: list[Driver], laps: list[int], **kwargs):
    if "ax" in kwargs:
        ax = kwargs["ax"]
    else:
        fig, ax = plt.subplots()
        ax.set_title('Lap delta')
    ref_lap_data = session.laps.pick_driver(drivers[0].abbrevation).pick_lap(laps[0])
    for driver, lap in zip(drivers, laps):
        lap_data = session.laps.pick_driver(driver.abbrevation).pick_lap(lap)
        delta, ref_tel, comp_tel = utils.delta_time(ref_lap_data,lap_data)
        ax.plot(ref_tel['Distance'], delta, '--', label=f'{driver.abbrevation} Lap {lap}', color=driver.color)
    ax.set_xlabel('Distance [m]')
    ax.set_ylabel('Delta [s]')
    ax.legend()

def lap_throttle(session: Session, drivers: list[Driver], laps: list[int], **kwargs):
    if "ax" in kwargs:
        ax = kwargs["ax"]
    else:
        fig, ax = plt.subplots()
        ax.set_title('Throttle')
    for driver, lap in zip(drivers, laps):
        lap_data = session.laps.pick_driver(driver.abbrevation).pick_lap(lap)
        tel = lap_data.get_telemetry()
        dist = tel['Distance']
        throttle = tel['Throttle']
        ax.plot(dist, throttle, label=f'{driver.abbrevation} Lap {lap}', color=driver.color)
    ax.set_xlabel('Distance [m]')
    ax.set_ylabel('Throttle [%]')
    ax.legend()

def lap_gear(session: Session, drivers: list[Driver], laps: list[int], **kwargs):
    if "ax" in kwargs:
        ax = kwargs["ax"]
    else:
        fig, ax = plt.subplots()
        ax.set_title('Gear')
    for driver, lap in zip(drivers, laps):
        lap_data = session.laps.pick_driver(driver.abbrevation).pick_lap(lap)
        tel = lap_data.get_telemetry()
        dist = tel['Distance']
        gear = tel['nGear']
        ax.plot(dist, gear, label=f'{driver.abbrevation} Lap {lap}', color=driver.color)
    ax.set_xlabel('Distance [m]')
    ax.set_ylabel('Gear')
    ax.legend()

def lap_brake(session: Session, drivers: list[Driver], laps: list[int], **kwargs):
    if "ax" in kwargs:
        ax = kwargs["ax"]
    else:
        fig, ax = plt.subplots()
        ax.set_title('Brake')
    for driver, lap in zip(drivers, laps):
        lap_data = session.laps.pick_driver(driver.abbrevation).pick_lap(lap)
        tel = lap_data.get_telemetry()
        dist = tel['Distance']
        brake = tel['Brake']
        ax.plot(dist, brake, label=f'{driver.abbrevation} Lap {lap}', color=driver.color)
    ax.set_xlabel('Distance [m]')
    ax.set_ylabel('Brake')
    ax.legend()

def rpm_v_speed(session: Session, drivers: list[Driver], **kwargs):
    if "ax" in kwargs:
        ax = kwargs["ax"]
    else:
        fig, ax = plt.subplots()
    for driver in drivers:
        data = session.laps.pick_driver(driver.abbrevation)
        tel = data.get_telemetry()
        vCar = tel['Speed']
        rpm = tel['RPM']
        ax.scatter(vCar, rpm, label=driver.team.abbrevation, color=driver.team.color, s=0.1)
    ax.set_xlabel('Speed [km/h]')
    ax.set_ylabel('RPM')
    ax.legend(markerscale=10)

def vTop_v_vMean(session: Session, teams: list[Team], **kwargs):
    if "ax" in kwargs:
        ax = kwargs["ax"]
    else:
        fig, ax = plt.subplots()

    for team in teams:
        data = session.laps.pick_driver(team.ref_driver).pick_fastest()
        tel = data.get_telemetry()
        ax.scatter(np.mean(tel['Speed']), np.max(tel['Speed']), label=team.abbrevation, color=team.color)
    ax.set_xlabel('Mean Speed [km/h]')
    ax.set_ylabel('Top Speed [km/h]')
    ax.legend()

def race_pace(session: Session):
    laps = session.laps.pick_quicklaps()
    transformed_laps = laps.copy()
    transformed_laps.loc[:,"LapTime (s)"] = laps["LapTime"].dt.total_seconds()
    team_order = (
        transformed_laps[["Team", "LapTime (s)"]]
        .groupby("Team")
        .median()["LapTime (s)"]
        .sort_values()
        .index
    )
    team_palette = {team: fastf1.plotting.team_color(team) for team in team_order}
    fig, ax = plt.subplots(figsize=(15, 10))
    sns.boxplot(
    data=transformed_laps,
    x="Team",
    y="LapTime (s)",
    hue="Team",
    order=team_order,
    palette=team_palette,
    whiskerprops=dict(color="white"),
    boxprops=dict(edgecolor="white"),
    medianprops=dict(color="grey"),
    capprops=dict(color="white"),
    )
    plt.grid(visible=False)
    ax.set(xlabel=None)
    plt.tight_layout()

def laptime_vs_lap(session: Session, drivers: list[Driver], **kwargs):
    fig, ax = plt.subplots()
    for driver in drivers:
        laps = session.laps.pick_drivers(driver.abbrevation).pick_track_status('1','equals')
        transformed_laps = laps.copy()
        transformed_laps.loc[:,"LapTime (s)"] = laps["LapTime"].dt.total_seconds()
        ax.plot(transformed_laps["LapNumber"],transformed_laps["LapTime (s)"],'-o',label=driver.abbrevation,color=driver.color,lw=0.7,markersize=2)
    ax.set_xlabel('Lap')
    ax.set_ylabel('Lap Time [s]')
    ax.legend()

def fc_laptime_vs_lap(session: Session, drivers: list[Driver], **kwargs):
    fig, ax = plt.subplots()
    for driver in drivers:
        laps = session.laps.pick_drivers(driver.abbrevation).pick_track_status('1','equals')
        transformed_laps = laps.copy()
        fuel_corrected_lap_time = fuel_corrected_laptime(transformed_laps['LapTime'], session.total_laps)
        transformed_laps.loc[:,"LapTime"] = fuel_corrected_lap_time
        transformed_laps.loc[:,"LapTime (s)"] = transformed_laps["LapTime"].dt.total_seconds()
        ax.plot(transformed_laps["LapNumber"],transformed_laps["LapTime (s)"],'-o',label=driver.abbrevation,color=driver.color,lw=0.7,markersize=2)
    ax.set_xlabel('Lap')
    ax.set_ylabel('Lap Time [s]')
    ax.legend()