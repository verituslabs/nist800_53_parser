from typing import NoReturn, List, Dict


class NIST800Parser:
    def __init__(self):
        pass

    def parse_json(self, file_name: str) -> NoReturn:
        raise NotImplementedError

    def get_groups(self) -> List[Dict]:
        raise NotImplementedError

    def get_group_by_group_id(self, group_id: str) -> Dict:
        raise NotImplementedError

    def get_group_by_group_title(self, title: str) -> Dict:
        raise NotImplementedError

    def get_controls(self) -> List[Dict]:
        raise NotImplementedError

    def get_control_by_control_id(self, control_id: str) -> Dict:
        raise NotImplementedError

    def get_crontrols_by_group_id(self, group_id: str) -> List[Dict]:
        raise NotImplementedError

    def get_control_parameters_by_control_id(self, control_id: str) -> List[Dict]:
        raise NotImplementedError

    def get_control_properties_by_control_id(self, control_id: str) -> List[Dict]:
        raise NotImplementedError

    def get_control_links_by_control_id(self, control_id: str) -> List[Dict]:
        raise NotImplementedError

    def get_parts_by_control_id(self, control_id: str) -> List[Dict]:
        raise NotImplementedError

def test_dummy():
    np = NIST800Parser() 
    assert(True == True) #dummy test
