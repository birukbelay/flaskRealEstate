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


def autolog(message):
    "Automatically log the current function details."
    import inspect, logging
    # Get the previous frame in the stack, otherwise it would
    # be this function!!!
    func = inspect.currentframe().f_back.f_code
    funs = inspect.currentframe().f_back
    logs = inspect.currentframe().f_code
    # Dump the message + the name of this function to the log.
    logging.debug("%s: %s in %s:%i" % (
        message,
        func.co_name,
        func.co_filename,
        func.co_firstlineno
    ))
    print(f"{bcolors.WARNING} ============================>{bcolors.ENDC}")
    print(f"The LogPlace\n Message={message}:\n {func.co_name} in {func.co_filename}:{funs.f_lineno}")
    print(f" BOld{bcolors.BOLD} ==----***{bcolors.ENDC}")
    print(f" Lof fun = in {logs.co_filename}:{logs.co_firstlineno}")
    print(f"{bcolors.WARNING} ============================||{bcolors.ENDC}")

    print(f" {bcolors.HEADER} ==-Test Header ---***{bcolors.ENDC}")
    print(f" {bcolors.OKBLUE} ==-Test Okblue ---***{bcolors.ENDC}")
    print(f" {bcolors.OKCYAN} ==-Test OKCYAN ---***{bcolors.ENDC}")
    print(f" {bcolors.OKGREEN} ==-Test OK GREEN ---***{bcolors.ENDC}")
    print(f" {bcolors.BOLD} ==-Test OKBold ---***{bcolors.ENDC}")
    print(f" {bcolors.WARNING} ==-Test OkWarning ---***{bcolors.ENDC}")
    print(f" {bcolors.FAIL} ==-Test Fail ---***{bcolors.ENDC}")
    print(f" {bcolors.ENDC} ==-Test ENDC ---***{bcolors.ENDC}")
    print(f" {bcolors.UNDERLINE} ==-Test Underline ---***{bcolors.ENDC}")
    # print(f"The Function Message={message}: {func.co_name} in {func.co_filename}:{func.co_firstlineno}")
    # print(f"The Log::\n name:= {funs.f_lineno},, :")

