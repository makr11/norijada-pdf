# Norijada PDF

Norijada PDF is a Python library for generating PDF files from text files containing short text.


## Installation
Create virtual environment and install norijada-pdf

```bash
pip install norijada-pdf
```

## Usage

1. List available fonts

```bash
norijada-pdf list-fonts
```

2. Add new fonts

```bash
norijada-pdf add-fonts
```

Specify directory name other than fonts
```bash
norijada-pdf add-fonts --dir some_dir
```

3. Generate PDF

Settings will be automatically created in the current directory if it does not exist under settings.json file.

Example settings.json file

```json
{
    "font_sizes": {
        "Bangers-Regular": 195,
        "BebasNeue-Regular": 195,
        "BerkshireSwash-Regular": 158,
        "BlackOpsOne-Regular": 139,
        "Bungee-Regular": 120,
        "Courgette-Regular": 156,
        "Galindo-Regular": 140,
        "KaushanScript-Regular": 167,
        "LibreBaskerville-Regular": 140,
        "Lobster-Regular": 172,
        "MouseMemoirs-Regular": 223,
        "Pacifico-Regular": 147,
        "PatrickHand-Regular": 190,
        "Ranchers-Regular": 170,
        "RubikMonoOne-Regular": 100,
        "RussoOne-Regular": 140,
        "SigmarOne-Regular": 110,
        "Staatliches-Regular": 180,
        "TitanOne-Regular": 130
    },
    "plot_increment": 1,
    "page_width": 500,
    "default_font_size": 150,
    "max_length": 240
}
```

You can modify existing settings.json file or reset to defaults by running
```bash
norijada-pdf reset-settings
```

PDF generator requires an input.txt file in the current directory. 
Input file should contain nicknames separated by new line. Additional arguments can be passed to the generator.
Run help command to see all available arguments

```bash
norijada-pdf generate-pdf --help
```

Run the PDF generator with the following command

```bash
norijada-pdf generate-pdf --font BebasNeue-Regular.ttf
```

Add unique id to the end of the file name

```bash
norijada-pdf generate-pdf --font BebasNeue-Regular.ttf --file-id prhg-8a
```

Example input.txt file

```text
Netko Je Super Lik
??i??o
??tupid
??akra
jajoslav
Kico
Poki
??okac
??abo
jajan
Ko????ek
??upavac
Vau
Kora
??uro
Pero
Stavros
Jasmin Stavros
Jasmin
Kalodont
```

Example output pdf file
[nicknames-prhg-8a.pdf](example%2Fnicknames-prhg-8a.pdf)

Example output pdf file rotated [nicknames-prhg-8a-rotated.pdf](example%2Fnicknames-prhg-8a-rotated.pdf)
## License

[MIT](https://choosealicense.com/licenses/mit/)