# MicroBioVision Software

An altered version of the BioVision software by Leon Pastawa (scump1).
This software is using ImageAnalysis on microscope pictures for applied science in process engineering and cultivation technology.

## BEFORE USAGE:
    - This programm needs a minimum of several packages installed

    - Installing packages requires pip to be installed
        - This can be tested by entering 
        ""
        in the Terminal
    
    - To install packages enter
    "pip install (name of the needed package)"
    in the Terminal

    - List of the packages:
        - numpy
        - 

## How to use
    - First click on "project" in the upper left corner and choose "Image Analysis"
    - You could now choose the desired algorithm (In the current version only one is available)
    - Pellet Size - Microscope Image
        - Choose your to be analyses images when clicking on the upper right box with the three dots. The code can easily deal with up to 50 images. However, there is an upper limit and the code should be started new every time after analysing this amount or it will break due to a full cage. Restarting it is faster than letting it fail.
        - When analysing images, the image will be turned into a binary scale. The threshhold for that will decide the code automatically, but can be changed on the right hand side.
        - As a new feature, the code can directly translate the pixle scale of the images to micrometers. However, one must enter the chosen magnitude at the microscope. This does only work for images taken with the EVOS XL Core Imaging System. The result will also give out the values in pixel (see unit in []). If a different microscope was used, only use those results without the micrometer scale and translate it manually.
        - If the set up was changed and the same change should be applied to all images, choose "Apply Current Settings to All".
        - After clicking "Analyse" the code will need a bit of time to analyse the images depending on the amount of images.
        - Results will show the values and the binary images to reevaluate the data manually.
        - Data can be saved on the bottom corner under "Save and Export"
            This will not automatically save the result lists and binary images. Clicking the save button when looking at the images will only save the images and same for the result lists. Though it will each save all lists or all images. Images will be saved as .png and the lists as .csv

        

## Version Log

### Version 0.0.1:
    - Added function to choose magnitude. This correlates to the magnifying parameter at the chose microscope
        - As of yet only the package for the EVOS X. Automatically chosen when using "Pellet Size - Microscope Images" when choosing the Algorithm
    - Images from other Microscopes can be used. All data given in mym can be ignored. Data that is given in pixel has to used and translated to the desired measuring unit manually
    
### Version 0.0.2:
    - Further Parameter calculations added:
        - Fere_max
        - Real perimeter of pellets
    - Bug fixes
    - Spell checking



