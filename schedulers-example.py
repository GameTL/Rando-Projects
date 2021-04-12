from apscheduler.schedulers.blocking import BlockingScheduler
count = 1
sched = BlockingScheduler()


@sched.scheduled_job('interval', seconds=1/60)
def scheduled_job():
    global count
    print('This job ran {0} times'.format(count))
    count = count + 1


scheduled_job()
sched.start()
