import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(message)s')

project_name = "summarizer"

files =[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py", # we got 5 levels of logging: debug, info, warning, error, critical as of now info is enabled.
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "app.py", 
    "params.yaml",
    "requirements.txt",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/trials.ipynb",
    #".gitignore"
]

for fpath in files:
    fpath = Path(fpath)
    fdir, fname = os.path.split(fpath)

    if fdir != "":
        os.makedirs(fdir, exist_ok = True)
        logging.info(f"Creating file directory {fdir}")
    
    if (not os.path.exists(fpath)) or (os.path.getsize(fpath) == 0):
        with open(fpath, 'w') as f:
            pass
            logging.info(f"creating empty file {fname}")
    else:
        logging.info(f"File {fname} already exists")