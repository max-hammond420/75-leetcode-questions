import Data.List

chop :: Int -> [Int] -> [[Int]]
chop _ [] = []
chop n xs = take n xs:chop n (drop n xs)

-- sumDiagonal :: [Int] -> Int
sumDiagonal x = sum $ zipWith (uncurry (!!)) [0..] $ chop 3 x

solve :: [Int] -> int
solve x = abs (sumDiagonal $ tail x - sumDiagonal $ transpose $ tail x)
-- solve [x] = abs (solvr [x] - solvl [x])

main :: IO ()
main = undefined
