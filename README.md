# Alien invastion

## How to run

To run use the following command

    cat mapfile | python app.py alien_count

## Assumptions
All aliens move at the same time on each step, i.e. more than one alien can end up in a city at a time and thus all aliens will fight and destroy the city and each other at the same time.

All input from the map file is sane e.g. there are no duplicate city names or there are no connection names without city entries.
