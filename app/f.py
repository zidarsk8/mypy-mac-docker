from typing import TYPE_CHECKING

from app.foo.bar import Activity

if TYPE_CHECKING:
    from app.c import Company


# uncommenting class below shows the invalid error, but with less info on
# what's going on.

# class FormTemplate:
#     pass
