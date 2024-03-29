from fastf1.core import Session
import numpy as np
from matplotlib import pyplot as plt

class Driver:
    def __init__(self, abbreviation: str, color: str) -> None:
        self.abbrevation = abbreviation
        self.color = color

def lap_speed_comparision(session: Session, drivers: list[Driver], laps: list[int]):
    """Give driver comparision data"""
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
    plt.show()



    