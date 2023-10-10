
# ActiveFileAuditor

![Build Status](https://img.shields.io/badge/build-passing-green.svg) ![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

ActiveFileAuditor is a powerful Python tool designed to scan directories and detect potential duplicate files. By leveraging sophisticated algorithms, this tool assesses filename and size variations to deliver accurate results.

## Features

- **Filename Similarity Analysis:** Uses the `difflib` Python library to compute similarity ratios between filenames.
- **Size Variation Detection:** Compares file sizes and reports variations within a specified threshold.
- **CSV Reporting:** Generates a comprehensive CSV report listing potential duplicate files.

## Installation

```bash
git clone https://github.com/YourUsername/ActiveFileAuditor.git
cd ActiveFileAuditor
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Ensure to set the `ROOT_DIR` in `main.py` to the directory you wish to scan.

## Citation

If you use this tool in your project or research, please cite:

```
Peter Xu, ActiveFileAuditor, https://github.com/peterandu365/ActiveFileAuditor, 2023
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

