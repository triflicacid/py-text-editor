from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as msg
from tkinter import filedialog as filed
import os, datetime, re, importlib

# Highlighting information
from assets import styles
from assets import conf

def reload_styles():
    importlib.reload(styles)
def run_program():
    # Start in OS
    global FILE_OPEN, FILE_PATH
    if FILE_OPEN:
        type = get_file_type(FILE_PATH)
        if type == "py":
            contents = open(FILE_PATH, "r")
            exec(contents.read())
            contents.close()
        elif type == "html" or type == "htm" or type == "shtml" or type == "xml" or type == "php" or type == "css":
            os.system("start chrome \"file:///"+str(FILE_PATH)+"\"")
        elif type == "bat" or type == "cmd":
            os.system("start \"\" \""+str(FILE_PATH)+"\"")
        elif type == "vbs":
            os.system("WScript \""+str(FILE_PATH)+"\"")
        else:
            message("Unable to execute file", "#FF0000")
            msg.showerror(MSG_TITLE, "Unable to run file '"+str(FILE_PATH)+"':\n\tUnsupported file type")
            #os.system("start notepad \""+str(FILE_PATH)+"\"")
    else:
        msg.showerror(MSG_TITLE, "Cannot run file")
def get_file_type(path):
    try:
        parts = path.split(".")
        return parts[len(parts) - 1]
    except:
        pass
    
def get_date(visual=True):
    now = datetime.datetime.now()
    if visual:
        return str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"  "+str(now.hour)+":"+str(now.minute)+":"+str(now.second)
    else:
        return now

def message(txt, colour="#000000"):
    bar.configure(text=str(get_date(True))+" - "+str(txt), foreground=str(colour))
    return True

def close_editor(window):
    global FILE_OPEN, FILE_SAVED
    if msg.askyesno(MSG_TITLE, "Are you sure you want to quit RSC Text Editor?"):
        if (FILE_OPEN and FILE_SAVED == False):
            if msg.showwarning(MSG_TITLE, "You have a file with unsaved changes. Save changes before exiting?", type=msg.YESNO) == "no":
                window.destroy()
            else:
                save_file(window)
                close_editor(window)
        else:
            window.destroy()
    
# Display file in editor Text()
def display(path):
    try:
        file = open(path, "r")
        win.delete("1.0", END)
        win.insert(INSERT, file.read())
        file.close()
    except FileNotFoundError:
        msg.showerror(MSG_TITLE, "Could not locate file "+str(path))
    except UnicodeDecodeError:
        msg.showerror(MSG_TITLE, "Cannot decode file")
        close_file(root, True)
    except:
        msg.showerror(MSG_TITLE, "Something went wrong")

# Save file
def save_file(parent):
    global FILE_OPEN, FILE_SAVED, FILE_PATH, IS_CONTENT
    if FILE_OPEN == False and FILE_PATH == None:
        if IS_CONTENT:
            # A new file but with contents
            saveas(parent)
            return None
        else:
            msg.showerror(MSG_TITLE, "Cannot save empty and unnamed file")
            message("Unable to save null file", "#FF0000")
            return False
    try:
        new_contents = win.get("1.0", END)
        # Save file
        file = open(FILE_PATH, "w")
        file.write(new_contents)
        file.close()
        FILE_SAVED = True
        message("Saved file "+str(FILE_PATH), "#009000")
        parent.title(str(MSG_TITLE) + " - " + str(FILE_PATH))
    except FileNotFoundError:
        msg.showerror(MSG_TITLE, "File "+str(FILE_PATH)+" does not exist")
        message("File "+str(FILE_PATH)+" does not exist", "#FF0000")
    #except:
        #msg.showerror(MSG_TITLE, "Something went wrong")

# save as file
def saveas(parent, title="Save As", putContents=True):
    global FILE_OPEN, FILE_SAVED, FILE_PATH
    file = filed.asksaveasfile(mode="w", title=title)
    if file != None:
        content = str(win.get("1.0", END))
        # If no file open, put current contents into file
        if not FILE_OPEN or putContents:
            file.write(content)
        # If a file is open do not put contents
        FILE_OPEN = True
        FILE_PATH = file.name
        FILE_SAVED = True
        file.close()
        display(FILE_PATH)
        message("Saved file "+str(FILE_PATH), "#009000")
        parent.title(str(MSG_TITLE) + " - " + str(FILE_PATH))
        highlight(get_file_type(FILE_PATH))

