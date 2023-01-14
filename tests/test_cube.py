from maple_prob_scraper.converter.cube import get_cube_detail
from maple_prob_scraper.resource.cube import CubeId, Grade, PartType
from maple_prob_scraper.type.cube_detail import CubeDetail


def test_get_cube_detail():
    detail: CubeDetail = get_cube_detail(CubeId.red_cube, Grade.epic, PartType.shoes, 120)

    assert detail.cube_id == CubeId.red_cube
    assert detail.cube_grade == Grade.epic
    assert detail.part_type == PartType.shoes
    assert detail.req_level == 120
    assert len(detail.probs) > 0