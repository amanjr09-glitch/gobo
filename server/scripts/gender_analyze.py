# Based on Nathan Matias's "Follow Bias" code
# https://github.com/mitmedialab/fbserver

import csv
import os

class NameGender:

    def __init__(self):
        self.names = {
            'male': self._read_names("male"),
            'female': self._read_names("female")
        }

        self.computed_names = {}

    def process(self, name):
        score = {'result': "", 'counts': 0}

        if name and name!="":
            if (isinstance(name, basestring) and name != ""):

                first_name = name.split(" ")[0].lower()
            else:
                first_name = None


        # try to retrieve from cache
        if first_name and first_name in self.computed_names:
                score = self.computed_names[first_name]
        else:
            male = self.names['male']['counts'][first_name] if first_name in self.names['male']['counts'] else 0
            female = self.names['female']['counts'][first_name] if first_name in self.names['female']['counts'] else 0
            total = male + female
            prob_male = 0
            prob_female = 0
            if (total > 0):
                return 0
#
#     # compute probabilities
#     prob_male = male / total.to_f if male
#     prob_female = female / total.to_f if female
#
#     score[:counts] = {:male = > prob_male,:female = > prob_female}
#     end
#
#     if (male > 0 & & female > 0)
#         if (prob_female > 0.66)
#             score[:result] = "Female"
#         elsif(prob_male > 0.66)
#         score[:result] = "Male"
#     else
#         score[:result] = "Unknown"
#     end
# elsif(male > 0)
# score[:result] = "Male"
# elsif(female > 0)
# score[:result] = "Female"
# else
# if ( @ names[:male][:definite].index(first_name))
# score[:result] = "Male"
# score[:counts] = {:male = > 1.0,:female = > 0.0}
# elsif( @ names[:female][:definite].index(first_name))
# score[:result] = "Female"
# score[:counts] = {:male = > 0.0,:female = > 1.0}
# else
# score[:result] = "Unknown"
# score[:counts] = {:male = > 0.0,:female = > 0.0}
# end
# end
#
#
# # cache for future use
# @computed_names
#
#
# [first_name] = score
# end
# else
# score[:result] = "Unknown"
# score[:counts] = {:male = > 0.0,:female = > 0.0}
# end
#
# score
# end

    def _read_names(self, gender):
        lang = "EN"
        country = "US"

        count_file_name = gender + "_names_" + lang + "_" + country + ".csv"
        definite_file_name = gender + "_auxilliary.csv"

        count_data = {}
        definite_data = []

        full_path = os.path.realpath(__file__)
        filepath = os.path.join(os.path.dirname(full_path), 'static_data/names/{}')

        with open(filepath.format(count_file_name), 'rb') as csvfile:
            namesreader = csv.reader(csvfile)
            for name_pair in namesreader:
                count_data[name_pair[0].lower()] = float(name_pair[1])

        with open(filepath.format(definite_file_name), 'rb') as csvfile:
            definite_data = [name.lower().strip() for name in csvfile.readlines()]

        return {
            'counts': count_data,
            'definite': definite_data
        }


