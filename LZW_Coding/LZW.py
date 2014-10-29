"""
LZW编码解码
lang:python
date:2014-10-29
author:you_shoubian
"""
def lzw( s ):
    '''
        LZW编码解码：
        s:待编码字符串
        encoding_dic:编码字典
        decoding_dic:解码字典
        index:索引
        p:当前前缀
        c:字符流中的下一个字符
        encoding:编码序列
        decoding_str:解码序列
        '~':起始标志
        '$':结束标志
    '''
    encoding_dic = {'~':'0', '$':'1'}
    decoding_dic = {'0':'~', '1':'$'}
    '''
        LZW编码
    '''
    index = 1
    for i in range( len( s ) ):
        if not s[i] in encoding_dic:
            index = index + 1
            encoding_dic[s[i]] = str( index )
            decoding_dic[str( index )] = s[i]
    # print( encoding_dic )
    encoding = ''
    p = ''
    c = ''
    s = '~' + s + '$'
    for i in range( len( s ) ):
        c = s[i]
        if c == '$':
            encoding = encoding + encoding_dic[p]
            encoding = encoding + encoding_dic['$']
            break
        if p + c in encoding_dic:
            p = p + c
        else:
            encoding = encoding + encoding_dic[p]
            index = index + 1
            encoding_dic[p + c] = str( index )
            decoding_dic[str( index )] = p + c
            p = c
    print( encoding )

    '''
        LZW解码
    '''
    # print( decoding_dic )
    decoding_str = ''
    for i in range( len( encoding ) ):
        if encoding[i] == '0':
            decoding_str = decoding_str + ''
        elif encoding[i] == '1':
            decoding_str = decoding_str + ''
            break
        else:
            decoding_str = decoding_str + decoding_dic[encoding[i]]
    print( decoding_str )

if __name__ == '__main__':
    s = input( "please input a string:" )
    lzw( s )
