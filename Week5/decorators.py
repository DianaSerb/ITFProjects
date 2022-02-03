import psutil as psutil


def get_virtual_memory():
    print(psutil.virtual_memory().percent)


# get_virtual_memory()


def get_virtual_memory_2():
    return psutil.virtual_memory().percent


# a = get_virtual_memory_2()
# print(a)


def display_test_logs(msg):  # nested functions
    def logger():
        print(f"Logging memory data {get_virtual_memory_2()}{msg}")

        def test():
            print("Hello")

        test()

    logger()


display_test_logs("thumbs up")


def display_test_logs_v2():
    threshold = 90

    def logger():
        print(threshold)

    return logger


display_test_logs_v2()()
