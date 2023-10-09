from model.anchor import root_dir


def run():
    # be sure to configure your ide to use 'model' as the working directory for the python runner.

    # make sure that whenever you access files that you do so with a path starting with root_dir().
    training_data_path = root_dir() + "training_data/"

    print("Hello World")
    print(training_data_path)


if __name__ == "__main__":
    run()
