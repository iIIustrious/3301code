#Thanks to Soulseekah

import fractions

# Example:
# >> p = 61
# >> q = 53
# >> n = getn( p, q )
# >> p = phi( n ) # or phipq( p, q )
# >> es = generate_es( p, 2 )
# >> e = es[0] # 17
# >> d = getd( e, p )
# >> c = encrypt( 65, e, n )
# >> m = decrypt( c, d, n )
# >> m == c # True

# Hamming weight for n
def popcount( n ):
	return len( bin( n )[2:].replace( '0', '' ) )

# Phi of any n
def phi( n ):
	if n == 1: return 1
	return sum( filter( lambda x: x == 1, ( fractions.gcd( n, k ) for k in range( 1, n + 1 ) ) ) )

# Is this number prime?
def is_prime( n ):
	for i in range( 2, int( n**0.5 ) + 1 ):
		if n % i == 0:
			return False
	return True

# Several RSA primitives that allow you to
# play around with stuff...

# Is this e good for this phi?
def is_good_e( e, p ):
	# e is odd
	if e % 2 == 0:
		return False
	# 1 < e < phi(n)
	if e < 2 and e > p:
		return False
	# e and phi(n) are coprime
	if fractions.gcd( e, p ) != 1:
		return False
	return True

# Generates a list of valid e for phi
# with a Hamming weight restriction h, not all e
# are secure
def generate_es( p, h=False ):
	es = []
	# 1 < e < phi(n)
	for e in range( 2, p ):
		if is_good_e( e, p ):
			if not h:
				es.append( e )
			elif popcount( e ) == h:
				es.append( e )
	return es

# Phi of p and q
def phipq( p, q ):
	return ( p - 1 ) * ( q - 1 )

# Get n for a p and q
def getn( p, q ):
	if not is_prime( p ) or not is_prime( q ):
		raise Exception( 'p and q must be prime' )
	# n = pq
	return p * q

# Generates the private exponent from
# e and phi(n)
def getd( e, p ):
	# de = 1 mod phi(n)
	d = 2
	while True:
		if ( d * e ) % p == 1:
			return d
		d = d + 1

# Encrypt number using RSA given
# m, public exponent e and n
def encrypt( m, e, n ):
	# c = m^e mod n	
	return pow( m, e, n )

# Decrypt number
# c, private exponent d and n
def decrypt( c, d, n ):
	# m = c^d mod n
	return pow( c, d, n )
