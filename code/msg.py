#--------------------------------------------------------------------
#Administration Details
#--------------------------------------------------------------------
__author__ = "Mats Larsen"
__copyright__ = "Mats Larsen 2014"
__credits__ = ["Mats Larsen"]
__license__ = "GPLv3"
__maintainer__ = "Mats Larsen"
__email__ = "larsen.mats.87@gmail.com"
__status__ = "Development"
__description__ = "Module is for displaying messeges. The Class should contain all the desired display messages. The idea is that it is typically the same messages there will be displayed. It should be understand as a fast phototyping of a appluication to display common messages."
__file__ = "msg.py"
__class__ ="DisplayMsg"
__dependencies__ = ["DisplayMsg"]
#--------------------------------------------------------------------
#Version
#--------------------------------------------------------------------
__version_stage__ = "Pre_alpha"
__version_number__ = "0.1"
__version_date__ = "20140917"
__version_risk__ = "This current version is in Pre-alpha version, which meaning that the program can crash or perform other unrespected behavoiurs."
__version_modification__ = "The development project has just been created."
__version_next_update__ = "Implementation of more messeages."
#--------------------------------------------------------------------
#Hardware
#--------------------------------------------------------------------
"""
This project is not releated to any kind of hardware, like GPIOs.
"""
#-----------------------------------------------------
#Import
#-----------------------------------------------------
import traceback
import os
#--------------------------------------------------------------------
#CONSTANTS
#--------------------------------------------------------------------
LOG_LEVEL = 2 # Information level
LOG_ALWAYS = 3 # Always log data
#--------------------------------------------------------------------
#METHODS
#-------------------------------------------------------------------
def log(msg, log_level=LOG_LEVEL):
    """
    Print a message, and track, where the log is invoked
    Input:
    -msg: message to be printed, ''
    -log_level: informationlevel, i
    """
    global LOG_LEVEL
    if log_level <= LOG_LEVEL:
        print(str(log_level) + ' : ' + __file__ + '.py::' + traceback.extract_stack()[-2][2] + ' : ' + msg)

class DisplayMsg(object):
    """
    This class contains all meassesges for given system.
    """
    def __init__(self,*args,**kwargs):
        """
        The constructor for the DisplayMsg.
        """
        #self._name = name # Name of the instance
        print(args)
        for a in args:
            print('here')
            print(a)
           
            
            if os.path.exists(a):   
                log('File exist')
                f = open(a,'r')
            else:
                log('Do not exist')
            #msg = f.readlines()
            
        #print(msg)
        self._msg = [] # List containing all messages

   
    def getMsg(self, index):
        """
        Return a messages given by the argument(index).
        """
        return  self._msg[index]
   
    def getName(self):
        """
        Returns the name of this intance.
        """
        return self._name
        
