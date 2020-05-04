# Name: ...
# UW NetID: ...
# Section: ...
# CSE 160
# Homework 5: Election prediction

import csv
import os
import time

def read_csv(path):
    """Reads the CSV file at path, and returns a list of rows from the file.

    Parameters:
        path: path to a CSV file. 

    Returns:
        list of dictionaries: Each dictionary maps the columns of the CSV file
        to the values found in one row of the CSV file. Although this function 
        will work for any csv file, for our purposes, depending on the contents
        of the CSV file, this will typically be a list of *ElectionDataRow*s or
        a list of *PollDataRow*s (or a list of electoral college data rows).
    """
    output = []
    csv_file = open(path)
    for row in csv.DictReader(csv_file):
        output.append(row)
    csv_file.close()    
    return output


################################################################################
# Problem 1: State edges
################################################################################

def row_to_edge(row):
    """Given an *ElectionDataRow* or *PollDataRow*, returns the 
    Democratic *Edge* in that *State*.

    Parameters:
        row: an *ElectionDataRow* or *PollDataRow* for a particular *State*

    Returns:
        Democratic *Edge* in that *State*: a float
    """
    return float(row["Dem"]) - float(row["Rep"])

 
def state_edges(election_result_rows):
    """Given a list of *ElectionDataRow*s, returns *StateEdge*s.

    Parameters:
        election_result_rows: list of *ElectionDataRow*s 
            This list has no duplicate *States*; that is, each *State* is 
            represented at most once in the input list.

    Returns:
        *StateEdges*: 
            dictionary from *State* (string) to *Edge* (float)
    """
    #TODO: Implement this function
    pass


################################################################################
# Problem 2: Find the most recent poll row
################################################################################

def earlier_date(date1, date2):
    """Given two dates as strings, returns True if date1 is before date2.

    Parameters:
        date1: a string representing a date (formatted like "Oct 06 2012")
        date2: a string representing a date (formatted like "Oct 06 2012")

    Returns:
        bool: True if date1 is before date2.
    """
    return (time.strptime(date1, "%b %d %Y") < time.strptime(date2, "%b %d %Y"))


def most_recent_poll_row(poll_rows, pollster, state):
    """ Given a list of *PollDataRow*s, returns the most recent (i.e. latest)
    row with the specified *Pollster* and *State*. If no such row exists, 
    it returns None.

    Parameters:
        poll_rows: a list of *PollDataRow*s
        pollster: a string representing a *Pollster*
        state: a string representing a *State*

    Returns:
        A *PollDataRow*: a dictionary from string to string  OR 
        None, if no such row exists
    """
    #TODO: Implement this function
    pass


################################################################################
# Problem 3: Pollster predictions
################################################################################

def unique_column_values(rows, column_name):
    """Given a list of rows and the name of a column (a string), 
    returns a set containing all values in that column.

    Parmeters:
        rows: a list of rows (could be a *PollDataRow* or another type of row)
        column_name: a string
    
    Returns:
        A set: containing all unique values in column `column_name`
    """
    #TODO: Implement this function
    pass


def pollster_predictions(poll_rows):
    """Given a list of *PollDataRow*s, returns *PollsterPredictions*.
    For a given pollster, uses only the most recent poll for a state.

    Parameters:
        poll_rows: a list of *PollDataRow*s

    Returns:
        A *PollsterPredictions*: a dictionary from *Pollster* to *StateEdges*
    """
    #TODO: Implement this function
    pass


################################################################################
# Problem 4: Pollster errors
################################################################################

def average_error(state_edges_predicted, state_edges_actual):
    """Given predicted *StateEdges* and actual *StateEdges*, returns
    the average error of the prediction.

    For each state present in state_edges_predicted, its error is
    calculated.  The average of all of these errors is returned.

    Parameters:
        state_edges_predicted: *StateEdges*, a dictionary from *State* to *Edge*
        state_edges_actual: *StateEdges*, a dictionary from *State* to *Edge*

    Returns:
        float: the average error
    """
    #TODO: Implement this function
    pass


def pollster_errors(pollster_predictions, state_edges_actual):
    """Given *PollsterPredictions* and actual *StateEdges*, 
    retuns *PollsterErrors*.

    Parameters:
        pollster_predictions: *PollsterPredictionss*, dictionary from *Pollster*
            to *StateEdges*
        state_edges_actual: *StateEdges*, dictionary from *State* to *Edge*

    Returns:
        *PollsterErrors*: a dictionary from *Pollster* to float (The float
        represents the *Pollster*'s average error).
    """
    #TODO: Implement this function
    pass


################################################################################
# Problem 5: Pivot a nested dictionary
################################################################################

def pivot_nested_dict(nested_dict):
    """Pivots a nested dictionary, producing a different nested dictionary
    containing the same values.

    The input is a dictionary d1 that maps from keys k1 to dictionaries d2,
    where d2 maps from keys k2 to values v.
    The output is a dictionary d3 that maps from keys k2 to dictionaries d4,
    where d4 maps from keys k1 to values v.
    For example:
      input = { "a" : { "x": 1, "y": 2 },
                "b" : { "x": 3, "z": 4 } }
      output = {'y': {'a': 2},
                'x': {'a': 1, 'b': 3},
                'z': {'b': 4} }
    """
     #TODO: Implement this function
    pass


