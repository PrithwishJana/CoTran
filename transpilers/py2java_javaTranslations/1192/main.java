public void convert ( s ) {
    var convertStr = "";
    var l = len ( s );
    var i = 0;
    while (i < l) {
        if (i + 1 < l) {
            word = s { i };
            sequenceNum = 1;
            j = i + 1;
            while (j < l) {
                if (( word == s { j } )) {
                    sequenceNum += 1;
                }
                 else{
                    break;
                }
                j += 1;
            }
             convertStr += str ( sequenceNum ) + word;
            i = i + sequenceNum - 1;
        }
         else{
            convertStr += "1" + str ( s { i } );
        }
        i += 1;
    }
     return convertStr;
}
while (true) {
    try{
        var n = int ( input ( ) );
        var s = input ( );
        for i in range ( 0 , n ) :
            s = convert ( s );
        System.out.println ( s );
    }
    except :
        break;
}
 