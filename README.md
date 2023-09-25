# GUIhelper

## Description

Python GUI app which in its current form allows recording of all pressed keys on the keyboard as well as mouse clicks (including coordinates) and sending them to MongoDB. Each session is stored as an individual collection. Application can also replay all the data by imitating inputs. End goal is to create an application that can help with creating user interfaces by allowing to record and replay user inputs. Such data can later be analyzed using different tools.

## Limitations

1. Currently replicating mouse movement is not possible, instead mouse is instantly moved to the coordinates where clicks happen.
2. Sets replay is slightly slower than the recording.

## Requirements

For requirements refer to requirements.txt.

## Starting application

Make sure to install required libraries from requirements.txt then run the command below in the directory:

```
python guihelper.py
```

## Listener

To access listener navigate the main GUI by pressing the "Listener" button.
By using buttons you can either start or stop recording inputs.
To stop the recording without clicking the button (as it records the button press) use the shortcut Left Alt+Esc+Z.

## Clicker

To access clicker navigate the main GUI by pressing the "Clicker" button.
By using buttons you can either start or stop playing inputs.
Before starting the clicker make sure to pick the proper set from the list on top.
If the set was recently recorded and does not appear on the list, press "Refresh List" button.
By choosing a set from the list and pressing "Delete Record" you can permanently delete the set from the database.
To stop the recording without clicking the button use the shortcut Left Alt+Esc+Z.
