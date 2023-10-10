from celery import shared_task


@shared_task(ignore_result=False)
def simulate() -> float:
    # FIXME:
    # load model
    # start simulation
    # return value
    return 1234567890
