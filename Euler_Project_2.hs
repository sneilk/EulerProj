-- https://projecteuler.net/problem=2
-- answer: 4613732

even_fib :: Integer

even_fib = helper 0 1 1
    where helper sum cur_n last_n   | cur_n >= 4000000 = sum
                                    | even cur_n       = helper (sum + cur_n) (last_n + cur_n) cur_n
                                    | otherwise        = helper sum (last_n + cur_n) cur_n
