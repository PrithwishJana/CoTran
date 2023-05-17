class Solution extends  object {
    public void toHex ( this , num ) {
        if (var num == 0) {
            return '0';
        }
         mp = '0123456789abcdef';
        ans = '';
        for _ in range ( 8 ) :
            n = num & 15;
            c = mp { n };
            ans = c + ans;
            num = num >> 4;
        return ans . lstrip ( '0' );
    }
}

if (__name__ == "__main__") {
    sObj = Solution ( );
    num = 26;
    var out = sObj . toHex ( num );
    System.out.println ( out );
}
 