################################################################################
# Problem 6: Average the edges in a single state
################################################################################

def average_error_to_weight(error):
    """Given the average error of a *Pollster*, returns that pollster's weight.

    Parameters:
        error: a float representing a *Pollster*'s average error, 
            The error must be a positive number.

    Returns:
        float: weight, calculated as 1/(error)^2
    """
    return error ** (-2)

# The default average error of a pollster who did no polling in the
# previous election.
DEFAULT_AVERAGE_ERROR = 5.0

def pollster_to_weight(pollster, pollster_errors):
    """"Given a *Pollster* and a *PollsterErrors*, return 
    the given pollster's weight.

    Parameters:
        pollster: *Pollster*, a string
        pollster_errors: *PollsterErrors*, a dictionary from *Pollster* to float

    Returns:
        float: weight
    """
    if pollster not in pollster_errors:
        weight = average_error_to_weight(DEFAULT_AVERAGE_ERROR)
    else:
        weight = average_error_to_weight(pollster_errors[pollster])
    return weight


def weighted_average(items, weights):
    """Returns the weighted average of a list of items.

    Parameters:
        items: a list of numbers.
        weights: a list of numbers, whose sum is nonzero.
            Each weight in weights corresponds to the item in items at 
            the same index. items and weights must be the same length.

    Returns:
        float: the weighted average, the sum of (product of each item and 
        its weight) divided by (the sum of the weights)
    """
    assert len(items) > 0
    assert len(items) == len(weights)
    #TODO: Implement this function
    pass


def average_edge(pollster_edges, pollster_errors):
    """Given *PollsterEdges* and *PollsterErrors*, returns the average 
    of these *Edge*s weighted by their respective *PollsterErrors*.
    
    Parameters:
        pollster_edges: *PollsterEdges*, a dictionary from *Pollster* to *Edge*
        pollster_errors: *PollsterErrors*, a dictionary from *Pollster* to float

    Returns:
        float: the weighted average of the *Edge*s, weighted by the errors
    """
    #TODO: Implement this function
    pass


################################################################################
# Problem 7: Predict the 2012 election
################################################################################

def predict_state_edges(pollster_predictions, pollster_errors):
    """Given *PollsterPredictions* from a current election and *PollsterErrors*
    from a past election, returns predicted *StateEdges* of the current election.

    Parameters:
        pollster_predictions: *PollsterPredictions*, a dictionary from 
            *Pollster* to *StateEdges*
        pollster_errors: *PollsterErrors*, a dictionary from *Pollster* to float

    Returns:
        *StateEdges*: predicted *StateEdges* of the current election
    """
    #TODO: Implement this function
    pass


################################################################################
# Electoral College, Main Function, etc.
################################################################################

def electoral_college_outcome(ec_rows, state_edges):
    """Given electoral college rows and *StateEdges*, returns the outcome of
    the Electoral College.

    Parameters:
        ec_rows: a list of electoral college rows, where an electoral college
            row is a dictionary from string to string (similar to an
            *ElectionDataRow* or a *PollDataRow* but with different keys)
        state_edges: *StateEdges*, a dictionary from *State* to *Edge*
        
    Returns:
        dictionary containing only the keys "Dem" and "Rep", mapped to a 
        number (as a float) of electoral votes won by that party.  
        If a state has an edge of exactly 0.0, its votes are evenly divided 
        between both parties.
    """
    ec_votes = {}               # maps from state to number of electoral votes
    for row in ec_rows:
        ec_votes[row["State"]] = float(row["Electors"])

    outcome = {"Dem": 0, "Rep": 0}
    for state in state_edges:
        votes = ec_votes[state]
        if state_edges[state] > 0:
            outcome["Dem"] += votes
        elif state_edges[state] < 0:
            outcome["Rep"] += votes
        else:
            outcome["Dem"] += votes / 2.0
            outcome["Rep"] += votes / 2.0
    return outcome


def print_dict(dictionary):
    """Given a dictionary, prints its contents in sorted order by key.
    Rounds float values to 8 decimal places.

    Returns:
        None
    """
    for key in sorted(dictionary.keys()):
        value = dictionary[key]
        if type(value) == float:
            value = round(value, 8)
        print key, value


def main():
    """Main function, executed when election.py is run as a Python script.
    """
    # Read state edges from the 2008 election
    edges_2008 = state_edges(read_csv("data/2008-results.csv"))

    # Read pollster predictions from the 2008 and 2012 election
    polls_2008 = pollster_predictions(read_csv("data/2008-polls.csv"))
    polls_2012 = pollster_predictions(read_csv("data/2012-polls.csv"))

    # Compute pollster errors for the 2008 election
    error_2008 = pollster_errors(polls_2008, edges_2008)

    # Predict the 2012 state edges
    prediction_2012 = predict_state_edges(polls_2012, error_2008)

    # Predict the 2012 Electoral College outcome
    row_list = read_csv("data/2012-electoral-college.csv")
    ec_2012 = electoral_college_outcome(row_list, prediction_2012)

    print "Predicted 2012 election results:"
    print_dict(prediction_2012)
    print

    print "Predicted 2012 Electoral College outcome:"
    print_dict(ec_2012)
    print


# If this file, election.py, is run as a Python script (such as by typing
# "python election.py" at the command shell), then run the main() function.
if __name__ == "__main__":
    main()


###
### Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").
