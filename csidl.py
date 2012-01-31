"""

        Print CSIDL Values for Windows

        CSIDL (constant special item ID list) values provide a unique system-independent
        way to identify special folders used frequently by applications, but which may not
        have the same name or location on any given system. For example, the system folder
        may be "C:\Windows" on one system and "C:\Winnt" on another. These constants are
        defined in Shlobj.h. A subset of them is also defined in Shfolder.h.

        Author: Simon Dawson
        Email: simon.dawson@sas.com

        Date: 8 February 2010
        
"""

import ctypes.wintypes

csidl={}
csidl["CSIDL_DESKTOP"]=0x0000
csidl["CSIDL_INTERNET"]=0x0001
csidl["CSIDL_PROGRAMS"]=0x0002
csidl["CSIDL_CONTROLS"]=0x0003
csidl["CSIDL_PRINTERS"]=0x0004
csidl["CSIDL_PERSONAL"]=0x0005
csidl["CSIDL_FAVORITES"]=0x0006
csidl["CSIDL_STARTUP"]=0x0007
csidl["CSIDL_RECENT"]=0x0008
csidl["CSIDL_SENDTO"]=0x0009
csidl["CSIDL_BITBUCKET"]=0x000a
csidl["CSIDL_STARTMENU"]=0x000b
csidl["CSIDL_MYDOCUMENTS"]=csidl["CSIDL_PERSONAL"]
csidl["CSIDL_MYMUSIC"]=0x000d
csidl["CSIDL_MYVIDEO"]=0x000e
csidl["CSIDL_DESKTOPDIRECTORY"]=0x0010
csidl["CSIDL_DRIVES"]=0x0011
csidl["CSIDL_NETWORK"]=0x0012
csidl["CSIDL_NETHOOD"]=0x0013
csidl["CSIDL_FONTS"]=0x0014
csidl["CSIDL_TEMPLATES"]=0x0015
csidl["CSIDL_COMMON_STARTMENU"]=0x0016
csidl["CSIDL_COMMON_PROGRAMS"]=0x0017
csidl["CSIDL_COMMON_STARTUP"]=0x0018
csidl["CSIDL_COMMON_DESKTOPDIRECTORY"]=0x0019
csidl["CSIDL_APPDATA"]=0x001a
csidl["CSIDL_PRINTHOOD"]=0x001b
csidl["CSIDL_LOCAL_APPDATA"]=0x001c
csidl["CSIDL_ALTSTARTUP"]=0x001d
csidl["CSIDL_COMMON_ALTSTARTUP"]=0x001e
csidl["CSIDL_COMMON_FAVORITES"]=0x001f
csidl["CSIDL_INTERNET_CACHE"]=0x0020
csidl["CSIDL_COOKIES"]=0x0021
csidl["CSIDL_HISTORY"]=0x0022
csidl["CSIDL_COMMON_APPDATA"]=0x0023
csidl["CSIDL_WINDOWS"]=0x0024
csidl["CSIDL_SYSTEM"]=0x0025
csidl["CSIDL_PROGRAM_FILES"]=0x0026
csidl["CSIDL_MYPICTURES"]=0x0027
csidl["CSIDL_PROFILE"]=0x0028
csidl["CSIDL_SYSTEMX86"]=0x0029
csidl["CSIDL_PROGRAM_FILESX86"]=0x002a
csidl["CSIDL_PROGRAM_FILES_COMMON"]=0x002b
csidl["CSIDL_PROGRAM_FILES_COMMONX86"]=0x002c
csidl["CSIDL_COMMON_TEMPLATES"]=0x002d
csidl["CSIDL_COMMON_DOCUMENTS"]=0x002e
csidl["CSIDL_COMMON_ADMINTOOLS"]=0x002f
csidl["CSIDL_ADMINTOOLS"]=0x0030
csidl["CSIDL_CONNECTIONS"]=0x0031
csidl["CSIDL_COMMON_MUSIC"]=0x0035
csidl["CSIDL_COMMON_PICTURES"]=0x0036
csidl["CSIDL_COMMON_VIDEO"]=0x0037
csidl["CSIDL_RESOURCES"]=0x0038
csidl["CSIDL_RESOURCES_LOCALIZED"]=0x0039
csidl["CSIDL_COMMON_OEM_LINKS"]=0x003a
csidl["CSIDL_CDBURN_AREA"]=0x003b
csidl["CSIDL_COMPUTERSNEARME"]=0x003d
csidl["CSIDL_PROFILES"]=0x003e
csidl["CSIDL_FOLDER_MASK"]=0x00ff
csidl["CSIDL_FLAG_PER_USER_INIT"]=0x0800
csidl["CSIDL_FLAG_NO_ALIAS"]=0x1000
csidl["CSIDL_FLAG_DONT_VERIFY"]=0x4000
csidl["CSIDL_FLAG_CREATE"]=0x8000

#csidl["CSIDL_FLAG_MASK"]=0xff00

SHGFP_TYPE_CURRENT= 0
for key in csidl.keys():	
	buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
	ctypes.windll.shell32.SHGetFolderPathW(0, csidl[key], 0, SHGFP_TYPE_CURRENT, buf)
	print key, "\t" ,buf.value

