from maple_prob_scraper.converter.cube import get_cube_detail
from maple_prob_scraper.resource.cube import CubeId, Grade, PartType
from maple_prob_scraper.type.cube_detail import CubeDetail


class CubeApp:
    cube_id = CubeId.suspicious_cube
    cube_grade = Grade.rare
    must_part = [
        PartType.weapon,
        PartType.pants,
        PartType.coat,
        PartType.pants,
        PartType.gloves,
        PartType.shoes,
        PartType.faceAccessory,
    ]
    default_req_level = 120

    def run(self) -> list[CubeDetail]:
        if self.cube_id == CubeId.suspicious_cube:
            if self.cube_grade in [Grade.unique, Grade.legendary]:
                raise ValueError()
        elif self.cube_id == CubeId.craftmans_cube:
            if self.cube_grade in [Grade.legendary]:
                raise ValueError()

        details = []
        for part in self.must_part:
            details.append(
                get_cube_detail(
                    self.cube_id,
                    self.cube_grade,
                    part,
                    self.default_req_level
                )
            )

        return details