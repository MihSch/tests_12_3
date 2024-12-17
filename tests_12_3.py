import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
             return method(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        name = Runner('John')
        for i in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)

    @skip_if_frozen
    def test_run(self):
        n = Runner('n')
        for i in range (10):
            n.run()
        self.assertEqual(n.distance, 10)

    @skip_if_frozen
    def test_challenge(self):
        n1 = Runner('n1')
        n2 = Runner('n2')
        for i in range (10):
            n1.run()
            n2.walk()
        self.assertNotEqual(n1.distance, n2.distance)

if __name__ == '__main__':
    unittest.main()


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @skip_if_frozen
    def setUp(self):
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    @skip_if_frozen
    def test_run1(self):
        n = Tournament(90, self.r1, self.r2, self.r3)
        res = Tournament.start(n)
        self.all_results['test1'] = res

    @skip_if_frozen
    def test_run2(self):
        n = Tournament(90, self.r1, self.r2)
        res = Tournament.start(n)
        self.all_results['test2'] = res

    @skip_if_frozen
    def test_run3(self):
        n = Tournament(90, self.r2, self.r3)
        res = Tournament.start(n)
        self.all_results['test3'] = res

    @skip_if_frozen
    def test_run4(self):
        n = Tournament(90, self.r1, self.r3)
        res = Tournament.start(n)
        self.all_results['test4'] = res

if __name__ == '__main__':
    unittest.main()