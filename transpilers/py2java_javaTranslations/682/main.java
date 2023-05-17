import sys;
public void knapSack ( W , wt , val , n ) {
    var maxratio = - sys . maxsize - 1 ;;
    maxindex = 0 ;;
    for i in range ( n ) :
        if (( ( val { i } / wt { i } ) > maxratio )) {
            maxratio = ( val { i } / wt { i } ) ;;
            var maxindex = i ;;
        }
     return ( W * maxratio ) ;;
}
var val = { 14 , 27 , 44 , 19 } ;;
var wt = { 6 , 7 , 9 , 8 } ;;
var n = len ( val ) ;;
var W = 50 ;;
System.out.println ( knapSack ( W , wt , val , n ) ) ;;
