import openai
from config import AGENT_ASSISTANT_IDS
import time

def delegate_task(agent_name, task_prompt):
    assistant_id = AGENT_ASSISTANT_IDS.get(agent_name)
    if not assistant_id:
        return {"error": "Unknown agent"}

    thread = openai.beta.threads.create()
    openai.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=task_prompt
    )

    run = openai.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id
    )

    while True:
        run_status = openai.beta.threads.runs.retrieve(run_id=run.id, thread_id=thread.id)
        if run_status.status == "completed":
            break
        time.sleep(1)

    messages = openai.beta.threads.messages.list(thread_id=thread.id)
    latest_message = messages.data[0].content[0].text.value
    return {"output": latest_message}