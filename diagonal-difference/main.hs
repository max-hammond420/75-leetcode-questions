import Data.List

chop :: Int -> [Int] -> [[Int]]
chop _ [] = []
chop n xs = take n xs:chop n (drop n xs)

sumDiagonal :: [[Int]] -> Int
sumDiagonal x = sum $ map (uncurry (!!)) $ zip x [0..]

solve :: [Int] -> Int
solve (x:xs) = abs $ sumDiagonal (chop x xs) - sumDiagonal (map reverse $ chop x xs)

main :: IO ()
main = interact $ show . solve . map read . words
