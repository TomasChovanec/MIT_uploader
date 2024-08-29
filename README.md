Skript pro nahrání .hex souboru do výukového přípravku s procesorem ATMEGA2560 v předmětu Mikroprocesorová technika. Automaticky detekuje, na kterém COM portu je připjen přípravek a automaticky doplní cestu k hex filu. Programování pak probíhá jen jedním kliknutím.

**Použití:**
Uložte do počítače skript. Buď jako klasický python script, pak je ale potřeba doinstalovat potřebné knihovny. Preferované je použít exe verzi (složka executable), která má všechny knihovny zabalené u sebe.

V Atmel studiu zvolte *Custom programming tool*. Do položky command doplňte následující příkaz, ve kterém upravíte cestu ke skriptu.

```
"cesta_k_exe_souboru_MIT_uploader.exe" "$(OutputDirectory)\$(OutputFileName).hex"
```


![image](https://github.com/user-attachments/assets/86ea3461-14e2-417c-ba1c-0d9e7afb8de1)


Nahrání do desky se pak provede jedním tlačítkem  - *Start without debugging*. 

![image](https://github.com/user-attachments/assets/a7dce799-33f4-46e4-a138-5c5935524741)
