from maple_prob_scraper.resource.cube import CubeId, Grade, PartType


class CubeDetail:
    def __init__(self):
        self.cube_id = CubeId.suspicious_cube
        self.cube_grade = Grade.rare
        self.part_type = PartType.cap
        self.req_level = 0
        self.probs = {}

    def __str__(self) -> str:
        return f'''info: {self.cube_id}, {self.cube_grade}, {self.part_type}, req_level={self.req_level}
probs: {str(self.probs)}'''

    cube_id: CubeId
    cube_grade: Grade
    part_type: PartType
    req_level: int
    probs: dict[str, str]
