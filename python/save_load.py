import pickle
import os
from platformdirs import user_data_dir

class SaveLoadManager():
    __save_path = user_data_dir("RecipeApp")

    @staticmethod
    def save(data):
        """Called whenever something is changed, saves to binary file using pickle"""
        save_dir = SaveLoadManager.__save_path
        saved_file_path = save_dir + "\savefile.bin"
        if not os.path.exists(save_dir): os.makedirs(save_dir)
        with open(saved_file_path, "wb") as file: pickle.dump(data, file)

    @staticmethod
    def load():
        """Called on login, loads all saved data from binary file using pickle"""
        save_dir = SaveLoadManager.__save_path
        saved_file_path = save_dir + "\savefile.bin"
        if not os.path.exists(save_dir): os.makedirs(save_dir)
        if not os.path.isfile(saved_file_path):
            with open(saved_file_path, "wb") as file: pickle.dump({}, file)
        with open(saved_file_path, "rb") as file: return (pickle.load(file))
        return {}