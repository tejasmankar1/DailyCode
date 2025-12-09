from dotenv import load_dotenv
load_dotenv()

from .client.rq_client import queue
from fastapi import FastAPI,Query
from .queues.worker import process_query

app = FastAPI()

@app.route('/')
def root():
    return {"status": 'Server is running'}

@app.post('/chat')
def chat(
        query: str = Query(...,description="The chat query of user")
):
    job = queue.enqueue(process_query ,query)
    return {"status" : "queued", "job_id" : job.id}

@app.get('/job-status')
def get_result(
        job_id : str = Query(..., description="JOB ID")
):
    job = queue.fetch_job(job_id=job_id)
    result = job.return_value()
    return {"result" :result}