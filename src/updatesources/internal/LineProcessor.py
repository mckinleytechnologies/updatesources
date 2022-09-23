import pathlib


_project_header = "PROJECT="
_search_modifier_delimiter = ","


class Line:
    def __init__(self, line: str):
        self._line = line

    @property
    def is_project_header(self):
        return self._line.startswith(_project_header)

    @property
    def is_commented(self):
        return self._line != "" and self._line[0] == '#'

    @property
    def is_empty(self):
        return self._line == ""

    def get_project_name(self):
        return self._line.replace(_project_header, "")

    def get_path_and_operation(self, search_root):
        first_char = self._line[0]
        if first_char == '+':
            remaining = self._line[1:]
            operation = 'add'

        elif first_char == '-':
            remaining = self._line[1:]
            operation = 'ignore'

        else:
            remaining = self._line
            operation = 'add'

        path_string, modifiers = _extract_modifiers(remaining)
        path = pathlib.Path(search_root).joinpath(path_string).resolve()
        return operation, path, modifiers


def _extract_modifiers(item):
    if _search_modifier_delimiter not in item:
        path = item
        modifiers = ["**.cpp", "**.h"]

    else:
        tokens = item.split(_search_modifier_delimiter)
        path = tokens[0]
        modifiers = tokens[1:]

    return path, modifiers

