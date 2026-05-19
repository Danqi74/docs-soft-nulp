from context.output_context import OutputContext
from strategy_factory import get_strategy
from readers.csv_reader import CsvReader


def main():
    reader = CsvReader()
    data = reader.read()

    strategy = get_strategy()
    context = OutputContext(strategy)

    context.execute(data)

if __name__ == "__main__":
    main()