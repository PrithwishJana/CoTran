class Solution extends  object {
    public void addStrings ( this , num1 , num2 ) {
        var res = {};
        var pos1 = len ( num1 ) - 1;
        var pos2 = len ( num2 ) - 1;
        var carry = 0;
        while (pos1 >= 0 or pos2 >= 0 or carry == 1) {
            digit1 = digit2 = 0;
            if (pos1 >= 0) {
                digit1 = ord ( num1 { pos1 } ) - ord ( '0' );
            }
             if (pos2 >= 0) {
                digit2 = ord ( num2 { pos2 } ) - ord ( '0' );
            }
             res . append ( str ( ( digit1 + digit2 + carry ) % 10 ) );
            carry = ( digit1 + digit2 + carry ) // 10;
            pos1 -= 1;
            pos2 -= 1;
        }
         return '' . join ( res { : : - 1 } );
    }
}

if (var __name__ == "__main__") {
    var sObj = Solution ( );
    var num1 = "11";
    var num2 = "123";
    var out = sObj . addStrings ( num1 , num2 );
    System.out.println ( out );
}
 