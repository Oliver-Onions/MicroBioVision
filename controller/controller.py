
from apscheduler.schedulers.background import BackgroundScheduler

from operator_mod.logger.global_logger import Logger

from controller.algorithms.algorithm_manager_class.algorithm_manager import AlgorithmManager

class Controller:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Controller, cls).__new__(cls)
        return cls._instance

    def __init__(self):

        self.logger = Logger("Controller").logger
        self.health_check_scheduler = BackgroundScheduler()

    def start_controller(self):

        # This is an runtime thread that exists throughout the application runtime. Thats why its a deamon thread that kills itslef when application ends.

        self.alg_man = AlgorithmManager()
        

        

                
    def shutdown(self):
        
        try:

            self.alg_man.shutdown()
                        
        except Exception as e:
            self.logger.error(f"Shutdown error: {e}")
