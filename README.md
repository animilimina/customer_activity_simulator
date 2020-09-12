# Customer activity simulator

This module is used to randomly generate a customer activity over a set time period.

## How to
Download the package, and run it in your terminal using command:

    python [package path]/main.py

Once the script finishes running, an **ActiveUsers.csv** file will appear in your Downloads directory.

The file has two columns:
- user_id: a unique id for each simulated customer
- activity: all the time periods the customer has been active

## Python version
This package was created using Python 3.8, it should still be functional if you are using previous Python3 versions.

## Settings
The **settings.py** file is used to modify the simulation parameters.

#### periods
The number of periods the simulation must cover.
At each period, an amount of new customers will be created and their activity between this period and the last one simulated.

#### new_customer_base
A starting point for the first period new customers generation.

Each subsequent iteration uses the previous number as its base.

#### growth_rate
The average growth rate for new customers through periods.

At each period, a random local growth rate is generated using numpy.random.normal(), with
- mean = growth_rate
- sd = 1.1*abs(1 - growth_rate)

#### growth_rate_min
This value is an override for rare cases where we would get an equal to or below 0 growth rate.

#### returning_rate
The average probability an active customer will remain active the next period.

Each customer has their own returning rate randomly generated using numpy.random.normal with:
- mean = returning_rate
- sd = (1 - returning_rate) / 2

Values below 0 or above 1 are overridden with 0 and 1 respectively.

#### reactivation_rate
The average probability an inactive customer will become active the next period

Each customer has their own reactivation rate randomly generated using numpy.random.normal with:
- mean = reactivation_rate
- sd = (1 - reactivation_rate) / 2

Values below 0 or above 1 are overridden with 0 and 1 respectively.

#### survival_rate
The probability a customer will still be a customer the next period, regardless of their activity

Each customer has their own survival rate randomly generated using numpy.random.normal with:
- mean = survival_rate
- sd = (1 - survival_rate) / 2

Values below 0 or above 1 are overridden with 0 and 1 respectively.