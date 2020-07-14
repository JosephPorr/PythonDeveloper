from argparse import Action, ArgumentParser

# argparse is a container to hold an argument.

# Below is the list of parameters passed as keyword arguments.
# https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():  #  Need to create parser function to return a function.
    parser = ArgumentParser(description="""
    Bash up PostgreSQL database locally or to AWS S3.
    """)

    parser.add_argument("url", help="URL of database to backup"
    # By adding this module you can call an argument based on name
    parser.add_argument("--driver",
            help="how & where to store backup",
            nargs=2,
            action=DriverAction,
            required=True)

    return parser

