from fastf1 import utils
from fastf1.core import Session
import numpy as np
from matplotlib import pyplot as plt

class Driver:
    def __init__(self, abbreviation: str, color: str) -> None:
        self.abbrevation = abbreviation
        self.color = color

def lap_speed_comparision_time(session: Session, drivers: list[Driver], laps: list[int], **kwargs):
    """Give driver comparision data"""
    if "ax" in kwargs:
        ax = kwargs["ax"]
    else:
        fig, ax = plt.subplots()
    for driver, lap in zip(drivers, laps):
        lap_data = session.laps.pick_driver(driver.abbrevation).pick_lap(lap)
        car_data = lap_data.get_car_data()
        time = car_data['Time']
        vCar = car_data['Speed']
        ax.plot(time, vCar, label=f'{driver.abbrevation} Lap {lap}', color=driver.color)
    ax.set_xlabel('Time')
    ax.set_ylabel('Speed [Km/h]')
    ax.set_title('Lap Speed')
    ax.legend()

def lap_speed_comparision(session: Session, drivers: list[Driver], laps: list[int], **kwargs):
    if "ax" in kwargs:
        ax = kwargs["ax"]
    else:
        fig, ax = plt.subplots()
    for driver, lap in zip(drivers, laps):
        lap_data = session.laps.pick_driver(driver.abbrevation).pick_lap(lap)
        tel = lap_data.get_telemetry()
        dist = tel['Distance']
        vCar = tel['Speed']
        ax.plot(dist, vCar, label=f'{driver.abbrevation} Lap {lap}', color=driver.color)
    ax.set_xlabel('Distance [m]')
    ax.set_ylabel('Speed [Km/h]')
    ax.set_title('Lap Speed')
    ax.legend()

def lap_delta(session: Session, drivers: list[Driver], laps: list[int], **kwargs):
    if "ax" in kwargs:
        ax = kwargs["ax"]
    else:
        fig, ax = plt.subplots()
    ref_lap_data = session.laps.pick_driver(drivers[0].abbrevation).pick_lap(laps[0])
    for driver, lap in zip(drivers, laps):
        lap_data = session.laps.pick_driver(driver.abbrevation).pick_lap(lap)
        delta, ref_tel, comp_tel = utils.delta_time(ref_lap_data,lap_data)
        ax.plot(ref_tel['Distance'], delta, '--', label=f'{driver.abbrevation} Lap {lap}', color=driver.color)
    ax.set_xlabel('Distance [m]')
    ax.set_ylabel('Delta [s]')
    ax.set_title('Lap delta')
    ax.legend()

def lap_throttle(session: Session, drivers: list[Driver], laps: list[int], **kwargs):
    if "ax" in kwargs:
        ax = kwargs["ax"]
    else:
        fig, ax = plt.subplots()
    for driver, lap in zip(drivers, laps):
        lap_data = session.laps.pick_driver(driver.abbrevation).pick_lap(lap)
        tel = lap_data.get_telemetry()
        dist = tel['Distance']
        throttle = tel['Throttle']
        ax.plot(dist, throttle, label=f'{driver.abbrevation} Lap {lap}', color=driver.color)
    ax.set_xlabel('Distance [m]')
    ax.set_ylabel('Throttle [%]')
    ax.set_title('Throttle')
    ax.legend()