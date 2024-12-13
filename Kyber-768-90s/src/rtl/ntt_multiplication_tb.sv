`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10.12.2024 21:57:35
// Design Name: 
// Module Name: ntt_multiplication_tb
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module ntt_multplication_tb;
    logic [15:0] f [255:0];
    logic [15:0] g [255:0];

    logic [15:0] zetas [127:0];
    logic [15:0] h [255:0];
    
    multiply_ntts uut (
        .f(f),
        .g(g),

        .zetas(zetas),
        .h(h)
    );

    initial begin
        $dumpfile("ntt_multiplication.vcd");
        $dumpvars(0, ntt_multplication_tb);
        
        f[0] = 245; f[1] = 1023; f[2] = 3100; f[3] = 201; f[4] = 2764; f[5] = 678; f[6] = 1455; f[7] = 2730;
        f[8] = 3072; f[9] = 160; f[10] = 1340; f[11] = 2220; f[12] = 2789; f[13] = 189; f[14] = 2556; f[15] = 1583;
        f[16] = 2598; f[17] = 173; f[18] = 1403; f[19] = 2984; f[20] = 1600; f[21] = 1814; f[22] = 2887; f[23] = 2054;
        f[24] = 920; f[25] = 2965; f[26] = 1594; f[27] = 1472; f[28] = 3302; f[29] = 482; f[30] = 935; f[31] = 3079;
        f[32] = 1165; f[33] = 2711; f[34] = 1153; f[35] = 2881; f[36] = 764; f[37] = 191; f[38] = 1763; f[39] = 3102;
        f[40] = 2165; f[41] = 1459; f[42] = 802; f[43] = 2279; f[44] = 1401; f[45] = 1500; f[46] = 293; f[47] = 2821;
        f[48] = 1925; f[49] = 1706; f[50] = 2890; f[51] = 1832; f[52] = 1603; f[53] = 987; f[54] = 1827; f[55] = 3218;
        f[56] = 249; f[57] = 2876; f[58] = 1107; f[59] = 2446; f[60] = 3013; f[61] = 140; f[62] = 1225; f[63] = 2740;
        f[64] = 1217; f[65] = 2098; f[66] = 1259; f[67] = 1228; f[68] = 2501; f[69] = 1581; f[70] = 1438; f[71] = 3086;
        f[72] = 1746; f[73] = 2941; f[74] = 3134; f[75] = 2543; f[76] = 2495; f[77] = 3190; f[78] = 1417; f[79] = 2583;
        f[80] = 1829; f[81] = 2760; f[82] = 2709; f[83] = 2273; f[84] = 2571; f[85] = 101; f[86] = 2479; f[87] = 2784;
        f[88] = 3178; f[89] = 1372; f[90] = 181; f[91] = 1109; f[92] = 2275; f[93] = 150; f[94] = 1873; f[95] = 2542;
        f[96] = 1047; f[97] = 2230; f[98] = 1664; f[99] = 2458; f[100] = 2888; f[101] = 1087; f[102] = 3113; f[103] = 1297;
        f[104] = 1565; f[105] = 2513; f[106] = 2686; f[107] = 1847; f[108] = 1645; f[109] = 2779; f[110] = 2552; f[111] = 3131;
        f[112] = 752; f[113] = 1824; f[114] = 3033; f[115] = 2184; f[116] = 2956; f[117] = 2673; f[118] = 2385; f[119] = 3193;
        f[120] = 1944; f[121] = 1638; f[122] = 2830; f[123] = 2395; f[124] = 1559; f[125] = 2920; f[126] = 1380; f[127] = 2263;
        f[128] = 1611; f[129] = 2910; f[130] = 3161; f[131] = 1681; f[132] = 2107; f[133] = 1299; f[134] = 1498; f[135] = 1702;
        f[136] = 2567; f[137] = 2398; f[138] = 1842; f[139] = 2974; f[140] = 1774; f[141] = 1118; f[142] = 2084; f[143] = 1199;
        f[144] = 1098; f[145] = 2377; f[146] = 2237; f[147] = 1875; f[148] = 2151; f[149] = 1042; f[150] = 2735; f[151] = 1592;
        f[152] = 1275; f[153] = 1926; f[154] = 2208; f[155] = 2381; f[156] = 3114; f[157] = 2143; f[158] = 2540; f[159] = 1182;
        f[160] = 2492; f[161] = 1896; f[162] = 1984; f[163] = 2050; f[164] = 1529; f[165] = 2426; f[166] = 1385; f[167] = 3048;
        f[168] = 1743; f[169] = 2641; f[170] = 1074; f[171] = 1150; f[172] = 1661; f[173] = 2754; f[174] = 2217; f[175] = 3018;
        f[176] = 2408; f[177] = 3320; f[178] = 1488; f[179] = 3014; f[180] = 2925; f[181] = 2467; f[182] = 2018; f[183] = 2875;
        f[184] = 3279; f[185] = 2339; f[186] = 2963; f[187] = 2785; f[188] = 2951; f[189] = 1690; f[190] = 2460; f[191] = 2011;
        f[192] = 2413; f[193] = 3246; f[194] = 3207; f[195] = 1073; f[196] = 1678; f[197] = 2175; f[198] = 3235; f[199] = 1343;
        f[200] = 2732; f[201] = 1682; f[202] = 2176; f[203] = 1860; f[204] = 3000; f[205] = 1405; f[206] = 2261; f[207] = 1138;
        f[208] = 1846; f[209] = 1569; f[210] = 3115; f[211] = 2517; f[212] = 1912; f[213] = 2794; f[214] = 2834; f[215] = 2494;
        f[216] = 1065; f[217] = 2878; f[218] = 2623; f[219] = 3286; f[220] = 2442; f[221] = 2922; f[222] = 1969; f[223] = 3225;
        f[224] = 1261; f[225] = 1049; f[226] = 2006; f[227] = 1737; f[228] = 1764; f[229] = 2913; f[230] = 2717; f[231] = 1481;
        f[232] = 2815; f[233] = 1330; f[234] = 2212; f[235] = 1768; f[236] = 2635; f[237] = 2898; f[238] = 3247; f[239] = 3200;
        f[240] = 1303; f[241] = 1208; f[242] = 2019; f[243] = 1667; f[244] = 1095; f[245] = 2869; f[246] = 3274; f[247] = 1810;
        f[248] = 2763; f[249] = 3067; f[250] = 2271; f[251] = 1772; f[252] = 1155; f[253] = 2109; f[254] = 2370; f[255] = 1780;

        g[0] = 1864; g[1] = 1825; g[2] = 1512; g[3] = 1255; g[4] = 2094; g[5] = 2921; g[6] = 142; g[7] = 2191;
        g[8] = 994; g[9] = 2510; g[10] = 104; g[11] = 1819; g[12] = 2311; g[13] = 1151; g[14] = 144; g[15] = 1430;
        g[16] = 2322; g[17] = 843; g[18] = 1872; g[19] = 2734; g[20] = 1621; g[21] = 823; g[22] = 243; g[23] = 2382;
        g[24] = 2998; g[25] = 2268; g[26] = 1582; g[27] = 2475; g[28] = 2238; g[29] = 2837; g[30] = 3119; g[31] = 2677;
        g[32] = 1699; g[33] = 2345; g[34] = 1157; g[35] = 2314; g[36] = 1376; g[37] = 1243; g[38] = 2194; g[39] = 1184;
        g[40] = 2756; g[41] = 2812; g[42] = 1156; g[43] = 3092; g[44] = 1462; g[45] = 289; g[46] = 121; g[47] = 2560;
        g[48] = 2489; g[49] = 1992; g[50] = 2153; g[51] = 2119; g[52] = 2067; g[53] = 1575; g[54] = 1753; g[55] = 1724;
        g[56] = 145; g[57] = 3328; g[58] = 2053; g[59] = 2702; g[60] = 1304; g[61] = 1812; g[62] = 2434; g[63] = 1560;
        g[64] = 3008; g[65] = 2179; g[66] = 1200; g[67] = 2293; g[68] = 1374; g[69] = 3215; g[70] = 1424; g[71] = 2380;
        g[72] = 2857; g[73] = 2978; g[74] = 2544; g[75] = 3255; g[76] = 3272; g[77] = 3228; g[78] = 280; g[79] = 1484;
        g[80] = 3037; g[81] = 1240; g[82] = 2483; g[83] = 2117; g[84] = 3214; g[85] = 2012; g[86] = 993; g[87] = 2374;
        g[88] = 2548; g[89] = 1192; g[90] = 2087; g[91] = 2557; g[92] = 1970; g[93] = 2298; g[94] = 3231; g[95] = 2566;
        g[96] = 2418; g[97] = 3004; g[98] = 2851; g[99] = 1541; g[100] = 1902; g[101] = 1473; g[102] = 3128; g[103] = 2214;
        g[104] = 3248; g[105] = 1833; g[106] = 2715; g[107] = 2297; g[108] = 2091; g[109] = 2781; g[110] = 1064; g[111] = 2134;
        g[112] = 1708; g[113] = 1876; g[114] = 1721; g[115] = 1178; g[116] = 1923; g[117] = 3262; g[118] = 2934; g[119] = 3199;
        g[120] = 1234; g[121] = 1963; g[122] = 1892; g[123] = 1469; g[124] = 1416; g[125] = 1714; g[126] = 2013; g[127] = 1904;
        g[128] = 1730; g[129] = 2171; g[130] = 2338; g[131] = 1328; g[132] = 1637; g[133] = 2223; g[134] = 1452; g[135] = 1517;
        g[136] = 1804; g[137] = 2116; g[138] = 1930; g[139] = 1627; g[140] = 1976; g[141] = 2225; g[142] = 1213; g[143] = 2294;
        g[144] = 2124; g[145] = 3001; g[146] = 1366; g[147] = 1644; g[148] = 2487; g[149] = 2997; g[150] = 3093; g[151] = 1878;
        g[152] = 3187; g[153] = 1307; g[154] = 2659; g[155] = 2266; g[156] = 1820; g[157] = 2511; g[158] = 1890; g[159] = 1249;
        g[160] = 2905; g[161] = 1784; g[162] = 2100; g[163] = 1289; g[164] = 1419; g[165] = 1392; g[166] = 2759; g[167] = 3201;
        g[168] = 2621; g[169] = 2838; g[170] = 1314; g[171] = 2584; g[172] = 1795; g[173] = 1410; g[174] = 2309; g[175] = 3034;
        g[176] = 2718; g[177] = 2420; g[178] = 2961; g[179] = 2631; g[180] = 2027; g[181] = 2696; g[182] = 1642; g[183] = 2822;
        g[184] = 3057; g[185] = 2681; g[186] = 2251; g[187] = 2539; g[188] = 2783; g[189] = 3010; g[190] = 1323; g[191] = 3111;
        g[192] = 1533; g[193] = 2112; g[194] = 1450; g[195] = 2274; g[196] = 2981; g[197] = 2957; g[198] = 2260; g[199] = 1674;
        g[200] = 1719; g[201] = 1356; g[202] = 2158; g[203] = 1683; g[204] = 1239; g[205] = 2336; g[206] = 1720; g[207] = 3085;
        g[208] = 2931; g[209] = 1412; g[210] = 1785; g[211] = 1769; g[212] = 3077; g[213] = 3202; g[214] = 3126; g[215] = 3260;
        g[216] = 2809; g[217] = 1906; g[218] = 3264; g[219] = 1983; g[220] = 1789; g[221] = 1620; g[222] = 2648; g[223] = 1718;
        g[224] = 1577; g[225] = 2918; g[226] = 1474; g[227] = 2186; g[228] = 1418; g[229] = 1127; g[230] = 2189; g[231] = 1198;
        g[232] = 1491; g[233] = 1365; g[234] = 2849; g[235] = 1841; g[236] = 1483; g[237] = 3069; g[238] = 2525; g[239] = 2456;
        g[240] = 2936; g[241] = 2017; g[242] = 3015; g[243] = 3174; g[244] = 2482; g[245] = 1518; g[246] = 2559; g[247] = 1741;
        g[248] = 2024; g[249] = 2422; g[250] = 3062; g[251] = 1168; g[252] = 2874; g[253] = 1388; g[254] = 1383; g[255] = 2747;

        zetas[0] = 17; zetas[1] = 2761; zetas[2] = 583; zetas[3] = 2649; zetas[4] = 1637; zetas[5] = 723; zetas[6] = 2288; zetas[7] = 1100;
        zetas[8] = 1409; zetas[9] = 2662; zetas[10] = 3281; zetas[11] = 233; zetas[12] = 756; zetas[13] = 2156; zetas[14] = 3015; zetas[15] = 3050;
        zetas[16] = 1703; zetas[17] = 1651; zetas[18] = 2789; zetas[19] = 1789; zetas[20] = 1847; zetas[21] = 952; zetas[22] = 1461; zetas[23] = 2687;
        zetas[24] = 939; zetas[25] = 2308; zetas[26] = 2437; zetas[27] = 2388; zetas[28] = 733; zetas[29] = 2337; zetas[30] = 268; zetas[31] = 641;
        zetas[32] = 1584; zetas[33] = 2298; zetas[34] = 2037; zetas[35] = 3220; zetas[36] = 375; zetas[37] = 2549; zetas[38] = 2090; zetas[39] = 1645;
        zetas[40] = 1063; zetas[41] = 319; zetas[42] = 2773; zetas[43] = 757; zetas[44] = 2099; zetas[45] = 561; zetas[46] = 2466; zetas[47] = 2594;
        zetas[48] = 2804; zetas[49] = 1092; zetas[50] = 403; zetas[51] = 1026; zetas[52] = 1143; zetas[53] = 2150; zetas[54] = 2775; zetas[55] = 886;
        zetas[56] = 1722; zetas[57] = 1212; zetas[58] = 1874; zetas[59] = 1029; zetas[60] = 2110; zetas[61] = 2935; zetas[62] = 885; zetas[63] = 2154;
        zetas[64] = 289; zetas[65] = 331; zetas[66] = 3253; zetas[67] = 1756; zetas[68] = 1197; zetas[69] = 2304; zetas[70] = 2277; zetas[71] = 2055;
        zetas[72] = 650; zetas[73] = 1977; zetas[74] = 2513; zetas[75] = 632; zetas[76] = 2865; zetas[77] = 33; zetas[78] = 1320; zetas[79] = 1915;
        zetas[80] = 2319; zetas[81] = 1435; zetas[82] = 807; zetas[83] = 452; zetas[84] = 1438; zetas[85] = 2868; zetas[86] = 1534; zetas[87] = 2402;
        zetas[88] = 2647; zetas[89] = 2617; zetas[90] = 1481; zetas[91] = 648; zetas[92] = 2474; zetas[93] = 3110; zetas[94] = 1227; zetas[95] = 910;
        zetas[96] = 296; zetas[97] = 2447; zetas[98] = 1339; zetas[99] = 1476; zetas[100] = 3046; zetas[101] = 56; zetas[102] = 2240; zetas[103] = 1333;
        zetas[104] = 1426; zetas[105] = 2094; zetas[106] = 535; zetas[107] = 2882; zetas[108] = 2393; zetas[109] = 2879; zetas[110] = 1974; zetas[111] = 821;
        zetas[112] = 1062; zetas[113] = 1919; zetas[114] = 193; zetas[115] = 797; zetas[116] = 2786; zetas[117] = 3260; zetas[118] = 569; zetas[119] = 1746;
        zetas[120] = 2642; zetas[121] = 630; zetas[122] = 1897; zetas[123] = 848; zetas[124] = 2580; zetas[125] = 3289; zetas[126] = 1729; zetas[127] = 3328;
 zetas[17] = 2637;

        #10;  
        $display("Resulting polynomial h:");
        for (int i = 0; i < 256; i++) begin
            $display("h[%0d] = %0d", i, h[i]);
        end

        $finish;
    end

endmodule