import os
import time

username = "YOUR_USER_NAME"
document = open("/Users/"+username+"/Dropbox/kindle-clippings.txt","r") 
 
data = "".join(document.readlines())
notes = []
try:
    clippings = data.split('==========')
    for clip in clippings:
        clipping = clip.split('Added on ')

        title = clipping[0].split('\r\n- ')[0].replace('\r\n','')
        date = clipping[1].split('\r\n')[0]
        location = clipping[0].split('\r\n- ')[1].replace('\r\n','')
        text = clipping[1].split('\r\n\r\n')[1]
        note = {'title': title, 'date': date, 'location': location, 'text': text}
        notes.append(note)
        #print note
    
except:
    print 'Unable parse clipping'

def MakeEvernoteNote(note):
    cmd = '''
    osascript<<END
        tell application "Evernote"
            set note_title to "'''+ unicode(note['title'], errors="ignore") + '''"
            set note_contents to "''' + unicode(note['location'], errors="ignore") + unicode(note['date'], errors="ignore") + "\n" + unicode(note['text'], errors="ignore") + "\n" '''"
            set found_notes to find notes note_title
            set num_notes_found to count found_notes
            if num_notes_found is greater than 0 then
                set this_note to item 1 in found_notes
                tell this_note to append text note_contents
            else
                set clip to create note title note_title with text note_contents
                if (not (tag named "kindle-note" exists)) then
                    make tag with properties {name:"kindle-note"}
                end if
                assign tag "kindle-note" to clip
            end if
        end tell 
    END'''

    os.system(cmd)

for note in notes:
    time.sleep(1)
    MakeEvernoteNote(note)