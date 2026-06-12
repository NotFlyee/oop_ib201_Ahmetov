from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_state(self, state: str):
        pass

class TV(Device):
    def __init__(self):
        self.is_on = 0
        self.state = None

class Light(Device):
    def __init__(self):
        self.is_on = 0
        self.state = "50%"

class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()

    def set_state(self, state: str):
        self.device.set_state(state)

class SonyTV(TV):
    def turn_on(self):
        if self.is_on:
            return
        self.is_on = 1
        print('SonyTV включен')

    def turn_off(self):
        if not self.is_on:
            return
        self.is_on = 0
        print('SonyTV выключен')

    def set_state(self, state: str):
        self.state = state
        print(f'Канал SonyTV переключен на {self.state}' if self.is_on else '')

class SamsungTV(TV):
    def turn_on(self):
        if self.is_on:
            return
        self.is_on = 1
        print('SamsungTV включен')

    def turn_off(self):
        if not self.is_on:
            return
        self.is_on = 0
        print('SamsungTV выключен')

    def set_state(self, state: str):
        self.state = state
        print(f'Канал SamsungTV переключен на {self.state}' if self.is_on else '')

class PhilipsLight(Light):
    def turn_on(self):
        if self.is_on:
            return
        self.is_on = 1
        print('PhilipsLight включен')

    def turn_off(self):
        if not self.is_on:
            return
        self.is_on = 0
        print('PhilipsLight выключен')

    def set_state(self, state: str):
        self.state = state
        print(f'Яркость PhilipsLight установлена на {self.state}')

class IKEALight(Light):
    def turn_on(self):
        if self.is_on:
            return
        self.is_on = 1
        print('IKEALight включен')

    def turn_off(self):
        if not self.is_on:
            return
        self.is_on = 0
        print('IKEALight выключен')

    def set_state(self, state: str):
        self.state = state
        print(f'Яркость IKEALight установлена на {self.state}')
