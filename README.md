# MicroBioVision Software [READ ME CORRUPTED THIS IS AN OLD VERSION - Fix in progress]

> Note: This README is currently being revised. Some sections, particularly dependency lists, may be incomplete.


An adapted and extended version of the BioVision software originally developed by Leon Pastawa (scump1).
The software performs image-based analysis of microscope images for applied research in process engineering and cultivation technology, with a focus on pellet morphology.

## Overview

The current version of MicroBioVision provides tools for:
- Pellet size analysis from microscope images
- Automated image binarization and segmentation
- Extraction of morphological parameters
- Optional conversion from pixel-based measurements to micrometers for supported microscopes

The software is intended for scientific use and manual result verification.

## System Requirements
- Python 3.8 or higher
- A working pip installation
- Tested on Windows systems

## Required Python Packages

WARNING: These packages might not be the correct packages, they are named from memory.
Solution in the meanwhile: Try running the code and the error will tell what kind of package is not installed in the last sentence of the error message. Install these packages

The following Python packages must be installed before running the software:
- numpy
- opencv-python
- pandas
- matplotlib
- scikit-image
- scipy
- tkinter (usually included with standard Python installations)

## Installation

Verify Python and pip
```bash
python --version 
pip --version
```

Install required packages
```bash
pip install numpy
```
If multiple Python versions are installed, use:
```bash
python -m pip install numpy opencv-python pandas matplotlib scikit-image scipy
```

Warning: Sometimes the installiation got troubles and sometimes the solution is to reopen the program

## Usage

### Start

- Start the software.
- Click Project in the upper left corner.
- Select Image Analysis.
- Choose the desired algorithm.
    (Currently, only one algorithm is available.)

### Pellet Size – Microscope Image

- Select the images to be analysed using the upper right selection box.
- The software can reliably process up to 50 images per run.
- Exceeding this number may lead to memory-related errors.
- Restarting the software after each batch is recommended.

### Image Processing

- Images are automatically converted to a binary representation.
- The threshold is chosen automatically but can be adjusted manually.
- Binary images are displayed alongside numerical results for manual validation.

### Scaling and Units

- Pixel-to-micrometer conversion is available if the microscope magnification is provided.
- This feature currently only supports images acquired with the EVOS XL Core Imaging System.
- Results are always additionally provided in pixel units (indicated by [px]).
- For images acquired with other microscopes:
- Ignore micrometer values.
- Convert pixel-based values manually using the appropriate scale.

### Batch Settings

- To apply identical settings to all images, select:
    Apply Current Settings to All

### Analysis and Output

- Click Analyse to start the image analysis.
- Processing time depends on the number of selected images.
- Output includes:
    - Numerical result tables
    - Corresponding binary images for verification

### Saving and Exporting Data

- Data can be saved using Save and Export in the bottom corner.
- Saving does not occur automatically.
- The save function depends on the active view:
- Image view: saves all binary images as .png
- Result list view: saves all result tables as .csv
- Each save operation exports all images or all tables, respectively.

## Version Log

### Version 0.0.1

- Added selection of microscope magnification
- Automatic scale conversion for EVOS XL Core Imaging System images
- Pixel-based results available for manual unit conversion
- Images from other microscopes supported without scale conversion

### Version 0.0.2

- Additional morphological parameters implemented:
- Maximum Feret diameter (Feret_max)
- Real pellet perimeter
- Bug fixes
- Spell checking and text corrections