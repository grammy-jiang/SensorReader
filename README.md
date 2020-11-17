# SensorReader

This project is to read the environment sensors of Sense HAT:

* humidity
* temperature from humidity sensor
* pressure
* temperature from pressure sensor

## Asynchronous Reader

This project is to read the sensors asynchronously.

[uvloop](https://github.com/MagicStack/uvloop) is adopted for the event loop as
default.

### Reader

In the reader,
[`asyncio.gather`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather)
is used to read the sensors asynchronously.

### Pipelines

In the pipelines, adopting the asynchronous dependencies or drivers is the
highest priority.

* [aiokafka](https://github.com/aio-libs/aiokafka) for Apache Kafka
* [asyncpg](https://github.com/MagicStack/asyncpg) for PostgreSQL
* [Motor](https://github.com/mongodb/motor) for MongoDB

### [APScheduler](https://github.com/agronholm/apscheduler)

Use
[`AsyncIOScheduler`](https://apscheduler.readthedocs.io/en/stable/modules/schedulers/asyncio.html#apscheduler.schedulers.asyncio.AsyncIOScheduler)
to schedule reading the sensors.

# Reference

## Sense HAT

* [astro-pi/python-sense-hat: Source code for Sense HAT Python library](https://github.com/astro-pi/python-sense-hat)
    * [Home - Sense HAT](https://pythonhosted.org/sense-hat/)
* [Getting started with the Sense HAT - Introduction | Raspberry Pi Projects](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat)
* [Buy a Sense HAT – Raspberry Pi](https://www.raspberrypi.org/products/sense-hat/)
* [Sense HAT - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/hardware/sense-hat/)
* [The possibilities of the Sense HAT - Raspberry Pi](https://www.raspberrypi.org/blog/sense-hat-projects/)

## AsyncIO

* [asyncio — Asynchronous I/O — Python 3.9.0 documentation](https://docs.python.org/3/library/asyncio.html)
