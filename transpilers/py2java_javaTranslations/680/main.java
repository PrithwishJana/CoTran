n_hamsters : var int = int ( input ( ) );
var hamsters = input ( );
var hamsters_standing = len ( { ham for ham in hamsters if ham == "X" } );
hamsters_sitting = n_hamsters - hamsters_standing;
if (hamsters_standing == hamsters_sitting) {
    System.out.println ( 0 );
    System.out.println ( hamsters );
}
 else if (hamsters_standing > hamsters_sitting){
    var num_change = ( hamsters_standing - hamsters_sitting ) // 2;
    System.out.println ( num_change );
    result = "";
    for (int hamster = 0; hamster < hamsters.length; hamster++){
        if (hamster == "X" and num_change > 0) {
            result += "x";
            num_change -= 1;
        }
         else{
            result += hamster;
        }
    }
    System.out.println ( result );
}
else{
    num_change = ( hamsters_sitting - hamsters_standing ) // 2;
    System.out.println ( num_change );
    var result = "";
    for (int hamster = 0; hamster < hamsters.length; hamster++){
        if (var hamster == "x" and num_change > 0) {
            result += "X";
            num_change -= 1;
        }
         else{
            result += hamster;
        }
    }
    System.out.println ( result );
}
