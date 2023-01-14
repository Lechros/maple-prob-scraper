class CubeDetail:
    def __init__(self):
        self.cube_id = 0
        self.cube_grade = ''
        self.part_name = ''
        self.req_level = 0
        self.probs = {}

    cube_id: int
    cube_grade: str
    part_name: str
    req_level: int
    probs: dict[str, str]
