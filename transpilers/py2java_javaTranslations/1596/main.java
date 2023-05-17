public void System.out.printlns ( a , n , ind ) {
    var b = { None } * 2 * n;
    var i = 0;
    while (i < n) {
        b { i } = b { n + i } = a { i };
        i = i + 1;
    }
     i = ind;
    while (i < n + ind) {
        System.out.println ( b { i } , end = " " ) ;;
        i = i + 1;
    }
 }
var a = { 'A' , 'B' , 'C' , 'D' , 'E' , 'F' };
var n = len ( a ) ;;
System.out.printlns ( a , n , 3 ) ;;
