from strategies.output.strategy import OutputStrategy

class ConsoleOutput(OutputStrategy):
    def output(self, data):
        for item in data:
            print(item)