import os
import sys
from zipfile import ZipFile
import shutil
from datasrc.exception.custom_exception import DataException

class DataStore:
    def __init__(self):
        self.root = os.path.join(os.getcwd(), "data")
        self.zip = os.path.join(self.root, "archive.zip")
        self.images = os.path.join(self.root, "images-101")
        #self.list_unwanted = ["BACKGROUND_Google"]
        self.list_unwanted = ['accordion', 'anchor', 'ant', 'BACKGROUND_Google', 'barrel', 'bass', 'beaver', 'binocular', \
                              'bonsai', 'brain', 'brontosaurus', 'buddha', 'butterfly', 'camera', 'cannon', 'car_side', \
                                 'ceiling_fan', 'cellphone', 'chair', 'chandelier', 'cougar_body', 'cougar_face', 'crab', \
                                    'crayfish', 'crocodile', 'crocodile_head', 'cup', 'dalmatian', 'dollar_bill', 'dolphin',\
                                          'dragonfly', 'electric_guitar', 'elephant', 'emu', 'euphonium', 'ewer', 'Faces', \
                                            'Faces_easy', 'ferry', 'flamingo', 'flamingo_head', 'garfield', 'gerenuk', \
                                                'gramophone', 'grand_piano', 'hawksbill', 'headphone', 'hedgehog', 'helicopter', \
                                                    'ibis', 'inline_skate', 'joshua_tree', 'kangaroo', 'ketch', 'lamp', 'laptop',\
                                                          'Leopards', 'llama', 'lobster', 'lotus', 'mandolin', 'mayfly', 'menorah',\
                                                              'metronome', 'minaret', 'nautilus', 'octopus', 'okapi', 'pagoda', 'panda',\
                                                                  'pigeon', 'pizza', 'platypus', 'pyramid', 'revolver', 'rhino', \
                                                                    'rooster', 'saxophone', 'schooner', 'scissors', 'scorpion', \
                                                                        'sea_horse', 'snoopy', 'soccer_ball', 'stapler', 'starfish',\
                                                                              'stegosaurus', 'stop_sign', 'strawberry', 'sunflower', \
                                                                                'tick', 'trilobite', 'umbrella', 'watch', 'water_lilly',\
                                                                                      'wheelchair', 'wild_cat', 'windsor_chair', 'wrench',\
                                                                                          'yin_yang']

    def prepare_data(self):
        try:
            print(" Extracting Data ")
            with ZipFile(self.zip, 'r') as files:
                files.extractall(path=self.root)

            files.close()
            print(" Process Completed ")
        except Exception as e:
            message = DataException(e, sys)
            return {"Created": False, "Reason": message.error_message}

    def remove_unwanted_classes(self):
        try:
            print(" Removing unwanted classes ")
            for label in self.list_unwanted:
                path = os.path.join(self.images,label)
                shutil.rmtree(path, ignore_errors=True)
            print(" Process Completed ")
        except Exception as e:
            message = DataException(e, sys)
            return {"Created": False, "Reason": message.error_message}

    def sync_data(self):
        try:
            print("\n====================== Starting Data sync ==============================\n")
            os.system(f"aws s3 sync { self.images } s3://put-name-of-s3-bucket-here/images/ ")
            print("\n====================== Data sync Completed ==========================\n")

        except Exception as e:
            message = DataException(e, sys)
            return {"Created": False, "Reason": message.error_message}

    def run_step(self):
        try:
            self.prepare_data()
            self.remove_unwanted_classes()
            self.sync_data()
            return True
        except Exception as e:
            message = DataException(e, sys)
            return {"Created": False, "Reason": message.error_message}


if __name__ == "__main__":
    store = DataStore()
    store.run_step()
