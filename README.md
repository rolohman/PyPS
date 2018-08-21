# PyPS

The current workflow:
1. setup_PyPS.py sets everything up
2. makeGamma0.py does the gamma0, smart downlooking, and extra filtering
3. runSnaphu.py makes config files and runs snaphu with tiles in parallel 
4. refDef.py flattens/references each ifg to nondeforming area
5. invertRates.py simple lsq inversion of rates and geocodes with cm/yr output