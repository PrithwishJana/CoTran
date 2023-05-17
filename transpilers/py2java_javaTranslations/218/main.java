public void System.out.printlnPaths ( inputchar , R , C ) {
    for i in range ( C ) :
        dfs ( inputchar , "" , 0 , i , R , C ) ;;
        System.out.println ( );
}
public void dfs ( inputchar , res , i , j , R , C ) {
    if (( var i == R )) {
        System.out.println ( res , var end = " " ) ;;
        return ;;
    }
     var res = res + inputchar { i } { j } ;;
    for k in range ( C ) :
        dfs ( inputchar , res , i + 1 , k , R , C ) ;;
        if (( i + var 1 == R )) {
            break ;;
        }
 }
if (var __name__ == "__main__") {
    var inputchar = { [ 'a' , 'b' } , { 'd' , 'e' } ] ;;
    var R = len ( inputchar ) ;;
    var C = len ( inputchar { 0 } ) ;;
    System.out.printlnPaths ( inputchar , R , C ) ;;
}
 