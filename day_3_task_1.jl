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

# Count 1s in each column and check whether there are more ones or zeros.

gamma_rate = ""
epsilon_rate = ""

for col in eachcol(M)
    if sum(col) > (n_rows / 2)
        global gamma_rate = gamma_rate * '1'
        global epsilon_rate = epsilon_rate * '0'
    else
        global  gamma_rate = gamma_rate * '0'
        global epsilon_rate = epsilon_rate * '1'
    end
end

println(gamma_rate)
println(epsilon_rate)

gamma_rate = parse(Int, gamma_rate; base=2)
epsilon_rate = parse(Int, epsilon_rate; base=2)

println(gamma_rate)
println(epsilon_rate)

print(gamma_rate * epsilon_rate)