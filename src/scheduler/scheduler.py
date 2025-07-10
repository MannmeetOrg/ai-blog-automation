import time

class Scheduler:
    def __init__(self, workflow):
        self.workflow = workflow

    def schedule_post(self, topic, audience, tone, publish_time):
        delay = (publish_time - time.time())
        if delay > 0:
            time.sleep(delay)
        self.workflow.run(topic, audience, tone)
