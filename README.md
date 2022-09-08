# UK Postcode Validation
a library that supports validating and formatting postcodes for the UK
The format is as follows, where A signifies a letter and 9 a digit:
Format 	Coverage 	Example
AA9A 9AA 	WC postcode area; EC1–EC4, NW1W, SE1P, SW1 	EC1A 1BB
A9A 9AA 	E1, N1, W1 	W1A 0AX
A9 9AA 	B, E, G, L, M, N, S, W 	M1 1AE
A99 9AA 	B33 8TH
AA9 9AA 	All other postcodes 	CR2 6XH
AA99 9AA 	DN55 1PT 

Notes:

    As all formats end with 9AA, the first part of a postcode can easily be extracted by ignoring the last three characters.
    Areas with only single-digit districts: BR, FY, HA, HD, HG, HR, HS, HX, JE, LD, SM, SR, WC, WN, ZE (although WC is always subdivided by a further letter, e.g. WC1A)
    Areas with only double-digit districts: AB, LL, SO
    Areas with a district '0' (zero): BL, BS, CM, CR, FY, HA, PR, SL, SS (BS is the only area to have both a district 0 and a district 10)
    The following central London single-digit districts have been further divided by inserting a letter after the digit and before the space: EC1–EC4 (but not EC50), SW1, W1, WC1, WC2 and parts of E1 (E1W), N1 (N1C and N1P), NW1 (NW1W) and SE1 (SE1P).
    The letters Q, V and X are not used in the first position.
    The letters I, J and Z are not used in the second position.
    The only letters to appear in the third position are A, B, C, D, E, F, G, H, J, K, P, S, T, U and W when the structure starts with A9A.
    The only letters to appear in the fourth position are A, B, E, H, M, N, P, R, V, W, X and Y when the structure starts with AA9A.
    The final two letters do not use C, I, K, M, O or V, so as not to resemble digits or each other when hand-written.
    Postcode sectors are one of ten digits: 0 to 9, with 0 only used once 9 has been used in a post town, save for Croydon and Newport
    
    
