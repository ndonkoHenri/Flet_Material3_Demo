try:
    from .section import Section, SubSection
    from .section_components import actions_section, selection_section, containment_section, communication_section, navigation_section, text_inputs_section
except ModuleNotFoundError:
    from section import Section, SubSection
    from section_components import actions_section, selection_section, containment_section, communication_section, navigation_section, text_inputs_section
