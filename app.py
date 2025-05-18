import os
from flask import Flask, request, jsonify
from redis import Redis
from rq import Queue
import numpy as np
import time

app = Flask(__name__)
redis_conn = Redis(host='redis', port=6379)
queue = Queue(connection=redis_conn)

def long_running_task(param):
    # Simulate a long-running task using numpy
    time.sleep(10)
    matrix = np.random.rand(1000, 1000)
    result = np.mean(matrix)
    return {'result': result}

@app.route('/start-task', methods=['POST'])
def start_task():
    data = request.json
    job = queue.enqueue(long_running_task, data['param'])
    return jsonify({'job_id': job.get_id()}), 202

@app.route('/task-result/<job_id>', methods=['GET'])
def get_task_result(job_id):
    job = queue.fetch_job(job_id)
    if job is None:
        return jsonify({'error': 'Job not found'}), 404

    if job.is_finished:
        result = job.result
        return jsonify({'status': 'completed', 'result': result}), 200
    elif job.is_failed:
        return jsonify({'status': 'failed', 'result': job.exc_info}), 500
    else:
        return jsonify({'status': 'in-progress'}), 202

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


