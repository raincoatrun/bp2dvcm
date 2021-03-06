import logging
from time import sleep
from recorddetail3 import RecordDetail, record_detail

LOG = logging.getLogger(__name__)


class MyProcess():

    def __init__(self,):
        self.numbers = list(range(0, 10))

    def step_one(self):
        with record_detail('one') as d:
            LOG.info('Doing step one with %s', type(d))
            self.numbers = [n + 2 for n in self.numbers]

    def step_two(self):
        with record_detail('two'):
            LOG.info('Doing step two')
            self.numbers = [n * 2 for n in self.numbers]
            sleep(1)

    def step_three(self):
        with RecordDetail('three') as d:
            LOG.info('Doing step three with %s', type(d))
            self.numbers = [(n - 2) / (n - 4) for n in self.numbers]

    def run(self):
        self.step_one()
        LOG.info(self.numbers)
        self.step_two()
        LOG.info(self.numbers)
        self.step_three()
        LOG.info(self.numbers)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    process = MyProcess()
    process.run()
