try:
    from .SubSection import SubSection
    from .Section import Section
except ModuleNotFoundError:
    from SubSection import Subsection
    from Section import Section