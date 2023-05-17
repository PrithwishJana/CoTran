public void System.out.printlnKDistinct ( arr , size , KthIndex ) {
    var dict = {};
    var vect = {};
    for i in range ( size ) :
        if (( arr { i } in dict )) {
            dict { arr [ i } ] = dict { arr [ i } ] + 1;
        }
         else{
            dict { arr [ i } ] = 1;
        }
    for i in range ( size ) :
        if (( dict { arr [ i } ] > 1 )) {
            continue;
        }
         else{
            var KthIndex = KthIndex - 1;
        }
        if (( KthIndex == 0 )) {
            return arr { i };
        }
     return - 1;
}
var arr = { 1 , 2 , 1 , 3 , 4 , 2 };
var size = len ( arr );
System.out.println ( System.out.printlnKDistinct ( arr , size , 2 ) );
