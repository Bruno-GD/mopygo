from os import getcwd
from os.path import join, isdir

from .utils.hugo.checkFolderStructure import isFolderStructure
from .utils.hugo.createHugoStructure import createHugoStructure
from .utils.hugo.populateContents import populateContents
from .utils.hugo.clearHugoContent import clearHugoContent


def generateSite(
    sections: list, elements: dict, *, outputFolder: str = join(getcwd(), "site")
) -> None:
    """
    Generate site from a list of sections and
    populate with elements inside of each section
    """

    # preconditions
    assert isinstance(sections, list)
    assert isinstance(elements, dict)
    assert isinstance(outputFolder, str)

    # logic
    if isdir(outputFolder):
        clearHugoContent(outputFolder)
    else:
        createHugoStructure(outputFolder)

    populateContents(outputFolder, sections, elements)

    # postcondition
    assert isFolderStructure(outputFolder)