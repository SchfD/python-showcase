import datetime
import time
from multiprocessing import Queue, Process
import pymongo
import numpy as np

mongo_cluster = pymongo.MongoClient("mongodb+srv://mongoAdmin:"
                                                 "SecureMongoPassword12@"
                                                 "pyprojectcluster.8qhpp.mongodb.net/"
                                                 "GreenhouseDB?retryWrites=true&w=majority")
mongo_database = mongo_cluster["GreenhouseDB"]
mongo_collection = mongo_database["GreenhouseCollection"]

service_queue = Queue()

SLEEP_INTERVAL = 10


def push_to_database(data_to_push):
    data_to_push["Time"] = str.replace(str(datetime.datetime.now()), " ", "T")
    service_queue.put(data_to_push)
    # mongo_collection.insert_one(data_to_push)


def query_last_element():
    return mongo_collection.find_one({}, sort=[('_id', pymongo.DESCENDING)])


def queue_process():
    print("Queue started!")
    while True:
        time.sleep(SLEEP_INTERVAL)
        print("Queue check!")
        while not service_queue.empty():
            data = service_queue.get()

            avg = np.mean(list(data["Temp"].values()))
            data["Temp"]["Average"] = avg

            mongo_collection.insert_one(data)


queue_thread = Process(target=queue_process)
queue_thread.start()
