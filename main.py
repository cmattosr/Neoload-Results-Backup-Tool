import os
import codecs
from shutil import make_archive
import shutil
from pathlib import Path
import tkinter as tk

#Backup folder in C: root directory will be created if it doesn´t exist, otherwise it won´t be created
try:
    Path("D:/Backup/").mkdir()
except:
    print("Folder was not created")

#initiating the results_folder variable
#save the folder containing the result files
result_folder = "D:/"

#Creating the user interface window
backup_app = tk.Tk()
backup_app.rowconfigure([0,1,2,3,4,5,6,7,8], weight=1)
backup_app.columnconfigure([0,1], weight=1)
backup_app.title("Neoload Result Backup Tool - Performance Testing Team")

label_explanation1 = tk.Label(text="This app will search for scenarios based on the scenario and project name informed.")
label_explanation1.grid(row=0, column=0, sticky="nsew", columnspan=2)

label_explanation2 = tk.Label(text="This app will create a zip file with the results for that Neoload execution.")
label_explanation2.grid(row=1, column=0, sticky="nsew", columnspan=2)

label_explanation3 = tk.Label(text="The search for the specific result will start in D:\ root folder.")
label_explanation3.grid(row=2, column=0, sticky="nsew", columnspan=2)

label_explanation4 = tk.Label(text="This application works with one result at a time.")
label_explanation4.grid(row=3, column=0, sticky="nsew", columnspan=2)

#label_explanation5 = tk.Label(text="The zip file will be created in the D:\Backup if you don´t inform a destination")
#label_explanation5.grid(row=4, column=0, sticky="nsew", columnspan=2)

label_input_scenario= tk.Label(text="Please inform the scenario name from Neoload execution you want to generate a zip file:")
label_input_scenario.grid(row=6, column=0, sticky="nse")

scenario_name_box = tk.Entry(width=50)
scenario_name_box.grid(row=6, column=1)

label_input_project= tk.Label(text="Please inform the project name from Neoload execution:")
label_input_project.grid(row=7, column=0, sticky="nse")

project_name_box = tk.Entry(width=50)
project_name_box.grid(row=7, column=1)

label_input_backup= tk.Label(text="Please inform the name of the zip file you want (without extension):")
label_input_backup.grid(row=8, column=0, sticky="nse")

backup_name_box = tk.Entry(width=50)
backup_name_box.grid(row=8, column=1)

def generate_backup_file():
    scenario_name = scenario_name_box.get()
    project_name = project_name_box.get()
    backup_name = backup_name_box.get()
    rootdir = 'D:/'
    #rootdir  = "C:/Users/Cesar_Mattos/Desktop/Python"
    for rootdir, dirs, files in os.walk(rootdir):
        for subdir in dirs:
            for file in files:
                if file == "index.html":
                    result_file = codecs.open(os.path.join(rootdir, file), "r", "utf-8")
                    result_file_lines = result_file.readlines()
                    for result_file_line in result_file_lines:
                        if (scenario_name in result_file_line) and (project_name in result_file_line):
                            #path = "C:/Backup"
                            path = "D:/Backup"
                            shutil.make_archive(os.path.join(path, backup_name), "zip", result_folder)
                            output = tk.Label(text=f"Completed: D:\Backup\{backup_name}.zip")
                            output.grid(row=10, column=0, columnspan=2)
                            #print(f"Completed: D:\Backup\{backup_name}.zip")
                            break
            result_folder = rootdir

button = tk.Button(text="Generate ZIP file", command=generate_backup_file)
button.grid(row=9, column=0, columnspan=2)

#scenario_name = "[TEM] Added Validations - 09:02 - 11 May 2021"
#scenario_name = str(input("Please inform the scenario name from Neoload execution you want to generate a zip file: "))
#backup_name = str(input("Please inform the name of the zip file you want (without extension): "))



backup_app.mainloop()
