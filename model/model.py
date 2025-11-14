from operator_mod.eventbus.event_handler import EventManager
from operator_mod.in_mem_storage.in_memory_data import InMemoryData

from model.data.configuration_manager import ConfigurationManager

class Model():
    """This class handles all data management and executes r/w operations and data filtering. Data calculations are part of the Controller."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Model, cls).__new__(cls)
        return cls._instance

    def __init__(self):

        self.events = EventManager()
        self.data = InMemoryData()
        self.configuirations = ConfigurationManager() # Inits the configs for our devices

    def start_model(self):

        # Basic Information setup
        self.data.add_data(self.data.Keys.PROJECT_PATH, None, self.data.Namespaces.DEFAULT)
