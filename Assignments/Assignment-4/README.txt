CONTENTS OF FOLDER
    cfr_map.ipynb
    data_process.ipynb
    white_wash.ipynb
    README.txt
    Source_data_for_CFR_vaccine_map_abridged.csv
    
In cfr_map.ipynb
    size of disk is determined by
        (size of outbreak/size of largest outbreak)*5000
    
    The csv file ended up with 'unknown' in the 4th coloumn, populated otherwise by numbers
    Instead of working within the code, I manually set the unknown value to 0 (Which I thought made sense)
    
    In addition, when reading the data from the csv file, some of the lines aren't read in, and I have no idea why.
    
    
Notes on the assignment


This assignment was very time consuming! Working with the earthquake map was difficult because the example file wasn't commented well.
I spent a bunch of time trying to understand why my points of data were behind the earth.

With regards to the part of the assignment with the binary numbers, it is pretty much impossible to check if the data is being read incorrectly.