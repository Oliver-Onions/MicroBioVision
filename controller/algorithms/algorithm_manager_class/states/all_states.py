

from concurrent.futures import ProcessPoolExecutor



from controller.algorithms.pellet_sizer.pellet_sizer import PelletSizer
from controller.algorithms.algorithm_manager_class.states.state_baseclass import State


class PelletSizerSingleState(State):
    
    def run_logic(self):
        
        # Grabbing the reference PelletsizerWidget
        reference = self.data.get_data(self.data.Keys.PELLET_SIZER_WIDGET_REFERENCE, self.data.Namespaces.DEFAULT)

        ### Get the information
        self.target_paths = self.data.get_data(self.data.Keys.PELLET_SIZER_IMAGES, self.data.Namespaces.DEFAULT)
        self.target_settings = self.data.get_data(self.data.Keys.PELLET_SIZER_IMAGE_SETTINGS, self.data.Namespaces.DEFAULT)
        
        pelletsizer = PelletSizer()

        reference._progressbar_update(0.2)
        
        results = []
        with ProcessPoolExecutor() as executor:
            
            try:
                futures = []
                for i, path in enumerate(self.target_paths):
                    
                    futures.append(executor.submit(pelletsizer.processing, path, True, self.target_settings[i]))
                
                reference._progressbar_update(0.5)
                
                for future in futures:
                    result = future.result()

                    if results is not None:
                        results.append(result)

                reference._progressbar_update(0.9)

            except Exception as e:
                self.logger.error(f"Error occured in pellet sizer: {e}.")

        self.data.add_data(self.data.Keys.PELLET_SIZER_RESULT, results, self.data.Namespaces.DEFAULT)

        reference.pellet_sizing_done.emit()
        

