import os
import logging
import pickle
import unittest
import shutil

def setup_directories(self):
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)

        # Percorsi delle directory
        log_dir = os.path.join(parent_dir, 'logs/crypto')
        data_dir = os.path.join(parent_dir, 'data')
        archive = os.path.join(parent_dir, 'test')
        backups_dir = os.path.join(parent_dir, 'backups')
        cache = os.path.join(data_dir, 'cache/' + self.symbols[self.symbol_key]['symbol1'])
        logging = os.path.join(log_dir, self.symbols[self.symbol_key]['symbol1'])
        
        # Creazione delle directory
        for directory in [log_dir, data_dir, archive, backups_dir, cache, logging]:
            if not os.path.exists(directory):
                os.makedirs(directory)

        # Configurazione delle directory
        dirs = {
            'log_dir': log_dir,
            'data_dir': data_dir,
            'cache': cache,
            'backups_dir': backups_dir,
            # Altre directory...
        }

        return dirs
    
    except Exception as e:
        print(f"Errore nella creazione delle directory: {e}")
        # Gestione dell'errore o ulteriori azioni

def setup_loggers(self):
    try:
        # Percorsi dei file di log
        log_files = {
            'console': os.path.join(self.directories['log_dir'], self.symbols[self.symbol_key]['symbol1'], 'console.log'),
            'alert': os.path.join(self.directories['log_dir'], self.symbols[self.symbol_key]['symbol1'], 'alert.log'),
            'dataframe': os.path.join(self.directories['log_dir'], self.symbols[self.symbol_key]['symbol1'], 'dataframe.log')
        }

        # Reset dei file di log esistenti
        for log_file in log_files.values():
            if os.path.exists(log_file):
                os.remove(log_file)

        # Inizializzazione dei logger
        logger1 = logging.getLogger('logger1')
        logger1.setLevel(logging.INFO)
        fh1 = logging.FileHandler(log_files['console'])
        fh1.setFormatter(logging.Formatter('%(asctime)s - "JARVIIS" - %(message)s'))
        logger1.addHandler(fh1)

        logger2 = logging.getLogger('logger2')
        logger2.setLevel(logging.INFO)
        fh2 = logging.FileHandler(log_files['alert'])
        fh2.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger2.addHandler(fh2)

        logger3 = logging.getLogger('logger3')
        logger3.setLevel(logging.INFO)
        fh3 = logging.FileHandler(log_files['dataframe'])
        logger3.addHandler(fh3)

        # Configurazione dei logger
        logs = {
            'logger1': logger1,
            'logger2': logger2,
            'logger3': logger3,
            # Altri logger...
        }

        return logs

    except Exception as e:
        print(f"Errore nella configurazione dei logger: {e}")
        # Gestione dell'errore o ulteriori azioni
def setup_pickle_files(self):
    currencies = {
        'BTC': {'sell': 999999999, 'buy': 1, 'acc':None},
        'ETH': {'sell': 999999999, 'buy': 1, 'acc':None},
        'SOL': {'sell': 999999999, 'buy': 1, 'acc':None},
        'AVAX': {'sell': 999999999, 'buy': 1, 'acc':None},
        'ADA': {'sell': 999999999, 'buy': 1, 'acc':None}
    }

    def create_pickle_file(cache_path, filename, default_value):
        pickle_file = os.path.join(cache_path, filename)
        if not os.path.exists(pickle_file):
            with open(pickle_file, 'wb') as file:
                pickle.dump(default_value, file)

    for currency in currencies.keys():
        cache_path = os.path.join(self.directories['data_dir'], 'cache', currency)
        os.makedirs(cache_path, exist_ok=True)
        create_pickle_file(cache_path, 'last_sell.pickle', currencies[currency]['sell'])
        create_pickle_file(cache_path, 'last_buy.pickle', currencies[currency]['buy'])
        create_pickle_file(cache_path, 'access.pickle', currencies[currency]['acc'])
   
#    UNIT TEST DEVE ESSERE FATTA SU UN FILE SEPARATO COME BEST PRACTICE PERCHE' MI DA
#    PROBLEMI VARI E CONFLITTI VARI CON IL FILE PRINCIPALE