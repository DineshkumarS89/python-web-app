import requests
from threading import Thread
import concurrent.futures
from sys import argv
import sys
import logging
import time

FORMAT = '%(asctime)-15s %(thread)d - %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(20)
home_page_response = {'timestamp':[],'duration':[]}
submit_page_response = {'timestamp':[],'duration':[]}

def generate_load(i,iter_count):
    logger.info(f"Starting the Thread:{i}")
    payload={'First':'Dineshkumar Sundaramoorthy'}
    url = "http://127.0.0.1:5000/"
    session = requests.Session()
    for i in range(iter_count):
        stime = time.time()
        response = session.get(url)
        etime = time.time()
        dur = etime - stime
        home_page_response['timestamp'].append(stime)
        home_page_response['duration'].append(dur)
        time.sleep(1-dur)
        stime = time.time()
        response = session.post(url+"submit",data=payload)
        etime = time.time()
        dur = etime - stime
        submit_page_response['timestamp'].append(stime)
        submit_page_response['duration'].append(dur)
        time.sleep(1-dur)
    logger.info(f"Finishing the Thread:{i}")

if __name__ == '__main__':
    if len(argv) < 4:
        logger.error("Incorrect Usage of the script: Run command 'python perf_test.py <total_users> <tps> <duration>'")
        sys.exit(-1)
    try:
        user = int(argv[1])
        tps = int(argv[2])
        duration = int(argv[3])
        iteration_per_user = (tps/user * duration)/2
        input = [int(iteration_per_user) for x in range(user)]
    except ValueError as v:
        logger.error("Incorrect value for Input arguments" + str(v))
        sys.exit(-1)
    except TypeError as t:
        logger.error("Incorrect type for Input arguments" + str(t))
        sys.exit(-1)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = executor.map(generate_load,range(user),input)

    print(f"Home Page: Total Hits: {len(home_page_response['duration'])}, avg response time: {sum(home_page_response['duration'])/len(home_page_response['duration']):.4f}, min response time: {min(home_page_response['duration']):.4f}, max response time: {max(home_page_response['duration']):.2f}")
    print(f"Submit Page: Total Hits: {len(submit_page_response['duration'])}, avg response time: {sum(submit_page_response['duration'])/len(submit_page_response['duration']):.4f}, min response time: {min(submit_page_response['duration']):.4f}, max response time: {max(submit_page_response['duration']):.2f}")