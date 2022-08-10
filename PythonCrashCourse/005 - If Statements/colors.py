### Colors ###

# This isn't part of the book exercises. I just felt it was time to make some
# of the output more colorful and wanted to get this in to the repo

# This will work in Windows Terminal, but not in Command Prompt. To enable
# it to work in Windows Command Prompt, we simply add the following registry
# key by opening a Command Prompt as Administrator and running the following:
#
# reg add HKEY_CURRENT_USER\Console /v VirtualTerminalLevel /t REG_DWORD /d 0x00000001 /f

# Note: If you want to revert the above registry modification to the original
# you can run the following:
#
# reg add HKEY_CURRENT_USER\Console /v VirtualTerminalLevel /t REG_DWORD /d 0x00000000 /f

# Declare a colors class (instead of making it colors, I'm calling it color so
# it will look better in the code

class color:
    WHITE = "\033[97m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    GREY = "\033[90m"
    SOFTWHITE = "\033[37m"
    SOFTCYAN = "\033[36m"
    SOFTMAGENTA = "\033[35m"
    SOFTBLUE = "\033[34m"
    SOFTYELLOW = "\033[33m"
    SOFTGREEN = "\033[32m"
    SOFTRED = "\033[31m"
    SOFTGREY = "\033[30m"
    DRACULA = "\033[38;5;52m"
    DRACULA2 = "\033[129;233;253m"
    BACKGROUNDD = "\033[40;42;54m"
    CURRENTLINED = "\033[68;71;90m"
    SELECTIOND = "\033[68;71;90m"
    FOREGROUNDD = "\033[248;248;242m"
    COMMENTD = "\033[98;114;164m"
    CYAND = "\033[129;233;253m"
    GREEND = "\033[80;250;123m"
    ORANGED = "\033[255;184;108m"
    PINKD = "\033[255;121;198m"
    PURPLED = "\033[189;147;249m"
    REDD = "\033[255;85;85m"
    YELLOWD = "\033[241;250;140m"
    ENDC = "\033[0m"
    AAA = "\033[38;5;0m"
    AAB = "\033[38;5;1m"
    AAC = "\033[38;5;2m"
    AAD = "\033[38;5;3m"
    AAE = "\033[38;5;4m"
    AAF = "\033[38;5;5m"
    AAG = "\033[38;5;6m"
    AAH = "\033[38;5;7m"
    AAI = "\033[38;5;8m"
    AAJ = "\033[38;5;9m"
    AAK = "\033[38;5;10m"
    AAL = "\033[38;5;11m"
    AAM = "\033[38;5;12m"
    AAN = "\033[38;5;13m"
    AAO = "\033[38;5;14m"
    AAP = "\033[38;5;15m"
    AAQ = "\033[38;5;16m"
    AAR = "\033[38;5;17m"
    AAS = "\033[38;5;18m"
    AAT = "\033[38;5;19m"
    AAU = "\033[38;5;20m"
    AAV = "\033[38;5;21m"
    AAW = "\033[38;5;22m"
    AAX = "\033[38;5;23m"
    AAY = "\033[38;5;24m"
    AAZ = "\033[38;5;25m"
    ABA = "\033[38;5;26m"
    ABB = "\033[38;5;27m"
    ABC = "\033[38;5;28m"
    ABD = "\033[38;5;29m"
    ABE = "\033[38;5;30m"
    ABF = "\033[38;5;31m"
    ABG = "\033[38;5;32m"
    ABH = "\033[38;5;33m"
    ABI = "\033[38;5;34m"
    ABJ = "\033[38;5;35m"
    ABK = "\033[38;5;36m"
    ABL = "\033[38;5;37m"
    ABM = "\033[38;5;38m"
    ABN = "\033[38;5;39m"
    ABO = "\033[38;5;40m"
    ABP = "\033[38;5;41m"
    ABQ = "\033[38;5;42m"
    ABR = "\033[38;5;43m"
    ABS = "\033[38;5;44m"
    ABT = "\033[38;5;45m"
    ABU = "\033[38;5;46m"
    ABV = "\033[38;5;47m"
    ABW = "\033[38;5;48m"
    ABX = "\033[38;5;49m"
    ABY = "\033[38;5;50m"
    ABZ = "\033[38;5;51m"
    ACA = "\033[38;5;52m"
    ACB = "\033[38;5;53m"
    ACC = "\033[38;5;54m"
    ACD = "\033[38;5;55m"
    ACE = "\033[38;5;56m"
    ACF = "\033[38;5;57m"
    ACG = "\033[38;5;58m"
    ACH = "\033[38;5;59m"
    ACI = "\033[38;5;60m"
    ACJ = "\033[38;5;61m"
    ACK = "\033[38;5;62m"
    ACL = "\033[38;5;63m"
    ACM = "\033[38;5;64m"
    ACN = "\033[38;5;65m"
    ACO = "\033[38;5;66m"
    ACP = "\033[38;5;67m"
    ACQ = "\033[38;5;68m"
    ACR = "\033[38;5;69m"
    ACS = "\033[38;5;70m"
    ACT = "\033[38;5;71m"
    ACU = "\033[38;5;72m"
    ACV = "\033[38;5;73m"
    ACW = "\033[38;5;74m"
    ACX = "\033[38;5;75m"
    ACY = "\033[38;5;76m"
    ACZ = "\033[38;5;77m"
    ADA = "\033[38;5;78m"
    ADB = "\033[38;5;79m"
    ADC = "\033[38;5;80m"
    ADD = "\033[38;5;81m"
    ADE = "\033[38;5;82m"
    ADF = "\033[38;5;83m"
    ADG = "\033[38;5;84m"
    ADH = "\033[38;5;85m"
    ADI = "\033[38;5;86m"
    ADJ = "\033[38;5;87m"
    ADK = "\033[38;5;88m"
    ADL = "\033[38;5;89m"
    ADM = "\033[38;5;90m"
    ADN = "\033[38;5;91m"
    ADO = "\033[38;5;92m"
    ADP = "\033[38;5;93m"
    ADQ = "\033[38;5;94m"
    ADR = "\033[38;5;95m"
    ADS = "\033[38;5;96m"
    ADT = "\033[38;5;97m"
    ADU = "\033[38;5;98m"
    ADV = "\033[38;5;99m"
    ADW = "\033[38;5;100m"
    ADX = "\033[38;5;101m"
    ADY = "\033[38;5;102m"
    ADZ = "\033[38;5;103m"
    AEA = "\033[38;5;104m"
    AEB = "\033[38;5;105m"
    AEC = "\033[38;5;106m"
    AED = "\033[38;5;107m"
    AEE = "\033[38;5;108m"
    AEF = "\033[38;5;109m"
    AEG = "\033[38;5;110m"
    AEH = "\033[38;5;111m"
    AEI = "\033[38;5;112m"
    AEJ = "\033[38;5;113m"
    AEK = "\033[38;5;114m"
    AEL = "\033[38;5;115m"
    AEM = "\033[38;5;116m"
    AEN = "\033[38;5;117m"
    AEO = "\033[38;5;118m"
    AEP = "\033[38;5;119m"
    AEQ = "\033[38;5;120m"
    AER = "\033[38;5;121m"
    AES = "\033[38;5;122m"
    AET = "\033[38;5;123m"
    AEU = "\033[38;5;124m"
    AEV = "\033[38;5;125m"
    AEW = "\033[38;5;126m"
    AEX = "\033[38;5;127m"
    AEY = "\033[38;5;128m"
    AEZ = "\033[38;5;129m"
    AFA = "\033[38;5;130m"
    AFB = "\033[38;5;131m"
    AFC = "\033[38;5;132m"
    AFD = "\033[38;5;133m"
    AFE = "\033[38;5;134m"
    AFF = "\033[38;5;135m"
    AFG = "\033[38;5;136m"
    AFH = "\033[38;5;137m"
    AFI = "\033[38;5;139m"
    AFJ = "\033[38;5;138m"
    AFK = "\033[38;5;140m"
    AFL = "\033[38;5;141m"
    AFM = "\033[38;5;142m"
    AFN = "\033[38;5;143m"
    AFO = "\033[38;5;144m"
    AFP = "\033[38;5;145m"
    AFQ = "\033[38;5;146m"
    AFR = "\033[38;5;147m"
    AFS = "\033[38;5;148m"
    AFT = "\033[38;5;149m"
    AFU = "\033[38;5;150m"
    AFV = "\033[38;5;151m"
    AFW = "\033[38;5;153m"
    AFX = "\033[38;5;152m"
    AFY = "\033[38;5;154m"
    AFZ = "\033[38;5;155m"
    AGA = "\033[38;5;156m"
    AGB = "\033[38;5;157m"
    AGC = "\033[38;5;158m"
    AGD = "\033[38;5;159m"
    AGE = "\033[38;5;160m"
    AGF = "\033[38;5;161m"
    AGG = "\033[38;5;162m"
    AGH = "\033[38;5;163m"
    AGI = "\033[38;5;164m"
    AGJ = "\033[38;5;165m"
    AGK = "\033[38;5;166m"
    AGL = "\033[38;5;167m"
    AGM = "\033[38;5;168m"
    AGN = "\033[38;5;169m"
    AGO = "\033[38;5;170m"
    AGP = "\033[38;5;171m"
    AGQ = "\033[38;5;172m"
    AGR = "\033[38;5;173m"
    AGS = "\033[38;5;174m"
    AGT = "\033[38;5;175m"
    AGU = "\033[38;5;176m"
    AGV = "\033[38;5;177m"
    AGW = "\033[38;5;179m"
    AGX = "\033[38;5;178m"
    AGY = "\033[38;5;180m"
    AGZ = "\033[38;5;181m"
    AHA = "\033[38;5;182m"
    AHB = "\033[38;5;183m"
    AHC = "\033[38;5;184m"
    AHD = "\033[38;5;185m"
    AHE = "\033[38;5;186m"
    AHF = "\033[38;5;187m"
    AHG = "\033[38;5;188m"
    AHH = "\033[38;5;189m"
    AHI = "\033[38;5;190m"
    AHJ = "\033[38;5;191m"
    AHK = "\033[38;5;192m"
    AHL = "\033[38;5;193m"
    AHM = "\033[38;5;194m"
    AHN = "\033[38;5;195m"
    AHO = "\033[38;5;196m"
    AHP = "\033[38;5;197m"
    AHQ = "\033[38;5;198m"
    AHR = "\033[38;5;199m"
    AHS = "\033[38;5;200m"
    AHT = "\033[38;5;201m"
    AHU = "\033[38;5;202m"
    AHV = "\033[38;5;203m"
    AHW = "\033[38;5;204m"
    AHX = "\033[38;5;205m"
    AHY = "\033[38;5;206m"
    AHZ = "\033[38;5;207m"
    AIA = "\033[38;5;208m"
    AIB = "\033[38;5;209m"
    AIC = "\033[38;5;210m"
    AID = "\033[38;5;211m"
    AIE = "\033[38;5;212m"
    AIF = "\033[38;5;213m"
    AIG = "\033[38;5;214m"
    AIH = "\033[38;5;215m"
    AII = "\033[38;5;216m"
    AIJ = "\033[38;5;217m"
    AIK = "\033[38;5;218m"
    AIL = "\033[38;5;219m"
    AIM = "\033[38;5;220m"
    AIN = "\033[38;5;221m"
    AIO = "\033[38;5;222m"
    AIP = "\033[38;5;223m"
    AIQ = "\033[38;5;224m"
    AIR = "\033[38;5;225m"
    AIS = "\033[38;5;226m"
    AIT = "\033[38;5;227m"
    AIU = "\033[38;5;228m"
    AIV = "\033[38;5;229m"
    AIW = "\033[38;5;230m"
    AIX = "\033[38;5;231m"
    AIY = "\033[38;5;232m"
    AIZ = "\033[38;5;233m"
    AJA = "\033[38;5;234m"
    AJB = "\033[38;5;235m"
    AJC = "\033[38;5;236m"
    AJD = "\033[38;5;237m"
    AJE = "\033[38;5;238m"
    AJF = "\033[38;5;239m"
    AJG = "\033[38;5;240m"
    AJH = "\033[38;5;241m"
    AJI = "\033[38;5;242m"
    AJJ = "\033[38;5;243m"
    AJK = "\033[38;5;244m"
    AJL = "\033[38;5;245m"
    AJM = "\033[38;5;246m"
    AJN = "\033[38;5;247m"
    AJO = "\033[38;5;248m"
    AJP = "\033[38;5;249m"
    AJQ = "\033[38;5;250m"
    AJR = "\033[38;5;251m"
    AJS = "\033[38;5;252m"
    AJT = "\033[38;5;253m"
    AJU = "\033[38;5;254m"
    AJV = "\033[38;5;255m"

print("\n")
print(color.ENDC + "-=-=- Basic Colors -=-=-")
print(color.WHITE + "This is white.")
print(color.CYAN + "This is cyan.")
print(color.MAGENTA + "This is magenta.")
print(color.BLUE + "This is blue.")
print(color.YELLOW + "This is yellow.")
print(color.GREEN + "This is green.")
print(color.RED + "This is red.")
print(color.GREY + "This is grey.")
print(color.SOFTWHITE + "This is soft white.")
print(color.SOFTCYAN + "This is soft cyan.")
print(color.SOFTMAGENTA + "This is soft magenta.")
print(color.SOFTBLUE + "This is soft blue.")
print(color.SOFTYELLOW + "This is soft yellow.")
print(color.SOFTGREEN + "This is soft green.")
print(color.SOFTRED + "This is soft red.")
print(color.SOFTGREY + "This is soft grey.")
print(color.ENDC + "This is ends color.")

print(color.ENDC + "-=-=- Block 1 -=-=-")
print(color.AAA + "Sheesh, man. That was a lot.")
print(color.AAB + "Sheesh, man. That was a lot.")
print(color.AAC + "Sheesh, man. That was a lot.")
print(color.AAD + "Sheesh, man. That was a lot.")
print(color.AAE + "Sheesh, man. That was a lot.")
print(color.AAF + "Sheesh, man. That was a lot.")
print(color.AAG + "Sheesh, man. That was a lot.")
print(color.AAH + "Sheesh, man. That was a lot.")
print(color.AAI + "Sheesh, man. That was a lot.")
print(color.AAJ + "Sheesh, man. That was a lot.")
print(color.AAK + "Sheesh, man. That was a lot.")
print(color.AAL + "Sheesh, man. That was a lot.")
print(color.AAM + "Sheesh, man. That was a lot.")
print(color.AAN + "Sheesh, man. That was a lot.")
print(color.AAO + "Sheesh, man. That was a lot.")
print(color.AAP + "Sheesh, man. That was a lot.")
print(color.AAQ + "Sheesh, man. That was a lot.")
print(color.AAR + "Sheesh, man. That was a lot.")
print(color.AAS + "Sheesh, man. That was a lot.")
print(color.AAT + "Sheesh, man. That was a lot.")
print(color.AAU + "Sheesh, man. That was a lot.")
print(color.AAV + "Sheesh, man. That was a lot.")
print(color.AAW + "Sheesh, man. That was a lot.")
print(color.AAX + "Sheesh, man. That was a lot.")
print(color.AAY + "Sheesh, man. That was a lot.")
print(color.AAZ + "Sheesh, man. That was a lot.")
print("\n")

print(color.ENDC + "-=-=- Block 2 -=-=-")
print(color.ABA + "Sheesh, man. That was a lot.")
print(color.ABB + "Sheesh, man. That was a lot.")
print(color.ABC + "Sheesh, man. That was a lot.")
print(color.ABD + "Sheesh, man. That was a lot.")
print(color.ABE + "Sheesh, man. That was a lot.")
print(color.ABF + "Sheesh, man. That was a lot.")
print(color.ABG + "Sheesh, man. That was a lot.")
print(color.ABH + "Sheesh, man. That was a lot.")
print(color.ABI + "Sheesh, man. That was a lot.")
print(color.ABJ + "Sheesh, man. That was a lot.")
print(color.ABK + "Sheesh, man. That was a lot.")
print(color.ABL + "Sheesh, man. That was a lot.")
print(color.ABM + "Sheesh, man. That was a lot.")
print(color.ABN + "Sheesh, man. That was a lot.")
print(color.ABO + "Sheesh, man. That was a lot.")
print(color.ABP + "Sheesh, man. That was a lot.")
print(color.ABQ + "Sheesh, man. That was a lot.")
print(color.ABR + "Sheesh, man. That was a lot.")
print(color.ABS + "Sheesh, man. That was a lot.")
print(color.ABT + "Sheesh, man. That was a lot.")
print(color.ABU + "Sheesh, man. That was a lot.")
print(color.ABV + "Sheesh, man. That was a lot.")
print(color.ABW + "Sheesh, man. That was a lot.")
print(color.ABX + "Sheesh, man. That was a lot.")
print(color.ABY + "Sheesh, man. That was a lot.")
print(color.ABZ + "Sheesh, man. That was a lot.")
print("\n")

print(color.ENDC + "-=-=- Block 3 -=-=-")
print(color.ACA + "Sheesh, man. That was a lot.")
print(color.ACB + "Sheesh, man. That was a lot.")
print(color.ACC + "Sheesh, man. That was a lot.")
print(color.ACD + "Sheesh, man. That was a lot.")
print(color.ACE + "Sheesh, man. That was a lot.")
print(color.ACF + "Sheesh, man. That was a lot.")
print(color.ACG + "Sheesh, man. That was a lot.")
print(color.ACH + "Sheesh, man. That was a lot.")
print(color.ACI + "Sheesh, man. That was a lot.")
print(color.ACJ + "Sheesh, man. That was a lot.")
print(color.ACK + "Sheesh, man. That was a lot.")
print(color.ACL + "Sheesh, man. That was a lot.")
print(color.ACM + "Sheesh, man. That was a lot.")
print(color.ACN + "Sheesh, man. That was a lot.")
print(color.ACO + "Sheesh, man. That was a lot.")
print(color.ACP + "Sheesh, man. That was a lot.")
print(color.ACQ + "Sheesh, man. That was a lot.")
print(color.ACR + "Sheesh, man. That was a lot.")
print(color.ACS + "Sheesh, man. That was a lot.")
print(color.ACT + "Sheesh, man. That was a lot.")
print(color.ACU + "Sheesh, man. That was a lot.")
print(color.ACV + "Sheesh, man. That was a lot.")
print(color.ACW + "Sheesh, man. That was a lot.")
print(color.ACX + "Sheesh, man. That was a lot.")
print(color.ACY + "Sheesh, man. That was a lot.")
print(color.ACZ + "Sheesh, man. That was a lot.")
print("\n")

print(color.ENDC + "-=-=- Block 4 -=-=-")
print(color.ADA + "Sheesh, man. That was a lot.")
print(color.ADB + "Sheesh, man. That was a lot.")
print(color.ADC + "Sheesh, man. That was a lot.")
print(color.ADD + "Sheesh, man. That was a lot.")
print(color.ADE + "Sheesh, man. That was a lot.")
print(color.ADF + "Sheesh, man. That was a lot.")
print(color.ADG + "Sheesh, man. That was a lot.")
print(color.ADH + "Sheesh, man. That was a lot.")
print(color.ADI + "Sheesh, man. That was a lot.")
print(color.ADJ + "Sheesh, man. That was a lot.")
print(color.ADK + "Sheesh, man. That was a lot.")
print(color.ADL + "Sheesh, man. That was a lot.")
print(color.ADM + "Sheesh, man. That was a lot.")
print(color.ADN + "Sheesh, man. That was a lot.")
print(color.ADO + "Sheesh, man. That was a lot.")
print(color.ADP + "Sheesh, man. That was a lot.")
print(color.ADQ + "Sheesh, man. That was a lot.")
print(color.ADR + "Sheesh, man. That was a lot.")
print(color.ADS + "Sheesh, man. That was a lot.")
print(color.ADT + "Sheesh, man. That was a lot.")
print(color.ADU + "Sheesh, man. That was a lot.")
print(color.ADV + "Sheesh, man. That was a lot.")
print(color.ADW + "Sheesh, man. That was a lot.")
print(color.ADX + "Sheesh, man. That was a lot.")
print(color.ADY + "Sheesh, man. That was a lot.")
print(color.ADZ + "Sheesh, man. That was a lot.")
print("\n")

print(color.ENDC + "-=-=- Block 5 -=-=-")
print(color.AEA + "Sheesh, man. That was a lot.")
print(color.AEB + "Sheesh, man. That was a lot.")
print(color.AEC + "Sheesh, man. That was a lot.")
print(color.AED + "Sheesh, man. That was a lot.")
print(color.AEE + "Sheesh, man. That was a lot.")
print(color.AEF + "Sheesh, man. That was a lot.")
print(color.AEG + "Sheesh, man. That was a lot.")
print(color.AEH + "Sheesh, man. That was a lot.")
print(color.AEI + "Sheesh, man. That was a lot.")
print(color.AEJ + "Sheesh, man. That was a lot.")
print(color.AEK + "Sheesh, man. That was a lot.")
print(color.AEL + "Sheesh, man. That was a lot.")
print(color.AEM + "Sheesh, man. That was a lot.")
print(color.AEN + "Sheesh, man. That was a lot.")
print(color.AEO + "Sheesh, man. That was a lot.")
print(color.AEP + "Sheesh, man. That was a lot.")
print(color.AEQ + "Sheesh, man. That was a lot.")
print(color.AER + "Sheesh, man. That was a lot.")
print(color.AES + "Sheesh, man. That was a lot.")
print(color.AET + "Sheesh, man. That was a lot.")
print(color.AEU + "Sheesh, man. That was a lot.")
print(color.AEV + "Sheesh, man. That was a lot.")
print(color.AEW + "Sheesh, man. That was a lot.")
print(color.AEX + "Sheesh, man. That was a lot.")
print(color.AEY + "Sheesh, man. That was a lot.")
print(color.AEZ + "Sheesh, man. That was a lot.")
print("\n")

print(color.ENDC + "-=-=- Block 6 -=-=-")
print(color.AFA + "Sheesh, man. That was a lot.")
print(color.AFB + "Sheesh, man. That was a lot.")
print(color.AFC + "Sheesh, man. That was a lot.")
print(color.AFD + "Sheesh, man. That was a lot.")
print(color.AFE + "Sheesh, man. That was a lot.")
print(color.AFF + "Sheesh, man. That was a lot.")
print(color.AFG + "Sheesh, man. That was a lot.")
print(color.AFH + "Sheesh, man. That was a lot.")
print(color.AFI + "Sheesh, man. That was a lot.")
print(color.AFJ + "Sheesh, man. That was a lot.")
print(color.AFK + "Sheesh, man. That was a lot.")
print(color.AFL + "Sheesh, man. That was a lot.")
print(color.AFM + "Sheesh, man. That was a lot.")
print(color.AFN + "Sheesh, man. That was a lot.")
print(color.AFO + "Sheesh, man. That was a lot.")
print(color.AFP + "Sheesh, man. That was a lot.")
print(color.AFQ + "Sheesh, man. That was a lot.")
print(color.AFR + "Sheesh, man. That was a lot.")
print(color.AFS + "Sheesh, man. That was a lot.")
print(color.AFT + "Sheesh, man. That was a lot.")
print(color.AFU + "Sheesh, man. That was a lot.")
print(color.AFV + "Sheesh, man. That was a lot.")
print(color.AFW + "Sheesh, man. That was a lot.")
print(color.AFX + "Sheesh, man. That was a lot.")
print(color.AFY + "Sheesh, man. That was a lot.")
print(color.AFZ + "Sheesh, man. That was a lot.")
print("\n")

print(color.ENDC + "-=-=- Block 7 -=-=-")
print(color.AGA + "Sheesh, man. That was a lot.")
print(color.AGB + "Sheesh, man. That was a lot.")
print(color.AGC + "Sheesh, man. That was a lot.")
print(color.AGD + "Sheesh, man. That was a lot.")
print(color.AGE + "Sheesh, man. That was a lot.")
print(color.AGF + "Sheesh, man. That was a lot.")
print(color.AGG + "Sheesh, man. That was a lot.")
print(color.AGH + "Sheesh, man. That was a lot.")
print(color.AGI + "Sheesh, man. That was a lot.")
print(color.AGJ + "Sheesh, man. That was a lot.")
print(color.AGK + "Sheesh, man. That was a lot.")
print(color.AGL + "Sheesh, man. That was a lot.")
print(color.AGM + "Sheesh, man. That was a lot.")
print(color.AGN + "Sheesh, man. That was a lot.")
print(color.AGO + "Sheesh, man. That was a lot.")
print(color.AGP + "Sheesh, man. That was a lot.")
print(color.AGQ + "Sheesh, man. That was a lot.")
print(color.AGR + "Sheesh, man. That was a lot.")
print(color.AGS + "Sheesh, man. That was a lot.")
print(color.AGT + "Sheesh, man. That was a lot.")
print(color.AGU + "Sheesh, man. That was a lot.")
print(color.AGV + "Sheesh, man. That was a lot.")
print(color.AGW + "Sheesh, man. That was a lot.")
print(color.AGX + "Sheesh, man. That was a lot.")
print(color.AGY + "Sheesh, man. That was a lot.")
print(color.AGZ + "Sheesh, man. That was a lot.")
print("\n")

print(color.ENDC + "-=-=- Block 8 -=-=-")
print(color.AHA + "Sheesh, man. That was a lot.")
print(color.AHB + "Sheesh, man. That was a lot.")
print(color.AHC + "Sheesh, man. That was a lot.")
print(color.AHD + "Sheesh, man. That was a lot.")
print(color.AHE + "Sheesh, man. That was a lot.")
print(color.AHF + "Sheesh, man. That was a lot.")
print(color.AHG + "Sheesh, man. That was a lot.")
print(color.AHH + "Sheesh, man. That was a lot.")
print(color.AHI + "Sheesh, man. That was a lot.")
print(color.AHJ + "Sheesh, man. That was a lot.")
print(color.AHK + "Sheesh, man. That was a lot.")
print(color.AHL + "Sheesh, man. That was a lot.")
print(color.AHM + "Sheesh, man. That was a lot.")
print(color.AHN + "Sheesh, man. That was a lot.")
print(color.AHO + "Sheesh, man. That was a lot.")
print(color.AHP + "Sheesh, man. That was a lot.")
print(color.AHQ + "Sheesh, man. That was a lot.")
print(color.AHR + "Sheesh, man. That was a lot.")
print(color.AHS + "Sheesh, man. That was a lot.")
print(color.AHT + "Sheesh, man. That was a lot.")
print(color.AHU + "Sheesh, man. That was a lot.")
print(color.AHV + "Sheesh, man. That was a lot.")
print(color.AHW + "Sheesh, man. That was a lot.")
print(color.AHX + "Sheesh, man. That was a lot.")
print(color.AHY + "Sheesh, man. That was a lot.")
print(color.AHZ + "Sheesh, man. That was a lot.")
print("\n")

print(color.ENDC + "-=-=- Block 9 -=-=-")
print(color.AIA + "Sheesh, man. That was a lot.")
print(color.AIB + "Sheesh, man. That was a lot.")
print(color.AIC + "Sheesh, man. That was a lot.")
print(color.AID + "Sheesh, man. That was a lot.")
print(color.AIE + "Sheesh, man. That was a lot.")
print(color.AIF + "Sheesh, man. That was a lot.")
print(color.AIG + "Sheesh, man. That was a lot.")
print(color.AIH + "Sheesh, man. That was a lot.")
print(color.AII + "Sheesh, man. That was a lot.")
print(color.AIJ + "Sheesh, man. That was a lot.")
print(color.AIK + "Sheesh, man. That was a lot.")
print(color.AIL + "Sheesh, man. That was a lot.")
print(color.AIM + "Sheesh, man. That was a lot.")
print(color.AIN + "Sheesh, man. That was a lot.")
print(color.AIO + "Sheesh, man. That was a lot.")
print(color.AIP + "Sheesh, man. That was a lot.")
print(color.AIQ + "Sheesh, man. That was a lot.")
print(color.AIR + "Sheesh, man. That was a lot.")
print(color.AIS + "Sheesh, man. That was a lot.")
print(color.AIT + "Sheesh, man. That was a lot.")
print(color.AIU + "Sheesh, man. That was a lot.")
print(color.AIV + "Sheesh, man. That was a lot.")
print(color.AIW + "Sheesh, man. That was a lot.")
print(color.AIX + "Sheesh, man. That was a lot.")
print(color.AIY + "Sheesh, man. That was a lot.")
print(color.AIZ + "Sheesh, man. That was a lot.")
print("\n")

print(color.ENDC + "-=-=- Block 10 -=-=-")
print(color.AJA + "Sheesh, man. That was a lot.")
print(color.AJB + "Sheesh, man. That was a lot.")
print(color.AJC + "Sheesh, man. That was a lot.")
print(color.AJD + "Sheesh, man. That was a lot.")
print(color.AJE + "Sheesh, man. That was a lot.")
print(color.AJF + "Sheesh, man. That was a lot.")
print(color.AJG + "Sheesh, man. That was a lot.")
print(color.AJH + "Sheesh, man. That was a lot.")
print(color.AJI + "Sheesh, man. That was a lot.")
print(color.AJJ + "Sheesh, man. That was a lot.")
print(color.AJK + "Sheesh, man. That was a lot.")
print(color.AJL + "Sheesh, man. That was a lot.")
print(color.AJM + "Sheesh, man. That was a lot.")
print(color.AJN + "Sheesh, man. That was a lot.")
print(color.AJO + "Sheesh, man. That was a lot.")
print(color.AJP + "Sheesh, man. That was a lot.")
print(color.AJQ + "Sheesh, man. That was a lot.")
print(color.AJR + "Sheesh, man. That was a lot.")
print(color.AJS + "Sheesh, man. That was a lot.")
print(color.AJT + "Sheesh, man. That was a lot.")
print(color.AJU + "Sheesh, man. That was a lot.")
print(color.AJV + "Sheesh, man. That was a lot.")
print("\n")

print(color.ENDC + "-=-=- Dracula Theme Attempt -=-=-")
print(color.ACH + "Background")
print(color.ADZ + "Current Line")
print(color.ADZ + "Selection")
print(color.AIX + "Foreground")
print(color.AEG + "Comment")
print(color.ADJ + "Cyan")
print(color.ADG + "Green")
print(color.AII + "Orange")
print(color.AIF + "Pink")
print(color.AIR + "Purple")
print(color.AHV + "Red")
print(color.AIW + "Yellow")
print(color.ENDC)
