import json

# Define the list of coding questions
from questions import coding_questions

# Create a list to store cell information
notebook_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# Coding Interview Questions\n",
            "\n",
            "This Jupyter Notebook contains Python code for 100 coding interview questions.\n",
            "Feel free to use it for interview preparation or as a reference.\n"
        ]
    }
]

# Add cells for each coding question
for i, question in enumerate(coding_questions, start=1):
    cell_info = {
        "cell_type": "code",
        "execution_count": i,
        "metadata": {},
        "outputs": [],
        "source": [
            f"# Question {i}\n",
            f"# {question}\n",
            ""
        ]
    }
    notebook_cells.append(cell_info)

# Add a closing markdown cell
notebook_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "# End of Coding Questions\n",
        "\n",
        "This concludes the list of 100 coding interview questions.\n"
    ]
})

# Create the notebook content by joining cell information
notebook_content = {
    "cells": notebook_cells,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.7.6"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Save the notebook content to a file
with open("coding_interview_questions.ipynb", "w") as notebook_file:
    json.dump(notebook_content, notebook_file, indent=2)

print("Jupyter Notebook created: coding_interview_questions.ipynb")
