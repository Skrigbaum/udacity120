#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load((open("../final_project/final_project_dataset.pkl", "rb")), fix_imports=True)

n_poi,n_poi_nan_pay, n_sal, n_email, total_people, nan_people = 0,0,0,0,0,0

print("Number of features: " + str(len(enron_data["SKILLING JEFFREY K"])))

for i in enron_data:
    total_people += 1
    if enron_data[i]["poi"]:
        n_poi += 1
        if enron_data[i]["total_payments"] == "NaN":
                n_poi_nan_pay += 1
    if enron_data[i]["total_payments"] == "NaN":
            nan_people += 1
    if enron_data[i]["salary"] != "NaN":
        n_sal += 1
    if enron_data[i]["email_address"] != "NaN":
        n_email += 1



print("Number of persons of interest: " + str(n_poi))

print("Stock of James Prentice: " + str(enron_data["PRENTICE JAMES"]["total_stock_value"]))
print("Emails from Wesley Colwell to POI: " + str(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]))
print("Jeffery K Skilling stock options: " + str(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]))

print("SKILLING PAYMENTS: " + str(enron_data["SKILLING JEFFREY K"]["total_payments"]))
print("LAY PAYMENTS: " + str(enron_data["LAY KENNETH L"]["total_payments"]))

print("FASTOW PAYMENTS: " + str(enron_data["FASTOW ANDREW S"]["total_payments"]))
print("Salary: " + str(n_sal))
print("Emails: " + str(n_email))
print("Total POI that are NaN total payments: "+ str(n_poi_nan_pay))
print("Total People: "+ str(total_people))
print("Total people that are NaN total payments: " + str(nan_people))
