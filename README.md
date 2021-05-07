
# Pythons and Dragons Pyinstaller evasion tool

## Project Description 
[This project is the PoC of On Python and Malware: Developing Stealth and Evasive Malware Without Obfuscation.](https://arxiv.org/abs/2105.00565)

### Requirements
```python
python3 -m pip install -r requirements.txt
```

## PnD script

### Decscription 
This script downloads and customize pyinstaller as the paper describes to make it stealth.

### Run 
```python
python3 PnD.py 
or 
python3 PnD.py -s your_signature_string
 ```

## Generate script

### Description
This script generates an executable for the given string using the customized pyinstaller.
### Run
```python
python3 generate.py your_script.py
```

## PEtools

### Descriptions 
[PEtools](https://github.com/petoolse/petools) is a portable executable (PE) manipulation toolkit. 
With this tool we will manipulate the executable to make it stealthier and bypass static analysis. 

### Usage 
After running the generate.py script, the PEtools will be initialized and your exe will be loaded. 

Then you need to follow these steps: 
 
 

 1. Click View Rich Button, a window will prompt then click Clear Sign Button and finally close the window
 2. Click the Sections Button, a window will prompt then right click _RDATA section, Press Edit and rename the section to .bss. Finally press close 
 3. Lastly click the Optional Header Button, a window will prompt then click the questionmark (?) button besides to Checksum, press ok and close the PEtools.

Your executable now should be stealth.
