import sys
import json
import sqlite3

if len(sys.argv) != 3:
    print("You need two arguments to make this work.")
    print("Usage:\nconvertToDD32.py DIFFNAME.BinDiff MODULE.exe\n")
    print("DIFFNAME is the name of the BinDiff file, and MODULE.exe is the name of the exe to be used in x32dbg.")
    print("Note: do NOT give your clients the same module name, for example, naming different clients just \"roblox.exe\" will cause conflicts in the debugger.")
    exit()

jsonarray = {"labels": []}
moduleName = sys.argv[2]

connection_obj = sqlite3.connect(sys.argv[1])
cursor_obj = connection_obj.cursor()
statement = '''SELECT * FROM function;'''
cursor_obj.execute(statement)
output = cursor_obj.fetchall()
connection_obj.close()

for row in output:
    jsonarray["labels"].append({"module": f"{moduleName}",
                                "address": f"{hex(row[1]-4194304)}",
                                "manual": "true",
                                "text": f"{row[4]}"})

open("outdb.dd32", "w").write(json.dumps(jsonarray, sort_keys=True, indent=1))