# Hard 2: Stoplight

There is a stoplight which starts every day by being red for 2 minutes and then green for 4 minutes. This repeats until midnight of the next day. Cars must queue in line when the light is red. Cars may move through the intersection at a rate of 4 cars per minute when the light is green. Cars arrive at the intersection at a rate of 2 per minute for the entire day.

There is daily maintenance scheduled from `[8:00AM - 8:59AM]` where the light is red for the entire time. The locals know this, but not foreigners, so the car arrival rate dwindles to 1 per minute during that time.

There is a car accident at `11:15AM` which causes the intersection to be blocked for 35 minutes.

A jaywalker crosses the intersection at `12:08PM`, no cars can pass during that minute.

At `2:24PM`, the light malfunctions and the next two minutes which are supposed to be red are now green. It gets fixed for the next cycle.

At `3:49PM`, a single car runs the red light. They get reprimanded by the police a block away.

There is a rush hour from `[5PM-5:59PM]` as everyone gets off of work. The car arrival rate is now 2.5 per minute during this time.

A tree falls in the intersection at `8:23PM`. Cars can begin crossing again at `8:36PM` when they finally move the tree.

How many cars have passed through the intersection today? `[12:00AM - 11:59PM]`

### Solution

The key is to realize that the queue for the light is empty at midnight. This means all cars have passed through the intersection. This assumption can be verified by calculating that the queue will be losing 4 cars per red/green cycle (every 6 minutes) during the normal time. Since there are 10 cycles per hour, the queue will be losing 40 cars per hour, so it will drain much faster than the red lights have made it build up throughout the day.

Now the problem goes from being "how many cars have passed through the intersection" to "how many cars have arrived to the queue" which is much simpler to calculate. All of the shenanigans with the red and green light can be ignored.

If the day was normal, there would be 2 cars per minute for 1,440 minutes which is 2,880 cars. The car rate drops during maintenance, so subtract 60. The car rate increases during rush hour, so add 30.

2,850 cars have arrived and passed through the intersection.