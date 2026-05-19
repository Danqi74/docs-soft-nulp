from strategies.output.strategy import OutputStrategy

class FileOutput(OutputStrategy):
    def output(self, data):
        with open("output.txt", "w", encoding="utf-8") as f:
            for item in data:
                f.write(str(item) + "\n")