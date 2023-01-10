solve :: [Int] -> [Int] -> [Int] -> [Int]
solve (a:as) (b:bs) (x:y:xs)
    | a > b     = solve as bs (x+1:y:[])
    | a < b     = solve as bs (x:y+1:[])
    | a == b    = solve as bs (x:y:[])
    | otherwise = x:y:[]

main :: IO ()
main = undefined
