class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def autolog(name, message=None):
    "Automatically log the current function details."
    import inspect, logging
    # Get the previous frame in the stack, otherwise it would
    # be this function!!!
    func = inspect.currentframe().f_back.f_code
    funs = inspect.currentframe().f_back
    logs = inspect.currentframe().f_code
    # Dump the message + the name of this function to the log.
    # logging.debug("%s: %s in %s:%i" % (
    #     message,
    #     func.co_name,
    #     func.co_filename,
    #     func.co_firstlineno
    # ))
    print(f"\n{bcolors.WARNING} ==============^=============>{bcolors.ENDC}")
    print(f"{bcolors.HEADER}  N: {name} = {bcolors.OKCYAN}:", end="")
    print(message)

    print(f"{bcolors.OKGREEN} {func.co_name} in {func.co_filename}:{funs.f_lineno}")
    print(f" Log Func--------{bcolors.ENDC}")
    print(f"  {logs.co_filename}:{logs.co_firstlineno}")
    print(f"{bcolors.WARNING} ==============___==============||\n{bcolors.ENDC}")


    # print(f"The Function Message={message}: {func.co_name} in {func.co_filename}:{func.co_firstlineno}")
    # print(f"The Log::\n name:= {funs.f_lineno},, :")

def autolog_plus(name, message=None):
    "Automatically log the current function details."
    import inspect, logging
    # Get the previous frame in the stack, otherwise it would
    # be this function!!!
    func = inspect.currentframe().f_back.f_back.f_code
    funs = inspect.currentframe().f_back.f_back
    logs = inspect.currentframe().f_code
    # Dump the message + the name of this function to the log.
    # logging.debug("%s: %s in %s:%i" % (
    #     message,
    #     func.co_name,
    #     func.co_filename,
    #     func.co_firstlineno
    # ))
    print(f"{bcolors.HEADER} !!!!!!!!!````````````````>{bcolors.ENDC}")
    print(f"{bcolors.WARNING}  N: {name} = {bcolors.OKCYAN}:", end="")
    print(message)
    print(f"{bcolors.OKGREEN} {func.co_name} in {func.co_filename}:{funs.f_lineno}")
    print(f" Log Func--------{bcolors.ENDC}")
    print(f"  {logs.co_filename}:{logs.co_firstlineno}")
    print(f"{bcolors.HEADER} |||||||||||||||||||||{bcolors.ENDC}\n")

