TITLE = "TASK TRACKER"
VER = "v 0.0.3"
CREATOR = "cubic"
STORAGE = "TASK.json"

# Import sys so that we can get command line arguments.
import sys

# Import time so we can get edit signatures
import time 

# Check the json exists
try:
    open(STORAGE, 'r').close()
except:
    open(STORAGE, 'w').write(" ")
        

# Choose which mode to
match sys.argv[1]:
    case "add":
        try:
            # Prepare the record's attributes
            json = open(STORAGE, 'r').readlines()
            id = str(len(json) - 1)
            epoch = str(int(time.time() * pow(10, 7)))
            createdAt = epoch
            updatedAt = epoch

            # Prepare the record
            record = " \""+ id +"\": {" + \
                     "\"desc\": \"" + sys.argv[2] + "\", " + \
                     "\"createdAt\": \"" + createdAt + "\", " + \
                     "\"updatedAt\": \"" + updatedAt + "\" " + \
                     "}\n"

            # Is this the first record
            if len(json) == 1:
                json = ["{\n", record, "}"]
            else:
                json = json[:-2] + [json[-2][:-1]+",\n", record, json[-1]]

            # Rewrite the record
            open(STORAGE, 'w').writelines(json)

        except KeyError:
            print("Add Error: Missing Description.")
            quit()

    case "update":
        pass
    case "delete":
        pass
    case "mark-in-progress":
        pass
    case "mark-done":
        pass
    case "list":
        pass
    case "version":
        pass
    case "help":
        pass
    case _:
        pass