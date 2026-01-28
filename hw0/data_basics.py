import os
from typing import Tuple

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import pandas as pd


class DataBasics:
    def __init__(self, filename: str) -> None:
        """
        The constructor for DataBasics class, whih loads the csv file into a
        pandas dataframe and saves it to `self.df`.

        Parameters:
            filename (str): The filename of the csv file.

        Returns:
            None

        Examples:
            >>> db = DataBasics(os.path.join(os.path.dirname(__file__), \
                "exam_original.csv"))
            >>> db.df.head(3)
               Unnamed: 0  Gender EthnicGroup         ParentEduc LunchType   TestPrep  MathScore  ReadingScore  WritingScore
            0           0  female     group B  bachelor's degree  standard       none         72            72            74
            1           1  female     group C       some college  standard  completed         69            90            88
            2           2  female     group B    master's degree  standard       none         90            95            93

            >>> type(db.df)
            <class 'pandas.core.frame.DataFrame'>
        """

        # >>> YOUR CODE HERE >>>
        self.df = pd.read_csv(filename)
        # <<< END OF YOUR CODE <<<


    def preprocess(self) -> None:
        """
        This function preprocesses the dataframe. It drops the "Unnamed: 0"
        column and renames the "ParentEduc" column to "ParentEducation". It
        also prints the first 3 rows of the preprocessed dataframe.

        Parameters:
            None

        Returns:
            None

        Examples:
            >>> db = DataBasics(os.path.join(os.path.dirname(__file__), \
                "exam_original.csv"))
            >>> db.preprocess()
               Gender EthnicGroup    ParentEducation LunchType   TestPrep  MathScore  ReadingScore  WritingScore
            0  female     group B  bachelor's degree  standard       none         72            72            74
            1  female     group C       some college  standard  completed         69            90            88
            2  female     group B    master's degree  standard       none         90            95            93
        """

        # >>> YOUR CODE HERE >>>
        self.df = self.df.drop(columns=["Unnamed: 0"])
        self.df = self.df.rename(columns={"ParentEduc": "ParentEducation"})
        print(self.df.head(3))
        # <<< END OF YOUR CODE <<<


    def writing_stats_given_score(self, score: int) -> Tuple[float, float, float]:
        """
        This function calculates the the minimum, maximum, and median of the Math
        scores among students who scored less than or equal to `score` in writing. 
        The function returns these statistics as a tuple of floats.

        Parameters:
            score (int): The maximum score to consider.

        Returns:
            Tuple[float, float, float]: The minimum, maximum, and median of the maths
                scores.

        Examples:
            >>> db = DataBasics(os.path.join(os.path.dirname(__file__), "exam_original.csv"))
            >>> minimum, maximum, median = db.writing_stats_given_score(60)
            >>> minimum
            0.0
            >>> maximum
            84.0
            >>> median
            53.0
        """
        
        # >>> YOUR CODE HERE >>>
        # Filter rows where WritingScore is greater than or equal to the given score
        filtered_df = self.df[self.df['WritingScore'] <= score]
        
        # Calculate the minimum, maximum, and median of the WritingScore
        minimum = filtered_df['MathScore'].min()
        maximum = filtered_df['MathScore'].max()
        median = filtered_df['MathScore'].median()
        # <<< END OF YOUR CODE <<<

        return float(minimum), float(maximum), float(median)


    def generate_reading_score_histogram(self) -> Figure:
        """
        This function generates a histogram of the reading scores. The
        histogram should have 15 bins and include appropriate labels and title.
        The histogram is saved as a png file and returned as a matplotlib
        Figure object.

        Parameters:
            None

        Returns:
            plt.Figure: The histogram of the reading scores.

        Examples:
            >>> db = DataBasics(os.path.join(os.path.dirname(__file__), \
                "exam_original.csv"))
            >>> fig = db.generate_reading_score_histogram()
            >>> type(fig)
            <class 'matplotlib.figure.Figure'>
        """
        fig = plt.figure()
        # >>> YOUR CODE HERE >>>
        plt.hist(self.df['ReadingScore'], bins=15, edgecolor='black')
        plt.xlabel('Reading Score')
        plt.ylabel('Frequency')
        plt.title('Histogram of Reading Scores')
        # <<< END OF YOUR CODE <<<


        fig.tight_layout()
        fig.savefig(os.path.join(os.path.dirname(
            __file__), "reading_score_histogram.png"))

        return fig

    def generate_math_writing_scatterplot(self) -> Figure:
        """
        This function generates a scatterplot of the math and writing scores
        with appropriate labels and title. The edge color of the point is set
        to white and transparency to 0.95 for the scatterplot. It also adds a
        regression line to the scatterplot. The scatterplot is saved as a png
        file and returned as a matplotlib Figure object.

        Parameters:
            None

        Returns:
            plt.Figure: The scatterplot of the math and writing scores.

        Examples:
            >>> db = DataBasics(os.path.join(os.path.dirname(__file__), \
                "exam_original.csv"))
            >>> fig = db.generate_math_writing_scatterplot()
            >>> type(fig)
            <class 'matplotlib.figure.Figure'>
        """
        fig = plt.figure()
        # >>> YOUR CODE HERE >>>
        x = self.df['MathScore']
        y = self.df['WritingScore']
        plt.scatter(x, y, edgecolor='white', alpha=0.95)
        m, b = np.polyfit(x, y, 1)
        plt.plot(x, m*x + b, color='red')
        plt.xlabel('Math Score')
        plt.ylabel('Writing Score')
        plt.title('Scatterplot of Math and Writing Scores with Regression Line')
        # <<< END OF YOUR CODE <<<


        fig.tight_layout()
        fig.savefig(os.path.join(os.path.dirname(
            __file__), "math_writing_scatterplot.png"))

        return fig


if __name__ == "__main__":
    import doctest
    import os

    from utils import print_green, print_red

    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Run the doctests. If all tests pass, print "All tests passed!"
    # You may ignore PYDEV DEBUGGER WARNINGS that appear in the console.
    if doctest.testmod(optionflags=doctest.ELLIPSIS).failed == 0:
        print_green("\nAll tests passed!\n")
    else:
        print_red("\nSome tests failed!\n")
