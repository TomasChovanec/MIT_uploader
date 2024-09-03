# MIT uploader
Skript pro nahrání .hex souboru do výukového přípravku s procesorem ATMEGA2560 v předmětu Mikroprocesorová technika. Automaticky detekuje, na kterém COM portu je připojen přípravek a automaticky doplní cestu k hex souboru. Programování pak probíhá jen jedním kliknutím.

**Použití:**
Uložte do počítače skript. Buď jako klasický python script (.py), pak je ale potřeba doinstalovat potřebné knihovny. Preferované je použít exe verzi (složka executable), která má všechny knihovny zabalené u sebe.

V Microchip studiu zvolte *Custom programming tool*. Do položky command doplňte následující příkaz, ve kterém upravte **pouze cestu ke skriptu**. Cestu k hex souboru doplní Microchip studio automaticky pomocí použitých direktiv ```$(OutputDirectory)\$(OutputFileName)```.

```
"D:\Programy\MIT_uploader\MIT_uploader.exe" "$(OutputDirectory)\$(OutputFileName).hex"
```

![image](https://github.com/user-attachments/assets/ad273e6d-bd13-4120-8276-e0aacc4276ed)


Nahrání do desky se pak provede jedním tlačítkem  - *Start without debugging*. 

![image](https://github.com/user-attachments/assets/a7dce799-33f4-46e4-a138-5c5935524741)
