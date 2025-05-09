# =============================================================================
# OmniCo Confidential
# -------------------
# This source code contains proprietary information of OmniCo.
# =============================================================================

def main():
    # print("Euphoria User Engagement Analysis Report")
    # print("----------------------------------------")
    # print()
    # # Initialize the stats dictionary for each algorithm
    stats = {
        'JoyStream': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        },
        'SerenityFlow': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        },
        'DeepPulse': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        }
    }

    # Open the CSV file and read data
    with open('euphoria_data.csv', 'r') as file:
        # Skip the header line
        header = file.readline()

        # Read each line in the file
        for line in file:
            # Remove any trailing whitespace characters like newline
            clean_line = line.strip()
            print(clean_line)

            # Split the line into a list of values
            columns = line.split(',')

            # Assign each column to a variable
            user_id = columns[0]
            algorithm = columns[1]
            session_duration = int(columns[2])
            happiness_rating = int(columns[3])

            # TODO: Define session_duration and happiness_rating variables and convert them to integers
            # Hint: Use the int() function to convert strings to integers
            # session_duration = ?
            # happiness_rating = ?

            # Update stats based on the algorithm
            if algorithm in stats:
                stats[algorithm]['total_happiness'] += happiness_rating
                stats[algorithm]['total_duration'] += session_duration
                stats[algorithm]['session_count'] += 1
            else:
                # Handle any unexpected algorithm names
                print(f"Unknown algorithm: {algorithm}")

    # TODO: Calculate averages for each algorithm
    print("Average Happiness Rating per Algorithm")
    for algorithm in stats: 
      avg_happiness = stats[algorithm]['total_happiness'] / stats[algorithm]['session_count']
      print(f"- {algorithm}: {avg_happiness}")
      
    print("Sessions per Algorithm")
    for algorithm in stats: 
      print(f"- {algorithm}: {stats[algorithm]['session_count']}")
    longest_session_duration = 0

    print("Average Session Duration per Algorithm")
    for algorithm in stats: 
      avg_duration = stats[algorithm]['total_duration'] / stats[algorithm]['session_count']
      print(f"- {algorithm}: {avg_duration}")
      if avg_duration > longest_session_duration:
         longest_session_duration = avg_duration
    
    print("Highest Average Happiness Rating")
    highest_avg_happiness = 0
    if avg_happiness > highest_avg_happiness:
        highest_avg_happiness = avg_happiness
    print(f"- {algorithm} with an average happiness rating of {highest_avg_happiness}")
    
    print("Longest Average Session Duration")
    print(f"- {algorithm} with an average session duration of {longest_session_duration} minutes")




    

      



    #   - Store these back into the stats dictionary under 'avg_happiness' and 'avg_duration'


    # TODO: Determine the algorithm with the highest average happiness rating
    # Initialize variables to keep track of the highest average happiness and the corresponding algorithm
    # Loop through stats to compare avg_happiness values

    # TODO: Determine the algorithm with the longest average session duration
    # Initialize variables to keep track of the longest average duration and the corresponding algorithm
    # Loop through stats to compare avg_duration values

    # TODO: Print the report
    # Use print statements to display the results in a formatted way
    # Follow the structure provided in the example output

if __name__ == "__main__":
    main()