# Released under MIT license
# See LICENSE for more information
import tkinter as tk
from tkinter import StringVar, Text

root = tk.Tk()
root.geometry("600x840")
root.title("Memory Module Description Maker")
root.resizable(False, False)
currentAlgorithmText = Text(root)

brandNameVar = StringVar(root)
icMfgVar = StringVar(root)
moduleFormatVar = StringVar(root)
icTypeVar = StringVar(root)
icVoltageVar = StringVar(root)
errorCorrectionVar = StringVar(root)
registerBufferMfgVar = StringVar(root)
moduleSizeVar = StringVar(root)
moduleRanksVar = StringVar(root)
deviceBitWidthVar = StringVar(root)
moduleBitWidthVar = StringVar(root)
allSpeedsVar = StringVar(root)
outputVar = StringVar(root)

showDictInfo = 0 # Set this to 1 to print information on the dictionaries below, may cause performance issues on some systems, FOR DEBUG PURPOSES
# Trademarks below are property of their respective owners
# OEM means that the IC manufacturer labels a module with their own ICs with the IC manufacturer's name and logo and is usually sold to a system manufacturer such as Dell or Lenovo
# Check if there is the IC manufacturer's label, some system builders label their modules for inventory managment. A common example is Hewlett Packard (HP).
brandName = {'Unknown','TM Technology (tmtech)','Catalyst/CSI','MemoryTen','Positivo BGH','ADATA','Antec','Apacer','Apotop','Avexir','Compustocx','Komputer Bay','EVGA','GALAX','GeIL','Gigabyte','Klevv','Lexar (Longsys, formerly Micron Technology)','FORSEE (Longsys)','Mushkin','OCZ (Toshiba, rarely uses Toshiba IC)','PanRam','Pareema','PNY Electronics','Pioneer','Silicon Power','Thermaltake','Timetec','Transcend','Wintec','Patriot Memory','Kingston Technology','G.Skill','Corsair','Team Group','OLOy','Gloway','Kingmax','Ramaxel','TwinMOS','Samsung (OEM)','Micron Technology (OEM)','SpecTek (OEM, Micron Technology)','Cruical (Micron Technology)','Ballistix (Micron Technology)','SK Hynix (OEM)','Hynix (OEM)','Hyundai (OEM)','Nanya Technology (OEM)','elixir (Nanya Technology)','Qimonda (OEM)','AENEON (Qimonda)','Elpida (OEM)','Infineon (OEM)','ProMOS Technologies (OEM)','Mosel Vitelic (OEM)','Vitelic (OEM)','Powerchip/PSC (OEM)','Winbond (OEM)', 'I\'M Intelligent Memory (OEM)','Vanguard International Semiconductor/VIS/TSMC (OEM)','LG Semiconductor (OEM)','Cypress Semiconductor (OEM)','Siemens (OEM)','Toshiba (OEM)','Hitachi (OEM)','Mitsubishi (OEM)','Texas Instruments/TI (OEM)'}
icMfg = {'Unknown','Samsung/SEC','Micron Technology','SpecTek (Micron Technology)','Hynix','SK hynix','Hyundai','Nanya Technology','Qimonda','Inotera Memories (joint venture of Nanya Technology and Qimonda)','Elpida','Infineon','ProMOS Technologies','Mosel Vitelic','Vitelic','Powerchip/PSC','Etron Technology','Winbond','ESMT/Elite MT','Alliance Semiconductor','ISSI','ChangXin Memory Technologies/CXMT','UniIC','Zentel','Mosel Vitelic','Vitelic','UMC','PieceMakers (Fabless)','I\'M Intelligent Memory (Fabless)','Utron Technology','OKI Electric Industry','Vanguard International Semiconductor/VIS/TSMC','Signetics','Fairchild','LG Semiconductor','Silicon Magic','Cypress Semiconductor','Siemens','Toshiba','Hitachi','Mitsubishi','Texas Instruments/TI','Nippon Electric Company/NEC', 'NPNX (Later Nippon Steel Semiconductor)'}
moduleFormat = {'Unknown','UDIMM','SODIMM','UniDIMM','RDIMM','LRDIMM','FBDIMM','RIMM','SORIMM','ISA Card','30-pin SIMM','72-pin SIMM','SIP','DIP'}
icType = {'Unknown','DDR','DDR2','DDR3','DDR3L','DDR3U','DDR3L/DDR4','DDR4','DDR5','SDRAM','DRAM','EDO DRAM','FPRAM'}
icVoltage = {'Unknown','3.3v','2.5v','2.6v','1.8v','1.5v','1.35v','1.2v','1.1v','1.05v'}
errorCorrection = {'Unknown','none/non-ECC','ECC','Parity','CRC', 'on-die ECC'}
registerBufferMfg = {'Unknown','N/A','Inphi','IDT','Intel','Rambus','Montage Technology','Renesas'}
moduleSize = {'Unknown','512KB','1MB','2MB','4MB','8MB','16MB','32MB','64MB','128MB','256MB','512MB','1GB','2GB','4GB','8GB','16GB','32GB','64GB','128GB'}
moduleRanks = {'Unknown','1R','2R','4R','8R'}
deviceBitWidth = {'Unknown','x4','x8','x16'}
moduleBitWidth = {'Unknown','8 bit','9 bit','32 bit','40 bit','64 bit','72 bit'}
allSpeeds = {''}
# All generations' speeds go into the same dictionary
allSpeeds.update({'Unknown'})
allSpeeds.update({'PC66','PC100','PC133'})
allSpeeds.update({'PC1600/200MHz','PC2100/266MHz','PC2700/333MHz','PC3200/400MHz'})
allSpeeds.update({'PC2-3200/400MHz','PC2-4300/533MHz','PC2-5300/667MHz','PC2-6400/800MHz','PC2-8500/1066MHz'})
allSpeeds.update({'PC3-6400/800MHz','PC3-8500/1066MHz','PC3-10600/1333MHz','PC3-12800/1600MHz','PC3-14900/1866MHz','PC3-17000/2133MHz'})
allSpeeds.update({'PC4-12800/1600MHz','PC4-14900/1866MHz','PC4-17000/2133MHz','PC4-19200/2400MHz','PC4-21300/2666MHz','PC4-23500/2933MHz','PC4-25600/3200MHz','PC4-40000/5000MHz'}) #last one is Corsair's Vengeance LPX overclocked set, chances of seeing that in real life is pretty slim...
allSpeeds.update({'PC5-38400/4800MHz','PC5-51200/6400MHz'})
if showDictInfo == 1: # See showDictInfo above
    print("==================================")
    print("Length of brandName: " + str(len(brandName)))
    print(brandName)
    print("==================================")
    print("Length of icMfg: " + str(len(icMfg)))
    print(icMfg)
    print("==================================")
    print("Length of moduleFormat: " + str(len(moduleFormat)))
    print(moduleFormat)
    print("==================================")
    print("Length of icType: " + str(len(icType)))
    print(icType)
    print("==================================")
    print("Length of icVoltage: " + str(len(icVoltage)))
    print(icVoltage)
    print("==================================")
    print("Length of errorCorrection: " + str(len(errorCorrection)))
    print(errorCorrection)
    print("==================================")
    print("Length of registerBufferMfg: " + str(len(registerBufferMfg)))
    print(registerBufferMfg)
    print("==================================")
    print("Length of moduleSize: " + str(len(moduleSize)))
    print(moduleSize)
    print("==================================")
    print("Length of deviceBitWidth: " + str(len(deviceBitWidth)))
    print(deviceBitWidth)
    print("==================================")
    print("Length of moduleBitWidth: " + str(len(moduleBitWidth)))
    print(moduleBitWidth)
    print("==================================")
    print("Length of allSpeeds: " + str(len(allSpeeds)))
    print(allSpeeds)

