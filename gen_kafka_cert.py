from __future__ import print_function, unicode_literals

import os
import os.path
import tempfile
import kafka_cert
import urllib3
import shutil
from config import config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def addKafkaConfig():
    cKey, cCert, caCert = getKafkaCerts()
    config["kafka"]["key"] = cKey.encode()
    config["kafka"]["cert"] = cCert.encode()
    config["kafka"]["cacert"] = caCert.encode()
    host = config["apic_host"].split(":")[0]
    config["kafka"]["broker"] = host + ":9093"

def getKafkaCerts():
    wdir = tempfile.mkdtemp()
    previous_dir = os.getcwd()
    apic_host = config["apic_host"]
    user = config["apic_login"]["username"]
    pwd = config["apic_login"]["password"]
    cn = config["system_id"]
    kafka_cert.logger = kafka_cert.set_logger(wdir, "kc.log")
    res = kafka_cert.generate(wdir, apic_host, cn, user, pwd)
    if not res:
        raise(Exception("Failed to get kafka certs"))

    readDict = {
        "server.key": "",
        "server.crt": "",
        "cacert.crt": "",
    }

    dir = wdir + "/"
    for fname in readDict:
        shutil.copy(dir + fname, previous_dir)
        f = open(dir + fname, "r")
        readDict[fname] = f.read()
        f.close()

    

    os.system('rm -rf ' + wdir)
    return readDict["server.key"], readDict["server.crt"], readDict["cacert.crt"]

def main():
    print("Starting Certificate Generation...")
    addKafkaConfig()
    print(config)

if __name__ == "__main__":
    main()