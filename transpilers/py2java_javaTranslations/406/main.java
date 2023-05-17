public void disp ( row_no , block ) {
    System.out.println ( row_no * block );
}
public void row ( ht , h ) {
    return ht // h;
}
public void calculate ( l , w , h , a , ht ) {
    var no_block = ( 4 * a ) // l;
    if (( h < w )) {
        var row_no = row ( ht , w );
    }
     else{
        row_no = row ( ht , h );
    }
    disp ( row_no , no_block );
}
if (var __name__ == '__main__') {
    var l = 50;
    var w = 20;
    var h = 35;
    var a = 700;
    var ht = 140;
    calculate ( l , w , h , a , ht );
}
 