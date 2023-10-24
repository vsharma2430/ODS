"""

CHECKS AND REMEDIES

//Pedestal Sizing wrt Bolt .
    0:Pass
    1:BOP fail
    2:Edge Dist fail
    3:Bolt falling
    4:Bolt size error

//SBC Check 
    0: Pass, (Width Increase Internal) 
    1: Foundation width Limit Reached =  Abort: ANALYSIS

//Moment Rf Check 
    0: Pass, 
    1: PtMax (4%) reached, Abort: THICKNESS increase., 
    2: Max possible R/f (Ex. 32@100) reached, Abort: THICKNESS increase.
    3: Thickness limit reached =  Abort: ANALYSIS

//Shear Rf Check. 
    0: Pass, 
    1: TvMax reached, Abort: THICKNESS increase., 
    2: Tc excceed at max possible R/f, Abort: THICKNESS increase.
    3: Thickness limit reached =  Abort: ANALYSIS

//Pedestal R/f Check
    0: Pass.
    1: Column Max R/f (4%) Failed. Increase pedestal width.
    2: Column R/f Placement Failed. Enable Higher diameter bars: Abort: ANALYSIS

 Load Combinations inbuilt (Foundation design)
        1. Operating                                                            
        2. Operating  + Wind 
        3. Empty  + Wind 
        4. Empty  + Service Wind 
        5. Operating  + Seismic DBE 
        6. Operating  + Seismic MCE 


/*
 * ERROR - REMEDY
 * 
 * 0. CHECK SUCCESSFUL
 * 1. PEDESTAL SIZE : BOLTS -    PEDESTAL WIDTH INCREASE
 * 2. FOOTING SIZE -             FOOTING WIDTH INCREASE
 * 3. R/F MOMENT -               FOOTING THK INCREASE
 * 4. R/F SHEAR -                FOOTING THK INCREASE
 * 5. PUNCHING TEST -            FOOTING THK INCREASE
 * 6. PEDESTAL SIZE : STRENGTH - PEDESTAL WIDTH INCREASE
 * 
 */

"""