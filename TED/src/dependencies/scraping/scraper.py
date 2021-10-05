# import your dependencies here


class MyClass:
    def __init__(self, **kwargs):
        self.config = kwargs.get("config")

    def do_something(self):
        """Do extraction or processing of data here"""
        return None

    def load_data(self):
        """Function to load data"""
        return None

    def save_data(self):
        """Function to save data"""
        return None

    def run(self):
        """Load data, do_something and finally save the data"""
        return None


if __name__ == "__main__":
    config = {}
    obj = MyClass(config = config)
    obj.run()