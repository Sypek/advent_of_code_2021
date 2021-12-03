using DelimitedFiles

INPUT_FILE_PATH = "data/day_3/input.txt"

input = readdlm(INPUT_FILE_PATH, String, skipblanks=true)

n_rows = length(input)
n_cols = length(input[1])

M = Matrix{Bool}(undef, n_rows, n_cols)
for i in 1:n_rows
    for (j, number) in enumerate(input[i])
        M[i, j] = parse(Bool, number)
    end
end

most_common_arr = copy(M)
least_common_arr = copy(M)

for i in 1:n_cols
    current_column = most_common_arr[:, i]
    len = length(current_column)
    if len == 1
        break
    end
    if sum(current_column) >= (length(current_column) / 2)  # there are more ones than zeros or the same number
        global most_common_arr = most_common_arr[current_column .> 0, :]
    else # there are more zeros than ones
        global most_common_arr = most_common_arr[current_column .== 0, :]
    end
end


for i in 1:n_cols
    current_column = least_common_arr[:, i]
    len = length(current_column)
    if len == 1
        break
    end
    if sum(current_column) >= (length(current_column) / 2)  # there are more ones than zeros or the same number
        global least_common_arr = least_common_arr[current_column .== 0, :]
        # print("Round: $i, ")
    else # there are more zeros than ones
        global least_common_arr = least_common_arr[current_column .> 0, :]
    end
end

println(most_common_arr)
println(least_common_arr)

oxygen_generator_rating = ""
for i in most_common_arr
    global oxygen_generator_rating = oxygen_generator_rating * string(convert(Int, i))
end

CO2_scrubber_rating = ""
for i in least_common_arr
    global CO2_scrubber_rating = CO2_scrubber_rating * string(convert(Int, i))
end

oxygen_generator_rating = parse(Int, oxygen_generator_rating; base=2)
CO2_scrubber_rating = parse(Int, CO2_scrubber_rating; base=2)


println(oxygen_generator_rating)
println(CO2_scrubber_rating)

final_score = oxygen_generator_rating * CO2_scrubber_rating
print("final score: $final_score")