import json
from flask import Flask
from flask import request
from flask_cors import CORS
import serial

import logging
import os #utilizado para pegar os valores que estão na variável de ambiente
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)
load_dotenv() #carrega as variveis de ambiente

logger = logging.getLogger("AIPO_NFC_READER")
logging.basicConfig(filename='allLogs.log', encoding='ISO-8859-1', level=logging.DEBUG)

# handle para lidar com o terminal
terminal_logger = logging.StreamHandler()
terminal_logger.setLevel(logging.DEBUG)

# handle para lidar com o arquivo
file_logger = logging.FileHandler("nfcReader.log", encoding='ISO-8859-1')
file_logger.setLevel(logging.WARNING)

# create formatter
formatter = logging.Formatter('%(name)s:%(levelname)s \t- - %(asctime)s %(message)s', datefmt='[%d/%m/%Y %H:%M:%S]')

# add formatter to handles
terminal_logger.setFormatter(formatter)
file_logger.setFormatter(formatter)

# add handles to logger
logger.addHandler(terminal_logger)
logger.addHandler(file_logger)

app.config['API_HOST'] = os.getenv("API_HOST")


@app.route('/serialAvailable', methods = ['GET'])
def serialAvailable():
  try:
    portaSerial = serial.Serial('/dev/ttyUSB0', 115200)
  except:
    return {"status":"problemas ao abrir a porta serial"}
  return  {"status":"ok"}

@app.route('/readCommand', methods = ['GET'])
def readCommand():
  try:
    portaSerial = serial.Serial('/dev/ttyUSB0', 115200)
  except:
    return {"status":"problemas ao abrir a porta serial"}

  if portaSerial.isOpen():
    try:
      portaSerial.write(b'p');
      incoming = portaSerial.readline()
    except Exception as e:
      logger.warning(str(e))
      return {"status":str(e)}
    portaSerial.close()
  else:
    return {"status": "porta serial fechada"}
  
  data = json.loads(incoming)

  comando = data["comando"]

  # logger.debug(comando)
  
  return  {"status":"ok", "comando": comando}
