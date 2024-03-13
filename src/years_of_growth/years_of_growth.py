def years_of_growth(
    initial_population,
    target_population,
    growth_rate,
    net_migration
):
    growth_rate_percentage = 1 + (growth_rate/100)
    current_population = initial_population
    years = 0
    while current_population < target_population:
        current_population = (current_population * growth_rate_percentage) + net_migration
        years +=1
    return years