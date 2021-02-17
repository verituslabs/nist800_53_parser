from typing import NoReturn, List, Dict


class NIST800Parser:
    def __init__(self):
        pass

    def parse_json(
        self,
        file_name: str = "data/nist.gov/SP800-53/rev4/xml/NIST_SP-800-53_rev4_catalog.xml",
    ) -> NoReturn:
        # I think you just need to parse this file
        # NIST_SP-800-53_rev4_catalog.json
        # use a tool like http://jsonviewer.stack.hu/
        # to help you
        # NOTE: this corresponds to the NIST 800.53 rev 4
        # Appendix F -- roughly page 159 (F-1)
        #
        # you probably want to store the parsed json
        # as self.catalog
        # HINT: read:
        # data/nist.gov/SP800-53/rev4/xml/NIST_SP-800-53_rev4_catalog.xml
        raise NotImplementedError

    def get_groups(self) -> List[Dict]:
        # return a list of Dicts where eact Dict is a group
        raise NotImplementedError

    def get_group_by_group_id(self, group_id: str) -> Dict:
        # return a Dict which is a group with given group_id
        raise NotImplementedError

    def get_group_by_group_title(self, title: str) -> Dict:
        # return a Dict which is a group with given title
        raise NotImplementedError

    def get_controls(self) -> List[Dict]:
        # return a List of Dicts where each Dict is a Control
        # (all controls in the catalog)
        raise NotImplementedError

    def get_control_by_control_id(self, control_id: str) -> Dict:
        # return a Dict which is a control with the given control_id
        raise NotImplementedError

    def get_crontrols_by_group_id(self, group_id: str) -> List[Dict]:
        # return a list of Dicts where each Dict is a control for
        # a group with the given group_id
        raise NotImplementedError

    def get_control_parameters_by_control_id(self, control_id: str) -> List[Dict]:
        # return a list of Dicts where each Dict is a control parameter for
        # a control with the given control_id
        raise NotImplementedError

    def get_control_properties_by_control_id(self, control_id: str) -> List[Dict]:
        # return a list of Dicts where each Dict is a control property for
        # a control with the given control_id
        raise NotImplementedError

    def get_control_links_by_control_id(self, control_id: str) -> List[Dict]:
        # return a list of Dicts where each Dict is a control link for
        # a control with the given control_id
        raise NotImplementedError

    def get_parts_by_control_id(self, control_id: str) -> List[Dict]:
        # return a list of Dicts where each Dict is a control part for
        # a control with the given control_id
        raise NotImplementedError


def test_dummy():
    np = NIST800Parser()
    assert True == True  # dummy test