# On key press on win -> mark fiel as unsaved to lates version
def mark_unsave(parent):
    global FILE_OPEN, FILE_SAVED, IS_CONTENT, IS_HIGHLIGHTING
    IS_CONTENT = True
    if FILE_OPEN:
        FILE_SAVED = False
        parent.title(str(MSG_TITLE) + " - " + str(FILE_PATH) + " - Unsaved")
    elif IS_CONTENT:
        parent.title(str(MSG_TITLE) + " - New File - Unsaved")
    if IS_HIGHLIGHTING:
        # Remove highlighting
        for tag in win.tag_names():
            win.tag_delete(tag)
        highlight(get_file_type(FILE_PATH))

# Open a file
def open_file(parent, sudo=False):
    global FILE_OPEN, FILE_SAVED, FILE_PATH
    if sudo == False:
        if FILE_OPEN == True and FILE_SAVED == False:
            if msg.showwarning(MSG_TITLE, "The current file is unsaved. Continue and loose changes?", type=msg.YESNO) == "yes":
                open_file(parent, True)
        else:
            open_file(parent, True)
    else:
        file = filed.askopenfile(parent=parent, mode="r", title="Open File")
        if file != None:
            FILE_OPEN = True
            FILE_PATH = file.name
            FILE_SAVED = True
            file.close()
            parent.title(str(MSG_TITLE) + " - " + str(FILE_PATH))
            message("Opened file "+str(FILE_PATH))
            display(FILE_PATH)
            # Syntax file
            if highlight(get_file_type(FILE_PATH)):
                pass

# Close a file
def close_file(parent, sudo=False):
    global FILE_OPEN, FILE_SAVED, FILE_PATH, IS_CONTENT, IS_HIGHLIGHTING
    win.delete("1.0", END)
    if sudo == False:
        if FILE_OPEN or IS_CONTENT:
            if FILE_SAVED == False:
                if msg.showwarning(MSG_TITLE, "The file is not saved. Continue and loose unsaved changes?", type=msg.YESNO) == "yes":
                    close_file(parent, True)
        else:
            message("No file to close")
    else:
        if FILE_OPEN:
            win.delete("1.0", END)
            message("Closed file "+str(FILE_PATH))
            FILE_OPEN = False
            FILE_SAVED = None
            FILE_PATH = None
            parent.title(MSG_TITLE)
            IS_CONTENT = False
            IS_HIGHLIGHTING = False

def new_file(parent):
    saveas(parent, "Create New", False)

def delete_file(parent):
    global FILE_OPEN, FILE_PATH, IS_CONTENT, IS_HIGHLIGHTING
    if FILE_OPEN:
        if msg.showwarning(MSG_TITLE, "Are you sure you want to delete "+str(FILE_PATH)+"?", type=msg.YESNO) == "yes":
            os.remove(FILE_PATH)
            message("Deleted "+str(FILE_PATH))
            win.delete("1.0", END)
            parent.title(MSG_TITLE)
            OPEN_FILE = False
            FILE_PATH = None
            FILE_SAVED = None
            IS_CONTENT = False
            IS_HIGHLIGHTING = False
    else:
        message("No file to delete")


