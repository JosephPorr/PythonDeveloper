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
    parser.add_argument("--driver", '-d',
            help="how & where to store backup",
            nargs=2,
            metavar=("DRIVER", "DESTINATION"),
            action=DriverAction,
            required=True)

    return parser

def main():
    import boto3
    import time
    from pgbackup import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        client = boto3.client('s3')
        timestamp = time.strftime("%Y-%m-%dT%H-%M', time.localtime"())   # https://docs.python.org/3/library/time.html#time.strftime
        file_name = pgdump.dump_file_name(args.url, timestamp)
        print(f"Backing database up to {args.destination} in S3 as {file_name}")
        # TODO: create a better name based on the database name and the date
        storage.s3(client, dump.stdout, args.destination, file_name)
    else:
        outfile = open(args.destination, 'wb')
        storage.local(dump.stdout, outfile)

        # Joe@Joe-PC MINGW64 ~/Documents/GitHub/PythonDeveloper/argparserpackage (master)
        # $ pip install -e .  The -e means install from local enviroment