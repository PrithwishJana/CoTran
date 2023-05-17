public void even_or_odd ( N ) {
    var l = len ( N ) ;;
    if (( N { l - 1 } == '0' or N { l - 1 } == '2' or N { l - 1 } == '4' or N { l - 1 } == '6' )) {
        return ( "Even" );
    }
     else{
        return ( "Odd" );
    }
}
var N = "735";
System.out.println ( even_or_odd ( N ) );
