

import gevent
import time

def women_moan():
    print('meow')
    gevent.sleep(0)
    print('meowwwwwww')

def man_moan():
    print('wooff')
    gevent.sleep(0)
    print('wooooofffff')


# time comparison 
sync_time_start = time.time()
women_moan()
man_moan()
sync_time_end = time.time()
print("\n#time taken for sync:",sync_time_end - sync_time_start,"\n\n")

async_time_start = time.time()
gevent.joinall([gevent.spawn(women_moan),gevent.spawn(man_moan)])
async_time_end = time.time()
print("\n#time taken for async:",async_time_end - async_time_start)
