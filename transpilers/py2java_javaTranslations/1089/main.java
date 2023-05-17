public void D_Pattern ( string , n ) {
    for i in range ( 0 , n ) :
        for j in range ( 0 , n ) :
            if (( var j == 1 or ( ( i == 0 or i == n - 1 ) and ( j > 1 and j < n - 2 ) ) or ( j == n - 2 and i != 0 and i != n - 1 ) )) {
                var string = string + "*";
            }
             else{
                string = string + " ";
            }
        string = string + "\n";
    return ( string ) ;;
}
string = "" ;;
var n = 9;
System.out.println ( D_Pattern ( string , n ) ) ;;
