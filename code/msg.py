"""
Module for class to contain display messeges.
"""
__author__ = "Mats LarseN"
__copyright__ = "Mats Larsen 2014"
__credits__ = ["Mats Larsen"]
__license__ = "GPLv3"
__maintainer__ = "Mats Larsen"
__email__ = "larsen.mats.87@gmail.com"
__status__ = "Development"
#-----------------------------------------------------
#Import
#-----------------------------------------------------
import traceback
import numpy as np
#--------------------------------------------------------------------
#CONSTANTS
#--------------------------------------------------------------------
LOG_LEVEL = 2 # Information level
LOG_ALWAYS = 3
FILE = 'msg'
CLASS = 'DisplayMsg'
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
        print(str(log_level) + ' : ' + FILE + '.py::' + traceback.extract_stack()[-2][2] + ' : ' + msg)

class DisplayMsg(object):
    """
    This class contains all meassesges for given system.
    """
    def __init__(self,name,log_level):
        """
        The constructor for the DisplayMsg.
        """
        self._name = name
        self._msg = [] # List containing all messages

        self._msg.append("The given mode was equal to the already operation mode.") #0

        self._msg.append("All diodes are not blocked. Meaning that the tube is free of plastic.")#1

        self._msg.append("The given operational mode is undefined acoording to the listed implemented methods. Please check the mode name and the desired implemented method for consistensis. The application will be shutted down now!!") #2
        self._msg.append(" is initilized and ready to be used!") #3
        self._msg.append("A detection event is succesfull added")#4
        self._msg.append("ErrorTyping : The arguments of the name is not a String, Please change it to a String!!")#5

        self._msg.append("Name Typing Error")#6
        self._msg.append("Type Typing Error")#7
        self._msg.append("ErrorTyping. The arguments of the type is defined, Please change it to a defined type!!")#8
        self._msg.append("ErrorTyping. The arguments of the log_level is undefined, Please change it to a integer!!")#9
        self._msg.append("Argument is not prensent in the method")#10
        self._msg.append("Forfill the non present argument in the method")#11 
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
        
