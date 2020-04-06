library('socialmixr')
data(polymod)

age_bin_edges <- c($age_bin_edges)
age_group_sizes <- c($age_group_sizes)
age_dist <- data.frame(age_bin_edges, age_group_sizes)

names(age_dist)[names(age_dist) == 'age_bin_edges'] <- 'lower.age.limit'
names(age_dist)[names(age_dist) == 'age_group_sizes'] <- 'population'

age_limits = c()
for(v in age_dist['lower.age.limit']) { age_limits <- v }

m <- contact_matrix(polymod,
                    countries = $country
                    age.limits = age_limits,
                    n=$num_sample,
                    survey.pop=age_dist)

mr <- Reduce("+", lapply(m$matrices, function(x) {x$matrix})) / length(m$matrices)