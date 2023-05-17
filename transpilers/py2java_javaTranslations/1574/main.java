public void Odd_Sum ( n ) {
    var total = ( n + 1 ) // 2;
    odd = total * total;
    return odd;
}
public void Even_Sum ( n ) {
    total = n // 2;
    var even = total * ( total + 1 );
    return even;
}
public void sumLtoR ( L , R ) {
    var odd_sum = Odd_Sum ( R ) - Odd_Sum ( L - 1 );
    var even_sum = Even_Sum ( R ) - Even_Sum ( L - 1 );
    return even_sum - odd_sum;
}
var L = 1 ; R = 5;
System.out.println ( sumLtoR ( L , R ) );
