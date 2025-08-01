TITLE = "TASK TRACKER"
VER = "v 0.0.2"
CREATOR = "cubic"

# Import sys so that we can get command line arguments.
import sys

# Choose which mode to
match sys.argv[1]:
    case "add":
        pass
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