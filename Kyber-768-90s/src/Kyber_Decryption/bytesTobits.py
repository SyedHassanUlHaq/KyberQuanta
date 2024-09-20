def bytes_to_bits(byte_array: bytes) -> list[int]:
    """
    Takes a list of bytes as a parameter.
    Returns a list of integers where each item is 1 or 0.
    `len(return_list) == 8 * len(input_list)`
    """
    result = []
    for byte in byte_array:
        string = f"{byte:08b}"
        result += [int(x) for x in string]
    assert len(result) == 8 * len(byte_array)
    return result

# Provided byte array
input_bytes =  b'\x9b[H\xe8e\xfb\x08Re\xf1\xab\xe7\xf3v\xbd\x83\xca\xb6\x02\xf3\xbc\x9b\x19\xe7r\xde>?\xc1\x90R\xf7\x12\x18\xc8\x1f;p\xa4\x02\xf8\x17\x87\xe3B\n\xc5X\x05,\xc3a\xef\xed_\xb9`\xbb\xa5O\xee\x89\xb8\xbc\xa6\x8do\xa3fN\xde}\xb7\x1b\x04\xf4\x9b\x05\xd5\x04\xcc>\xb9H\x7f&\xfb\xac\x9d\xbc\xaf\xb3\x9c\xf1\x17\x11\x9a\xfb\xd1\x9dh?\x80U\x1au\x88\xc3\xceZ\xf0\xc8\x85\xca\x85\x1a\x127v\x8b\x00\x85=\x16\xc1\xa4\xb8kj\xea\x07\xe4\xc5\x98\x9b\xdd\xd8,N\x8f\xaa3^|\x85\x8f\x88;$\x88w\xaaN\x7f\xa4\xed\xe4\xb4q\x06\xa9\x9c\xbd(kwf\x9f\xbeYoV\xc95\xa1\\\xc5\xd8(o\xff\x9c\x04G\x85\xbcw\xa5\x8e\xa1\xfa\xbe\xdcF\xfe\t"\xe8\x040*Ow\xb8\x8et\x8c\xec\xed4\xce\xd0<\xb1\xc3\x9f\xb4\xab\xbe9\xee=h\x121s\xcc\x05\xe9\x107E\x91\xb2\xfe\x84{\x1f\xf7<\xdd#5\xc3p\xebo\x8bI\x82!\xc4\xf8P\xe5/\xac#\xea\x92O@\xea\xc4\x88 \xd4\x88O\x89F\x87m\xc6CW\xd3Jj\x01\x02\xcc\xc6\r\x13\x01\x10\xbd\x7f\xa5\x8esgp\xef\x97o,:\xaf?\x98\xcb>K\xb0Y%E\xde\x82<\x88\xdcZ\xae\xb1L\xf0\x13y1Z\x0bSv\x88\xd2p.\xe5w\xfd\xb4\xeb\x89\x15\xac\x9d\xf1\x91\x11\xd3\xd2\xd0v\x8e\xd4\x1cnE\xa0\x16\xdf\xb7r\\u\\\xc6\xe1y\x07\xb5\xc3\xc4":\x0e\x801\x03\xe9J\xe8\xdc\xe9\xfes\x82\x01k\xb1\xc3ge\xfc\xe8v^\x07\xd8s\x0e\x01{B\x1c\xf7\xe3w-\'~\x80\x9dc$\xb0g\x9c\x06y/Y\xa5\xf2&N#\xa2\xfcV\rsv\x18\x11\xff\x96\x821\xd5\x18\xf4\x01\xdcX\xa1\xc0\xfb\xe3\x92\xcf\xcdA6M\xcc-\x98\x8a\x02\xfe\xcciw\xb9\x85\x82\x86\x1c\x18\xafl\x9d7\x19\xfc\xad]\x8a\xde\xda\x1d\x0f\xe7\xf3\xb0\xf9\xedZ%Y\x0f\x8e\'P\x8c6!\xcf\xc6\xa6\x94\xec\xa8\xf4\xeb\x884Dq\x99\xb3?\xb5(&\xad\xd3?B\x0b\x04\xa2\xddp\x0eZ\xb5\r\x10\xc9\x04"\xc0G\x91w\x89\x11\xc5\x123\xb9<\xbd\x1fGbM\xe5\xcc0\x7fKVB\xb6\x18\xf6\xa6\x87\x19\x1a\x11\'^\x8c\xae`l\xa2p3\xef\x1f\xd4;F\xa7\xef\xe6+\x0f\x16=\xcb\xe6\xe7\xd81\xef\xe0\x9a\xdaR>\xdd\x8c\xfb\x15s8\x05\x96H\xb7\x94<\x15\x93U\xcf\xaf\xd2\xd6\xf8\x8e\xe5s\xc4[\xccU\xd7\'i\xfc3\xba\xe8\x1e\xf3\n\x82ji\xbd\x94\x82|6\x95\xd9Gg\xb4*o\xb9\xcd\x0b\xae\xc8?`\xf9u\x12h\xb4\x97\xc4\x19\x03\xd0\x8f\x16\xd1\x93\xdd\xa5\xe7\x87m\x7f|g\xa3\x17\xcb\xa0\xff\x16\xd5\xa3\x97\xee\xe9\xdaU=\x00\xae1(\xe0\xc2E\x9dr\xe2P5a\x04\xf1\x17M\xfd\x99Dg\xb9R\xdc\xc2\\\xe3\x18\xb4B\n\x97\xe9y\xc3u3\xbe\x97\xa5\xb8\x86\x1f\xa8{\x00\x97\x1c\xaa{h\xa1x\x1d\x83\x8a\x89\x85\x1b\xf9J\xe77Y\xd2\xbf=\xca!"\xbd\xda9^\xf3E\xc6\xa09\xc7^[\xbfj\x91`\x18-t\xe9o\xfb\xad\xccy3\r\xd3]\xc0H\xde\x04{\x12>\xff\xbey\x94\x81\xa7\x99\x8b\xd4rS\x07]@]\xb6\x9aE\x05\x1d#V\x93A\xbeLg\xd9Oj\t\x05B\xb8,tk\xe2\xb2`\xf5\xd9E\xf4\xab\xa1\x1f=\x84i\x8b(\xd5\x0c\xc5\x08\xbf\xc4\xd9z2\xd7\xed\x84x6\xe5A,\x93\x0c\x08\x8e4\xe8Az\xe6\xf4\x87\xbb\x95\xfd`F.\xa7\xa6c\x8f5\xfc<W\xf5\x9ac\x11\x07\xf5K\x05\xa4\xe6-\xd0\xbc\xad\x18o\xf1\x98\xa4\xbfx\xb53\xf8B\xe5{\xef\x14\xd0\x82\xb6\xa8\xceV\x01\xc9\x00\x8f\xf2{?_\xdf\xe5uU\x9c\xf1\x17\xcd\x87\x05q\x19\xfa\x05\xee\xc6\x9a7\xbd\xf1\x1f\xc1\x1b\xe4_\xc1\xdd\xd9\x1d?9k\xa7\xa5\xb5\xd1S\xdd\x92&Lk\x1b*c\xcb]f3t\x9e\x9b\x8e\xdd\xe0\xa0\xf3\xc1\xfc\xe6W\x1d\xa0\xf9\x02\x8b\xe6,J\xb3\x16\xa0"\xc2S\x1e\x83\x13\xa9GY9&\xb3\xfe\x9e\x91\xa7\xfc8w\xfa"A\xbb-\x81\xe3\x81\xd6\x0b\xe8V\xde@O\xad\x1f\x9a\xdf5\xf7\xe3\xb2\x9bp\xce\xa9\xc7\xb2Jx\xb8\xba\x03%x\x16!-\xa1\x80f\x18\xa2C\x8f\x98kO\xff\xa4@\xdeS\x14\x1d\x98\xb0Gm\x11\xcb\xbe\xdfe\x83\xe8fZ\x11]\'\x9d\x19\xe3\xeb\xbb\xd8\x07\x10}\xb2\x9b\xa1\x90_\x8f\x12\x9ekMwU\x11\x8aT=o\xdf\xbbW\x8fd\x86O\xa4\xdd\n" wL,\xd2\x84x\xf3r\xcd\xa4~\xf4\xa4\t\x190s\xf4\xa7\xf0\xb5\xb4m\\\xb7\xd7\xa2\xf3>\x05\xc66\x10\x83^\xe1\x1f5\xdcX\x9c\xe3\xa0o\xebG\xf8\x19]\xcdd\x8cy\x0c\xcb\xda\x96\x8f\xefv\x0b\x0cg6]\xc7\x15\x19*.#wn\x07~\xc2\x02\xd06\xa1\xae\x84\x9e\x8c\xfbH\xd2\x87\xb2vy\\\xaf\xa5\x87l\xf9\x04\xbd-%\x16\xecK \xba\xd2\xe2\x0c\x0b;\xd6\xd02\x0e\xa7 \xce-\xe1Q\xb9hT\\uSH_z,\x06\x9f\xf4&\x96\xee\xa2l\x0bRR\xba)\x85\xbc\x95\xf5\xc8\x1cb@\xf2\xbcX(\x82\x1dV\xc8\xbc\xa5>\x1a\xcbv\xd1\x8cGyt\x0e\x8d\xd8g\xdc\xf0\x14\xdc\x97.$|lC1\xf4\x11G|Gmp\xb1k\xff\xd1\x1a\x84+]5]t.\x96\xfc\xb8\x9d\xc7\x1a9GJ\x85\x04\x96\x9a\xd4\x16\xffc\xbb\xe7\xbc\r%\nB$\xb7=J\xac\xfa\xa6\x80\xfd#\x8e7i~(bk\xc8\x8a-\xfd\xac\xda\xb7\x84cm\xb3\xaf\xcaR6j\x86\x8b\xa3U\xa8\x95\xd3\xe2\x84n\xa5\xd2)\xe6\xfa\x92\xcd\x88\x89\xdee\t\x04\x89\x18\t\xe1\xc7\n\xc7\xb2\xab\xb9\xc2x\x10Z\xff\xedW\xe3\xf3\xbaz>a\x06\xef\x82\x99zj\xf0p\x9e"A\x1a\xff4(b\xfd1M\xff\xba6\xea\x81T\xe7tw\xe5\x8b\xab\x82\xd9\x03\xb6\xfaDT3\xb7\xd2\x1eJ_n\xacNg|\xc3\xc9\x0e\xb1\x85T\xd9\x89w\xb8\x80Fh\x17&\xb0\xf2z\x98|\xc96v\xd6\x18\x1aw\xcb)\x7f\xa1\x86\xb0\x9e\xaa\xb4K\x95\x99\xce\x92\x02\xa9Q\xbc\x00\xd5\xf2\xaf\x1f \x02\xe1\x8c\x1aH}\xeb\x14V$!\x10*\x0b;wa\xc0!zn"\xa0H\\\x85O(\xa4P\x92\xda\xb1\xda \xdf0\x1c\xcbu`\x1fI\xe8e\'\xef\xa5I\x9fp\xda\xb23\xf3\x80\xe0\xa2\xc2(uv0*&\xea3\x17ve\xa8n"\xaa\xb5\x98\r\xfe\xe3\xc7;%zj\xad/<]P\xae\xbd\xda\xfb\x06;\xc5\x91c\xc3\x1d\xb72\n\x11\xe1sx\xd1\xf90\x03\x1b\xdbR\xe2@\x93\xb5dB\x06d\xccu\x0e\x94j\xd6\xc4\x7f\x0fvE[yj\xbb\xc1\x0b\xee\x08\xe2j\x81X\xaca\xee\xea`h\xe8\xf2\x88\xfcBY[I\xe3n$v\xd9\xc2\\\x1a\x90\xe9\x8e\xc8\x14\x1b\xf4\xeb\x11\x86RR\x7f\x16\x0b\xb3\xa5p\xec%>@r\xbc\xfaFz6\xee\x9d\xdc\xa8\xb6In\xbcp(\x0bp4\xdb\x03\xc5\x14\xe6\x8cap\xc2\xfd\xf2/\xa0\xaf\xb9\xe4\x0c\xd1\x08E\xfd4\x83,b\xd2\x12\xd5\'\xb0Nh\xe7\xaa\xc8\xf1\x93\xa8\x9e\xd5\xb8J)*i\x0c\x96\xb9\xd5q\x9b\x10\x9d&\x0c\x13\x98.B\xefw\xd8\xa9\x0e\x1c\x8a`Vi\xb3\xbe\xaa\xac\xc1\xa2\xe7>\xef\x8f0\xfa3\x82\xba\x90\xb8s\xaa\xf3v\xaf\x0e\xd0\xc5w\x03\xc6\xb0\xf0\x90&\xd5S&6\x1d\xf9\xd2\r(\xf8e\x93\n:\xa8\xe9\xeb\x85\xee\xa5{\x1e\xf1%\x89\xf0\xcf\xe3\x98n\xb6\'\xee\xc1v\x07\x8fb\xb7\x11\xd4\x8a)\xe1\x96\xc4\xe9\xa0\xab\xb11\xfdr\xf5\xc61KA\x90\xb3\x8f\x81|70\x8e@r\xc3\xc22\x0c\xfe\xa3\x12/\xafv\xa8\xdc\xd4\xbe\xfa\x14\xe9\n6\xaf\x1dX\x80i\xa8:|\xb7 \x83\x98\xab@\xb7\x1b\x8e\xcd\xcb\x8b\xcd\xc7_\xc5]\x18\x92"\xe4\xcfG\xe8r\x03\xcc-\xc20\xf0\xe6\xeci\xee1\xcd\xe7\xc7y\x1b\x06\r\xf4\xff\x90`\x9f\xb2\xe9\xd2\x9f\x9c4\x9a\x1d\xf8\x05\xefg\xf7e2z\xc7\xf2\x15(l=\xda\xc2\xf5h\xe4\x7f\x92*Eyg\x82\x05\xf3\x97\xc3\x07\x12\xc4\xe7\x95\x8c\xf5\xac:\xba\x0c\xa1h)\x1a\xf3{\xff\x99\xb6\x08\xcb|\x8f\x04>\xad\xb1\xa6\xf9:9\x03\xdeB\xd0p\xcfi\x8e\xe2M\x06>\xb0\x8b\nJ\xb6\xbe\x05\xe4\xa5\xbc\xff\x1e\xf1\xb2\x1a\x84\x956{\xfa\x0e-\xe3\xfa\xe2$S\x8b\xd8\xe0\xb9\x93g\x1e\x974\x0c\xd5\xcc\xfe<\xc3\x84\r\x16\xe4\xad4\x1b\xab\xb0P9\xff\xe4\xa5\xc2\xe5\x03\xea`9\x1cI\xbeo8\xaa\xd5\x8d\x96]5\xde\x87?\xe0q\x0b\xdfd.\x07\x9c\xaduq\xc9\xffW5\xed\xe9\x1fGA\xddp\xad\x9c\xbb\x07E\xfc!\xccZT4\xcd\xc8\x8e\xf2\x7ft6\ty\xac\xc5_\x18)2\xd5\xb2\xa5\xa6\x10\x82\x86Np\xc9`\x1b\xa0[lC\xe6\x14\xc3\xc4-M\xad\xe2|\xb7\xb1\x13\xfd>\x8f-F2\xdf\x8fawb\xa9\x1b\xbd\xff\xb4Q\x14\x0ep\x97^\xdf\\\x1d+\x87\x0cA\xdd\x97\x1e\x1b&\x8f\xdd\x8f\xdeV\xae\xb1S\x81p\x0fw6\xf71\x89\xce\x93\xabd{o\xa8\xb0a\x1b\xf9\x10i\x01z\xc5\xe2\x06\x17PI\xc5*\xce\xa36\xb1\xf6\x92"\xc1mAqJ\xf1U\x14p\xc7J\xe7"\x91\x87\x8c\x97\x9e\xe0\xb18\xda\xd3\xa6\xf6\xb9e\xfc\xff\xe8n\x1f\x83\x15\xaf\x92\x04@C@b\n\xda\xfafGN\xcchu\xf3%\x08\xb5\x8e\xaa#\x06y\x83\xb2\xd7.\xf9M\xc6}\x172\xafU\xdb^Dr.?\x908\xeeG\xb6-v\x87:\x94\x00\x8b.}\x90\xd3\xdf\xc8\x9c\x0c\x8a\xcb\x01Qf\x98\xb8\xca\xc6\xef\\\x1aZ\x820\xe9\xde\x80\xc7\x9cN\xa6\r\x7f \xd7`\x0f[\x13Z\xce\xe8\xd4s\xb0"\x0f-z\\\xc1\x9ag\x85\x05\xe5xd\xfc\xac\xe8Vh\x85\xec\xb3C\xde\xafW\xde\xff\xde\xb2\xfa\xcc(8M\xd1O\x85\xfdGY\x96\xfe\xf2\xf6\xcc\xa6\t\xab\xb2\xf7\xa6\xaa\x85\xba\xda`\xe4\x04\x05[\xaa\x9bT\x07@\xb29\xa5Tn*\xdf\xcb\xc4\xd3\x19N\x82R\xf8\xb9\x8dox\xd2*.\xc9_j\xfc\x00*\'\xa2If\xfb\xc3\xaf\xd6\xb9X\xbe\x1b[=U&\x0b\xe6*N\xb7\x18\xcb(T\x99\x16G\'\x8a\xe4^\x1f4\xd7\xa9\xf5S\t\x87SL,\x11\x02\xbe(;~\xd5\xe0\x18\x00C;Q\xfd\xd1h\'\x95O\x9d\tv\xe4l+x\xc4b\xc73\x08\xc4\x07\xbc@@f\xe7\xca*]\xb2H\r\xd4\x85\xa4Q.I\x1cy\x0fP=\xd5\x9el2\xbe\xc10\x10\x1e\xb0hJC\xc8`\x1e)\xc8\xe3qB\xd0\xcf\xdc\xcb>\xad\x8e\xcb\x05\x14\x86\x97\t\x02\x9c}\xa9\x94F\x85s\xce\xeb\x94r\x9d\xab\xa1\x07\x91\xc9Q\x7ft\xc8i)Yk\xac\xfc\xa7\xa9^\x11\xc3S\xd7\xde\x00%O\xa8q\x9b\x88\xc7\xab \xfd|i\x86\xca\x02L\xd0\xe7T\xb62\x1e\x02hU\xe3\xf2\xce\x17|\xb2\x13^ng\xa2\xf1\xccR##\xb2 \xf9eyi\xf5J\xff\x87/n/$\xc3\x10;\x9e\x9e\xb2\xec\xbf\x1c)}\xde\xfc\xb9}8\xb15\x16\x8e\x87\xf9\xb1\x16e\xb5\xbe\xb2\xc8\x7fw\xd5\x81\x13\x13o%\xb6A!\xd9\xd6\xf4\x99\xb5\xf3\x15\xeae:F\xb9pW\xd7J\n\x9e\xe2c\x88Z\xaa\xb5'

# Convert bytes to bits
bits = bytes_to_bits(input_bytes)

# Print the output
# print(bits)
