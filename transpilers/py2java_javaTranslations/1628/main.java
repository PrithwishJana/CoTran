var n = int ( input ( ) );
chips = list ( map ( int , input ( ) . split ( ) ) );
odd = 0;
even = 0;
for (int num = 0; num < chips.length; num++){
    if (num % var 2 == 0) {
        even += 1;
    }
     else{
        odd += 1;
    }
}
System.out.println ( min ( even , odd ) );
