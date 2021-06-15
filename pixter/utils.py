from pathlib import Path


def filepathlist(p: Path, pattern="*.*"):
    """
    Return a list of files in the directory
    Parameters
    ----------
    p : Path
        Director path
    pattern : string
        Path.glob file name pattern
    Returns
    -------
    listOfFiles : List of PosixPath(s)
        List of files
    See Also
    --------
    ku.fileNameList
    Examples
    --------
    >>> flist = ku.filePathList(Path("../temp_del/frames"))
    >>> flist = ku.filePathList(Path("../temp_del/frames"), "img??.png")
    >>> flist = ku.filePathList(Path("../temp_del/frames"), "img*.*")
    """
    if p.exists():
        p = p.glob(pattern)
        return [x for x in p if x.is_file()]
    else:
        msg = "Path does not exist"
        print(msg)
        raise Exception(msg)


def filenamelist(p: Path, pattern="*.*"):
    """
    Return a list of files in the directory
    Parameters
    ----------
    p : Path
        Director path
    pattern : string
        Path.glob file name pattern
    Returns
    -------
    listOfFiles : List of PosixPath(s)
        List of files
    See Also
    --------
    ku.filePathList
    Examples
    --------
    >>> flist = ku.fileNameList(Path("../temp_del/frames"))
    >>> flist = ku.fileNameList(Path("../temp_del/frames"), "img??.png")
    >>> flist = ku.fileNameList(Path("../temp_del/frames"), "img*.*")
    """
    if p.exists():
        p = p.glob(pattern)
        return [x.name for x in p if x.is_file()]
    else:
        msg = "Path does not exist"
        print(msg)
        raise Exception(msg)


def is_notebook():
    """
    Checks if the code is executing in a Jupyter notebook (Not tested in Google Collab)
    Experimental. Use with caution!
    Returns
    -------
    True or False : bool
    Ref
    -------
    https://stackoverflow.com/questions/15411967/how-can-i-check-if-code-is-executed-in-the-ipython-notebook
    """
    try:
        from IPython import get_ipython
        if get_ipython() is None or 'IPKernelApp' not in get_ipython().config:  # pragma: no cover
            return False
    except ImportError:
        return False
    return True