def generateDescription():
    output.delete('1.0', tk.END)
    print("Generating...")
    output.insert(tk.END, "Module Brand Name: " + brandNameVar.get() + "\n")
    output.insert(tk.END, "IC Manufacturer: " + icMfgVar.get() + "\n")
    output.insert(tk.END, "Module Format: " + moduleFormatVar.get() + "\n")
    output.insert(tk.END, "IC Type: " + icTypeVar.get() + "\n")
    output.insert(tk.END, "Voltage: " + icVoltageVar.get() + "\n")
    output.insert(tk.END, "Speed: " + allSpeedsVar.get() + "\n")
    output.insert(tk.END, "Error Correction: " + errorCorrectionVar.get() + "\n")
    output.insert(tk.END, "Register/Buffer Mfg: " + registerBufferMfgVar.get() + "\n")
    output.insert(tk.END, "Module Size: " + moduleSizeVar.get() + "\n")
    output.insert(tk.END, "Organization: " + moduleRanksVar.get() + deviceBitWidthVar.get() + "\n")
    output.insert(tk.END, "Module Total Bit Width: " + moduleBitWidthVar.get())
root.grid_columnconfigure(0, weight=1, uniform="column")
brandNameDropdown = tk.OptionMenu(root, brandNameVar, *brandName)
brandNameDropdown.grid(row=1, column=0, sticky='nesw', padx=5, pady=2.5)
brandNameVar.set("Module Brand Name")
icMfgDropdown = tk.OptionMenu(root, icMfgVar, *icMfg)
icMfgDropdown.grid(row=2, column=0, sticky='nesw', padx=5, pady=2.5)
icMfgVar.set("IC Mfg")
moduleFormatDropdown = tk.OptionMenu(root, moduleFormatVar, *moduleFormat)
moduleFormatDropdown.grid(row=3, column=0, sticky='nesw', padx=5, pady=2.5)
moduleFormatVar.set("Module Format")
icTypeDropdown = tk.OptionMenu(root, icTypeVar, *icType)
icTypeDropdown.grid(row=4, column=0, sticky='nesw', padx=5, pady=2.5)
icTypeVar.set("IC Type")
icVoltageDropdown = tk.OptionMenu(root, icVoltageVar, *icVoltage)
icVoltageDropdown.grid(row=5, column=0, sticky='nesw', padx=5, pady=2.5)
icVoltageVar.set("IC Voltage")
allSpeedsDropdown = tk.OptionMenu(root, allSpeedsVar, *allSpeeds)
allSpeedsDropdown.grid(row=6, column=0, sticky='nesw', padx=5, pady=2.5)
allSpeedsVar.set("Speed")
errorCorrectionDropdown = tk.OptionMenu(root, errorCorrectionVar, *errorCorrection)
errorCorrectionDropdown.grid(row=7, column=0, sticky='nesw', padx=5, pady=2.5)
errorCorrectionVar.set("Error Correction")
registerBufferMfgDropdown = tk.OptionMenu(root, registerBufferMfgVar, *registerBufferMfg)
registerBufferMfgDropdown.grid(row=8, column=0, sticky='nesw', padx=5, pady=2.5)
registerBufferMfgVar.set("Buffer IC Mfg")
moduleSizeDropdown = tk.OptionMenu(root, moduleSizeVar, *moduleSize)
moduleSizeDropdown.grid(row=9, sticky='nesw', padx=5, pady=2.5)
moduleSizeVar.set("Module Size")
moduleRanksDropdown = tk.OptionMenu(root, moduleRanksVar, *moduleRanks)
moduleRanksDropdown.grid(row=10, sticky='nesw', padx=5, pady=2.5)
moduleRanksVar.set("Amount of Ranks")
deviceBitWidthDropdown = tk.OptionMenu(root, deviceBitWidthVar, *deviceBitWidth)
deviceBitWidthDropdown.grid(row=11, sticky='nesw', padx=5, pady=2.5)
deviceBitWidthVar.set("Device Bit Width")
moduleBitWidthDropdown = tk.OptionMenu(root, moduleBitWidthVar, *moduleBitWidth)
moduleBitWidthDropdown.grid(row=12, sticky='nesw', padx=5, pady=2.5)
moduleBitWidthVar.set("Module Total Bit Width")
generateButton = tk.Button(root, text = "Generate Description         ", command = generateDescription)
generateButton.grid(row=13, sticky='nesw', padx=5, pady=2.5)
output = Text(root)
output.grid(row=14, sticky='nesw', padx=5, pady=2.5)

root.mainloop()