def highlight(mode=None):
    if mode == None:
        return False
    try:
        if mode == "py":
            mode = "python"
        elif mode == "js":
            mode = "javascript"
        elif mode == "html" or mode == "htm" or mode == "shtml":
            mode = "html"
        elif mode == "bat" or mode == "cmd":
            mode = "batch"
        elif mode == "xml" or mode == "xsl":
            mode = "xml"
        __tmp__ = styles.STYLES[mode]
    except:
        return False

    global IS_HIGHLIGHTING, FONT_FAMILY, FONT_SIZE
    IS_HIGHLIGHTING = True
    # Get lines of thing
    all = win.get("1.0", END)
    lines = all.split("\n")

    line_number = 1
    # Loop through each line
    for line in lines:
        # Loop through each syntax
        for style in styles.STYLES[mode][0]:
            matches = re.finditer(re.compile(style[1], re.IGNORECASE), line)
            for match in matches:
                #print("Match with ", style[0], " ->", match)
                win.tag_add(style[0], str(line_number)+"."+str(match.start(0)), str(line_number)+"."+str(match.end(0)))
            stylelist = style[2].split(",")
            try:
                win.tag_configure(style[0], foreground=stylelist[0])
            except:
                pass
            try:
                win.tag_configure(style[0], background=stylelist[1])
            except:
                pass
            try:
                win.tag_configure(style[0], font=(FONT_FAMILY, FONT_SIZE, stylelist[2]))
            except:
                pass
        line_number += 1
    # Do global styles
    for style in styles.STYLES[mode][1]:
        matches = re.finditer(re.compile(style[1], re.IGNORECASE), line)
        for match in matches:
            #print("Match with ", style[0], " ->", match)
            win.tag_add(style[0], str(line_number)+"."+str(match.start(0)), str(line_number)+"."+str(match.end(0)))
        stylelist = style[2].split(",")
        try:
            win.tag_configure(style[0], foreground=stylelist[0])
        except:
            pass
        try:
            win.tag_configure(style[0], background=stylelist[1])
        except:
            pass
        try:
            win.tag_configure(style[0], font=(FONT_FAMILY, FONT_SIZE, stylelist[2]))
        except:
            pass
    return True
    
# Title for msg
MSG_TITLE = "RSC Text Editor"
# Is a file open?
FILE_OPEN = False
# File path of open file
FILE_PATH = None
# Is file saved?
FILE_SAVED = None
# Is there content in the win?
IS_CONTENT = False
# Are we highlighting?
IS_HIGHLIGHTING = False

#FONT_FAMILY = "Courier New"
#FONT_SIZE = 8

for key in conf.CONF:
    exec(str(key)+" = "+str(conf.CONF[key]))

root = Tk()
root.title(MSG_TITLE)

# ******************* Buttons ***************** #
# New file
Button(root, text="New", command=lambda: new_file(root)).grid(row=0, column=0, padx=5)
# Save file
Button(root, text="Save", command=lambda: save_file(root)).grid(row=0, column=1, padx=5)
# Save As file
Button(root, text="Save As", command=lambda: saveas(root)).grid(row=0, column=2, padx=5)
# Open file
Button(root, text="Open", command=lambda: open_file(root)).grid(row=0, column=3, padx=5)
# Close file
Button(root, text="Close", command=lambda: close_file(root)).grid(row=0, column=4, padx=5)
# Delete file
Button(root, text="Delete", command=lambda: delete_file(root)).grid(row=0, column=5, padx=5)
# Run file
Button(root, text="Run", command=run_program).grid(row=0, column=6, padx=5)


# File screen Text()
win = Text(root, width=150, height=45, font=(FONT_FAMILY, FONT_SIZE))
win.grid(row=5, column=0, columnspan=10)

# On any key press, make saved = false
win.bind("<Key>", lambda e: mark_unsave(root))

# Message bar
bar = Label(root, background="#DEDEDE", width=140, font=(FONT_FAMILY, FONT_SIZE))
bar.grid(row=20, column=0, columnspan=10)

root.bind("<Control-o>", lambda e: open_file(root))
root.bind("<Control-n>", lambda e: new_file(root))
root.bind("<Control-s>", lambda e: save_file(root))
root.bind("<Control-Shift-s>", lambda e: saveas(root))
root.bind("<Escape>", lambda e: close_file(root))
root.bind("<Control-e>", lambda e: close_editor(root))
root.bind("<Control-d>", lambda e: delete_file(root))
root.bind("<F5>", lambda e: run_program())
root.bind("<Control-r>", lambda e: reload_styles())

root.protocol("WM_DELETE_WINDOW", lambda: close_editor(root))

root.mainloop()






