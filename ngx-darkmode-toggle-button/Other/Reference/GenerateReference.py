import sys
from pathlib import Path
from TasksForCommonProjectStructure import TasksForCommonProjectStructure


def generate_reference():
    TasksForCommonProjectStructure().standardized_tasks_generate_reference_by_docfx(str(Path(__file__).absolute()), 1,  sys.argv)


if __name__ == "__main__":
    generate_reference()
