import belch.parse
import belch.controllers
import sys

def main():

    a = api.Api("scatx.cloud.caresource.corp")

    commands = {
        "stats": controllers.Stats(a),
        "vulns": controllers.Vulns(a),
        "types": controllers.Types(a),
        "languages": controllers.Languages(a)
    }

    welcome(commands)
    while True:

        while True:
            inst = prompt()


            if inst[0] == "exit":
                sys.exit()

            if inst[0] == "help":
                if len(inst) == 2 and inst[1] in commands.keys():
                    commands[inst[1]]._help()
                else:
                    welcome(commands)
                break

            if inst[0] in commands.keys():
                commands[inst[0]]._run(inst)
                break

            welcome(commands)
            break


def prompt():
    r = input("\n\033[91m{}\033[00m ".format("belch#"))
    print("")
    return (r.split(" "))



def welcome(commands):
    print(("<" * 45 ) + " belch CLI " + (">" * 45) + "\n")
    print("Commands: " +  " ".join(commands.keys()) + " help exit\n")
    print("Help Usage: help [command]")







if __name__ == "__main__":
    main()
