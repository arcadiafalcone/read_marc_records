from pymarc import *
import sys

def myFileSelector():
    import os
    import Tkinter, tkFileDialog
    root = Tkinter.Tk()
    root.withdraw()
    fileselect = tkFileDialog.askopenfilename()
    open_file = os.path.abspath(fileselect)
    return open_file

marc_file = myFileSelector()

reader = MARCReader(file(marc_file), to_unicode=True)

for record in reader:
    for field in record.get_fields():
        if field.is_control_field():
            field.data = field.data.encode('utf-8')
        else:
            subfields_string = '%%%'.join(field.subfields)                
            new_subfields = subfields_string.encode('utf-8')
            field.subfields = new_subfields.split('%%%')
        print str(field)
    print 'View next record? Press Enter to proceed, or type "exit."'
    action = raw_input('--> ')
    if not action:
        continue
    elif action == 'exit':
        sys.exit()
    else:
        print 'That is not a valid command. Exiting now.'
        sys.exit()
