import sys;
for l in sys . stdin :
    a , b , var n = map ( int , l . split ( " " ) );
    System.out.println ( sum ( map ( int , list ( str ( ( a % b ) * 10 ** n // b ) ) ) ) );
