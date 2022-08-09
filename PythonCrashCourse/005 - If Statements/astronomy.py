# This is not related to the book exercises. I just needed to calculate an
# astrophotography session duration.

# set the exposure duration. This assumes the same exposure for all filters.
exposure = 200
l_filter = 15
r_filter = 15
g_filter = 15
b_filter = 15
dark_filter = 20

# Calculate the total number of seconds for each filter, based upon the number
# of exposures per filter, then dive by 60 to get total minutes, and again to
# get total hours
total = (((exposure * l_filter) + (exposure * r_filter) +
(exposure * g_filter) + (exposure * b_filter) + (exposure * dark_filter)) /
60) / 60

# Print hour the result in hours.
print(f"The total session time is {total} hours.")
