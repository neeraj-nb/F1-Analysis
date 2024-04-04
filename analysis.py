import fastf1.plotting
from fastf1 import utils
from fastf1.core import Session
import numpy as np
from matplotlib import pyplot as plt

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
    def __init__(self, abbreviation: str, color: str, team: Team) -> None:
        self.abbrevation = abbreviation
        self.color = color
        self.team = team

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