import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """метод, в котором вызывается 10 раз метод walk и сравнивается атрибут distance этого объекта со значением 50."""
        runner = Runner('test_runner')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        """метод, в  котором создаётся объект класса Runner с произвольным именем и вызовите run() у
    этого объекта 10 раз."""
    #После чего методом assertEqual сравните distance этого объекта со значением 100.
        pass

    def test_challenge(self):
        """метод в котором создаются 2 объекта класса Runner с произвольными именами."""
    #Далее  10 раз у объектов вызываются методы run и walk соответственно.Т.к.дистанции
    #должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
        pass

if __name__ == "__main__":
    unittest.main()
    print('Hello')
