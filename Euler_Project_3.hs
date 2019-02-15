-- https://projecteuler.net/problem=3
-- answer: 6857
largest_prime_factor :: Integer -> Integer

largest_prime_factor l = helper l 1 2
    where helper l max_f count  | l == 1            = max_f
                                | mod l count == 0  = helper (div l count) count count
                                | otherwise         = helper l max_f (count+1)

