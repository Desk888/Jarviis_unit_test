import os
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
   